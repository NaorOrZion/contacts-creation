from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '2774a55e98aeed2030491d89dfb15ace96aea055' # madorlibaiscool -> SHA1 hash

    from .navigation import navigation

    app.register_blueprint(navigation, url_prefix='/')

    return app