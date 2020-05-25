from flask import Flask, g
from flask_restful import Api

from config import AppConfig
from server.health.endpoint import Health, HealthGAE
from server.api.image_endpoint import ProcessImageEndpoint
from server.api.text_endpoint import ProcessTextEndpoint
from server.services import AppServiceSingleton


def create_app():
    def add_endpoints():
        # Warm Up for Google App Engine
        api.add_resource(HealthGAE, '/_ah/warmup')
        # Health Endpoint
        api.add_resource(Health, '/health')
        # Process Image Endpoint
        api.add_resource(ProcessImageEndpoint, '/analyze/image')
        # Process Text Endpoint
        api.add_resource(ProcessTextEndpoint, '/analyze/text')

    # TODO: Look into parallelism: https://medium.com/@dkhd/handling-multiple-requests-on-flask-60208eacc154
    config = AppConfig()
    app = Flask(__name__)
    api = Api(app)
    add_endpoints()

    @app.before_request
    def init_services():
        """
        This populates the global context object with the required services
        """
        g.services = AppServiceSingleton(config.vision_cred_filepath, config.ingredients_db_dirpath)

    return app


if __name__ == '__main__':
    # This is used when running locally only. Deployments will use Gunicorn
    app = create_app()
    app.run(debug=True, port=5000)
