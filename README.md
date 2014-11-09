Geobricks REST Engine
=====================

The main purpose of this project is to provide a deployable and configurable entry point for the Geobricks REST services. 

Geobricks project takes advantage of the [Flask Blueprints](http://flask.pocoo.org/docs/0.10/blueprints/) The projects consist of a REST service called `engine.py` located in the `geobricks_rest_engine/rest` package which acts as a main entry point for the Geobricks REST services. The engine REST service reads the `settings.py` configuration file stored in the `geobricks_rest_engine/config` package. This files contains an array of objects named `modules`. Each object describes a Geobricks service and provide the parameters to load the module. The following example describes the configuration needed to load the Geobricks MODIS plug-in:
```python
{
  "description": "MODIS",
  "path_to_the_blueprint": "geobricks_modis.rest.modis_rest",
  "blueprint_name": "modis",
  "url_prefix": "/browse/modis"
}
```
