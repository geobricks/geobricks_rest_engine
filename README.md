Geobricks REST Engine
=====================

The purpose of this project is to provide a deployable and configurable entry point for the Geobricks REST services. The projects consist of a REST service called `engine.py` located in the `geobricks_rest_engine/rest` package which acts as a main entry point for the Geobricks REST services. The engine REST service reads the `settings.py` configuration file stored in the `geobricks_rest_engine/config` package. This files contains an array of objects named `modules`: each object describes a Geobricks service and provide the parameters to load the module.
