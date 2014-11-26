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


# Initialize the Flask app
app = Flask(__name__)

# Logging level.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*', 'headers': ['Content-Type']}})

# Dynamic import of modules specified in config.settings.py
for module in rest_settings['modules']:

    # Load module
    mod = import_module(module['path_to_the_blueprint'])

    # Overwrite modules settings
    conf_mod = import_module(module['path_to_the_config'])
    conf = getattr(conf_mod, 'config')
    conf['common_settings'] = dict_merge(conf, common_settings)

    # Load Blueprint
    rest = getattr(mod, module['blueprint_name'])

    # Register Blueprint
    app.register_blueprint(rest, url_prefix=module['url_prefix'])

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


# Start Flask server
if __name__ == '__main__':
    app.run(host=rest_settings['host'], port=rest_settings['port'], debug=rest_settings['debug'], threaded=True)