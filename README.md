# CarPriceScraper

## Espa�ol

Esta pr�ctica se ha realizado bajo el contexto de la asignatura Tipolog�a y ciclo de vida de los datos, perteneciente al M�ster en Ciencia de Datos de la Universitat Oberta de Catalunya (UOC). En ella, se aplican t�cnicas de web scraping mediante el lenguaje de programaci�n Python para extraer as� datos de la web [Milanuncios.com](httpswww.milanuncios.com) y generar un [dataset](https://doi.org/10.5281/zenodo.5651148) sobre coches usados a la venta. 

## English
This assignment has been carried out as part of Tipolog�a y ciclo de vida de los datos course, belonging to the Master in Data Science at the Universitat Oberta de Catalunya (UOC). Web scraping techniques are applied using Python programming language in order to extract data from [Milanuncios.com](httpswww.milanuncios.com) website and create a [dataset](https://doi.org/10.5281/zenodo.5651148) of used cars on sale. 

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
Team members
 David Dur�n
 Pablo Mart�nez

## License
 Code [MIT](httpschoosealicense.comlicensesmit)
 Dataset [CC BY-NC-SA 4.0](httpscreativecommons.orglicensesby-nc-sa4.0)