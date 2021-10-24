from flask import Flask, jsonify
from config import Config
from flask_cors import CORS


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 跨域
    CORS(app)

    @app.route('/')
    def hello_world():
        return '王子烨是zhui牛逼的'



    # 注册蓝图 blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app