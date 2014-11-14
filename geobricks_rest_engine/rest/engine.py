import json
import logging
import urllib2
from flask import Flask
from flask import request
from flask import Response
from flask.ext.cors import CORS
from importlib import import_module
from flask.ext.cors import cross_origin
from geobricks_rest_engine.config.settings import settings


# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*'}})

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

# Dynamic import of modules specified in config.settings.py
for module in settings['modules']:

    # Load module
    mod = import_module(module['path_to_the_blueprint'])

    # Load Blueprint
    rest = getattr(mod, module['blueprint_name'])

    # Register Blueprint
    app.register_blueprint(rest, url_prefix=module['url_prefix'])

# Logging level.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Start Flask server
if __name__ == '__main__':
    app.run(host=settings['host'], port=settings['port'], debug=settings['debug'], threaded=True)