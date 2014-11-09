import logging
from flask import Flask
from flask.ext.cors import CORS
from importlib import import_module
from flask.ext.cors import cross_origin
from geobricks_rest_engine.config.settings import settings


# Initialize the Flask app
app = Flask(__name__)

# Initialize CORS filters
cors = CORS(app, resources={r'/*': {'origins': '*'}})

# Root REST
@app.route('/')
@cross_origin(origins='*')
def root():
    return 'Welcome to Geobricks!'

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