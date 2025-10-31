import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

# --- CONFIGURACIÓN ---
URL_BASE = "http://books.toscrape.com/"
OUTPUT_FILE = 'analisis_competencia_seo.csv'
# ---------------------

def extraer_datos_producto(url):
    """Extrae el título, precio y ficha técnica de forma robusta."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'lxml')

        titulo_tag = soup.find('h1')
        titulo = titulo_tag.text.strip() if titulo_tag else "N/A"

        precio_tag = soup.find(class_='price_color')
        precio = precio_tag.text.strip() if precio_tag else "N/A"

        datos = {'URL': url, 'Titulo_Producto': titulo, 'Precio_Competencia': precio}
        caracteristicas = {}

        try:
            tabla = soup.find(class_='table table-striped')
            if tabla:
                for fila in tabla.find_all('tr'):
                    celdas = fila.find_all('td')
                    if len(celdas) == 2:
                        nombre = celdas[0].text.strip()
                        valor = celdas[1].text.strip()
                        caracteristicas[nombre] = valor

            datos.update(caracteristicas)

        except Exception as e:
            print(f"⚠️ Aviso: Error al extraer ficha técnica en {url}: {e}")
            pass

        return datos

    except requests.exceptions.RequestException as e:
        print(f"⛔ Error de conexión al procesar {url}: {e}")
        return None


def analizar_competencia_y_exportar(url_base):
    print(f"✅ Analizando página base para encontrar productos: {url_base}")

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['URL', 'Titulo_Producto', 'Precio_Competencia', 'UPC', 'Product Type', 'Price', 'Tax']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()

       try:
            # 1. Obtener la respuesta de la URL base
            response_base = requests.get(url_base, timeout=10)
            
            # 2. Verificar si la respuesta es exitosa (código 200)
            if response_base.status_code != 200:
                print(f"⛔ Error: No se pudo acceder a la URL base. Status: {response_base.status_code}")
                return # Detiene la función si falla la conexión
            
          

            soup_base = BeautifulSoup(response_base.text, 'lxml')
            enlaces_productos = []

            for enlace in soup_base.find_all('a'):
                href = enlace.get('href')
                if href and 'catalogue' in href:
                    full_url = urljoin(URL_BASE, href)
                    enlaces_productos.append(full_url)

            urls_unicas = list(set(enlaces_productos))
            print(f"🔗 Encontrados {len(urls_unicas)} enlaces de productos únicos. Iniciando extracción...")

            for i, url_producto in enumerate(urls_unicas[:10]):
                datos = extraer_datos_producto(url_producto)
                if datos:
                    writer.writerow(datos)
                    print(f"    -> {i+1}. Extraído: {datos['Titulo_Producto'][:40]}...")
                time.sleep(0.5)

            print("-" * 40)
            print(f"✅ ¡Automatización SEO completa! Datos guardados en: {OUTPUT_FILE}")

        except requests.exceptions.RequestException as e:
            print(f"⛔ Error de conexión al iniciar el rastreo: {e}")


if __name__ == '__main__':
    analizar_competencia_y_exportar(URL_BASE)