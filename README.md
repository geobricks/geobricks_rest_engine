Geobricks REST Engine
=====================

The main purpose of this project is to provide a deployable and configurable entry point for the Geobricks REST services. 

The Geobricks project takes advantage of the [blueprints](http://flask.pocoo.org/docs/0.10/blueprints/) concept to create modular components which provide services to the users. This project consist of a single [REST service](https://github.com/geobricks/geobricks_rest_engine/blob/master/geobricks_rest_engine/rest/engine.py) which loads modules at the start-up of the application and provides a single entry point to the Geobricks web services. 

The REST engine can be easilly configured through a simple [settings file](https://github.com/geobricks/geobricks_rest_engine/blob/master/geobricks_rest_engine/config/settings.py) which contains an array of objects named `modules`. Each object describes a Geobricks service and provides the parameters to load the module. The following example describes the configuration needed to load the Geobricks MODIS plug-in:
```python
{
  "description": "MODIS",
  "path_to_the_blueprint": "geobricks_modis.rest.modis_rest",
  "blueprint_name": "modis",
  "url_prefix": "/browse/modis"
}
```
The following table provides a description of each parameter of the configuration objects.

|Parameter Name|Description|Mandatory|
|--------------|-----------|:-------:|
|description|Human readable description. This parameter is only used to make the configuration file more comprehensible and easy to mantain.|No|
