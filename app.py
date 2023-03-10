import os

from flask import Flask, render_template

from auth import login_required


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'feed50.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/')
    @login_required
    def index():
        articles = feed.articles()
        if not articles:
            return render_template('index.html')

        return render_template('index.html', articles=articles)

    import db
    db.init_app(app)

    import auth
    app.register_blueprint(auth.bp)

    import feed
    app.register_blueprint(feed.bp)

    app.add_url_rule('/', endpoint='index')

    return app
