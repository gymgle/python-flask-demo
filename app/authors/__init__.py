from flask import Blueprint
from flask_restful import Api

authors_bp = Blueprint('authors_blueprint', __name__)
authors_api = Api(app=authors_bp)

from .authors import *

authors_api.add_resource(AuthorsAPI, '/authors')
authors_api.add_resource(AuthorDetailAPI, '/authors/<id>')
