# Application Factory
# Dual purpose: 
# creation of Flask instance inside a function
# tells Python which flaskr directory should be treated as package

import os

from flask import Flask

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True) # creates Flask instance
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    
    from . import db
    db.init_app(app)

    if not os.path.exists(app.config['DATABASE']):
        with app.app_context():
            db.init_db()

    from . import auth
    app.register_blueprint(auth.bp)

    from  . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    return app