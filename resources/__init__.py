from flask import Flask, jsonify
from resources.config import Config
from dotenv import load_dotenv
# from flask_smorest import Api
from flask_restful import Api 
# from resources.views import blp as VideoBlueprint
from resources.handles import VideoListResource, VideoToDisk, TranscribeVideo
import os
from flask_cors import CORS

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config.from_object(Config)
    api = Api(app)
    
    CORS(app, resources={r"/*"}, origins="*")
    

    @app.route("/")
    def hello():
        return jsonify({"greeting": "Hello World"})

    # api.register_blueprint(VideoBlueprint)
    api.add_resource(VideoListResource, "/videos")
    api.add_resource(VideoToDisk, "/videos/upload")
    api.add_resource(TranscribeVideo, "/videos/<filename>/transcribe")

    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])

    return app