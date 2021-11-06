[<https://www.uoc.edu/portal/system/modules/edu.uoc.presentations/resources/img/branding/logo-uoc-default.png_1618809817.png">](https://uoc.edu/)

# CarPriceScraper

## Español

Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos, perteneciente al Máster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC). En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web [Milanuncios.com](httpswww.milanuncios.com) y generar un [dataset](https://doi.org/10.5281/zenodo.5651148) sobre coches usados a la venta. 

## English
This assignment has been carried out as part of Tipología y ciclo de vida de los datos course, belonging to the Master in Data Science at the Universitat Oberta de Catalunya (UOC). Web scraping techniques are applied using Python programming language in order to extract data from [Milanuncios.com](httpswww.milanuncios.com) website and create a [dataset](https://doi.org/10.5281/zenodo.5651148) of used cars on sale. 

## Installation

Use the package manager [pip](httpspip.pypa.ioenstable) to install the required libraries as per requirements.txt.

```bash
pip install -r requirements.txt
```

## Usage
Go to the scrapy project directory
```python
cd milpymilpy
```
Run this command to start the spider.
```
scrapy crawl ads -O output_filename.csv --set delimiter=';'
```
Use `-O output_filename.csv` to save the scraped data and `--set delimiter=';'` to choose the variable delimiter.

## Authors
**Team members**

 David Durán
 
 Pablo Martínez

## License
 Code [MIT](httpschoosealicense.comlicensesmit)
 
 Dataset [CC BY-NC-SA 4.0](httpscreativecommons.orglicensesby-nc-sa4.0)
 
 [<img src="https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png">](https://licensebuttons.net)
