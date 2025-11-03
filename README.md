 # 🐍 Analizador de Competencia SEO y Precios para E-commerce

## 💡 Propósito del Proyecto
Este script de Python automatiza la recopilación de datos de la competencia (Web Scraping) para obtener información clave de SEO y E-commerce. Está diseñado para dueños de negocios (como tiendas de laptops o Etsy) y analistas que necesitan **tomar decisiones rápidas de pricing y optimización de producto.**

## 🎯 ¿Qué Resuelve?
En el mundo del E-commerce, los precios y las especificaciones técnicas (fichas técnicas) de la competencia cambian constantemente. Analizar esto manualmente es lento e ineficiente.

Este script ofrece:
1.  **Monitoreo de Precios:** Recopilación automatizada del precio de lista.
2.  **Análisis de Fichas Técnicas:** Extracción detallada de especificaciones del producto (como UPC, Product Type, características extra). Esto es crucial para **optimizar los listados SEO** y asegurar que tus productos no estén sub-especificados frente a la competencia.
3.  **Código Robusto:** Incluye manejo de errores de conexión y de datos faltantes, asegurando que el proceso no se detenga si una página falla.

## ⚙️ Tecnologías Utilizadas
* **Python:** Lenguaje principal de desarrollo.
* **Requests:** Para realizar peticiones HTTP (descargar la página web).
* **BeautifulSoup (BS4):** Para el parseo del HTML y la extracción de datos específicos (títulos, precios, tablas).
* **CSV:** Para la exportación de resultados listos para análisis en Excel o Google Sheets.
* **Manejo de Errores (`try/except`):** Para garantizar la estabilidad de la automatización.

## 🚀 Cómo Usar el Script
1.  **Clonar el Repositorio:** Descarga los archivos en tu máquina.
2.  **Instalar Dependencias:** Abre tu terminal y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Ejecutar el Script:**
    ```bash
    python seo_analizador_pro.py
    ```

## ✅ Resultados
El script genera el archivo `analisis_competencia_seo.csv` con las siguientes columnas:
* URL
* Titulo_Producto
* Precio_Competencia
* UPC
* Product Type
* *Y cualquier otra especificación encontrada en la ficha técnica.*