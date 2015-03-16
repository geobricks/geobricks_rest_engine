import json
import logging
import urllib2
from flask import Flask
from flask import request
from flask import Response
from flask.ext.cors import CORS
from importlib import import_module
from flask.ext.cors import cross_origin
from geobricks_rest_engine.config.rest_settings import settings as rest_settings
from geobricks_rest_engine.config.common_settings import settings as common_settings
from geobricks_rest_engine.core.utils import dict_merge
from geobricks_rest_engine.core.log import logger

# Logger
log = logger(__file__)

# werkzeug logging level.
logging.getLogger('werkzeug').setLevel(logging.INFO)

# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*', 'headers': ['Content-Type']}})


# Dynamic import of modules specified in config.settings.py
def load_modules():
    for module in rest_settings['modules']:

        try:
            try:
                # Overwrite modules settings
                conf_mod = import_module(module['path_to_the_config'])
                conf_mod.config["settings"] = dict_merge(conf_mod.config, common_settings)
                conf_mod.config["settings"] = conf_mod.config["settings"]["settings"]
            except Exception, e:
                log.warning(e)

            try:
                # Load module
                mod = import_module(module['path_to_the_blueprint'])

                # Load Blueprint
                rest = getattr(mod, module['blueprint_name'])

                # Register Blueprint
                app.register_blueprint(rest, url_prefix=module['url_prefix'])
                log.info("Module loaded: " + module['path_to_the_blueprint'])
            except Exception, e:
                log.warning(e)
        except Exception, e:
            log.warning(e)

@app.route('/')
@cross_origin(origins='*')
def root():
    """
    Root REST service.
    @return: Welcome message.
    """
    return 'Welcome to Geobricks!'

@app.route('/discovery/')
@cross_origin(origins='*')
def discovery():
    """
    Discovery service to list all the available Geobricks plug-ins.
    @return: List of objects describing the plug-in: name, description and type.
    """
    rules = []
    for r in app.url_map.iter_rules():
        rule_name = str(r)
        if '.' in r.endpoint and rule_name.endswith('/') and 'discovery' in rule_name:
            discovery_url = request.host_url + rule_name[1:]
            plugin_description = json.load(urllib2.urlopen(discovery_url))
            rules.append(plugin_description)
    rules.sort()
    return Response(json.dumps(rules), content_type='application/json; charset=utf-8')


@app.route('/discovery/service/url/name/<name>/')
@cross_origin(origins='*')
def discovery_by_name(name):
    """
    Discovery service url by name
    @return: List the url to call the service
    """
    result = {}
    for r in app.url_map.iter_rules():
        rule_name = str(r)
        if '.' in r.endpoint and rule_name.endswith('/') and 'discovery' in rule_name:
            discovery_url = request.host_url + rule_name[1:]
            print discovery_url
            plugin_description = json.load(urllib2.urlopen(discovery_url))
            if "name" in plugin_description:
                if plugin_description["name"] == name:
                    result["url"] = (request.host_url + rule_name[1:]).replace("discovery/", "")
    return Response(json.dumps(result), content_type='application/json; charset=utf-8')


@app.route('/discovery/<type>/')
@cross_origin(origins='*')
def discovery_by_type(type):
    """
    Discovery service to list all the available Geobricks plug-ins.
    @return: List of objects describing the plug-in: name, description and type.
    """
    rules = []
    for r in app.url_map.iter_rules():
        rule_name = str(r)
        if '.' in r.endpoint and rule_name.endswith('/') and 'discovery' in rule_name:
            discovery_url = request.host_url + rule_name[1:]
            plugin_description = json.load(urllib2.urlopen(discovery_url))
            if type.upper() in plugin_description['type'].upper():
                rules.append(plugin_description)
    rules.sort()
    return Response(json.dumps(rules), content_type='application/json; charset=utf-8')


def run_engine():
    app.run(host=rest_settings['host'], port=rest_settings['port'], debug=rest_settings['debug'], threaded=True)


# Start Flask server
if __name__ == '__main__':
    # load modules
    load_modules()
    # run REST engine
    run_engine()
