Geobricks REST Engine
=====================

The main purpose of this project is to provide a deployable and configurable entry point for the Geobricks REST services. 

The Geobricks project takes advantage of the [blueprints](http://flask.pocoo.org/docs/0.10/blueprints/) concept to create modular components which provide services to the users. This project consist of a single [REST service](../blob/master/geobricks_rest_engine/rest/engine.py) which loads modules at the start-up of the application and provides a single entry point to the Geobricks web services. 

The REST engine can be easilly configured through a simple [settings file](../blob/master/geobricks_rest_engine/config/settings.py) which contains an array of objects named `modules`. Each object describes a Geobricks service and provides the parameters to load the module. The following example describes the configuration needed to load the Geobricks MODIS plug-in:
```python
{
  "description": "MODIS",
  "path_to_the_blueprint": "geobricks_modis.rest.modis_rest",
  "blueprint_name": "modis",
  "url_prefix": "/browse/modis"
}
```
The following table provides a description of each parameter of the configuration objects.

|Name|Description|Mandatory|
|--------------|-----------|:-------:|
|description|Human readable description. This parameter is only used to make the configuration file more comprehensible and easy to mantain.|No|
|path_to_the_blueprint|The import path to the Python file which contains the blueprint.|Yes|
|blueprint_name|The name of the blueprint variable.|Yes|
|url_prefix|Every web service defined by the blueprint will be preceeded by this string. |Yes|

The `url_prefix` is very useful to group all the services provided by a module with a single entry point. As istance, every service provided by the Geobricks MODIS plug-in will be introduced by the `/browse/modis` prefix. The next table shows how the URL's are modified by the prefix.

|Original URL|Prefix|REST Engine URL|
|------------|------|---------------|
|http://example.com/|/browse/modis/|http://example.com/browse/modis/|
|http://example.com/MOD13Q1/|/browse/modis/|http://example.com/browse/modis/MOD13Q1/|
