from flask_restful import Api
from flask import Blueprint
from .controller import GenerarLinkDeFoto

multimediaBlueprint = Blueprint('multimediaBlueprint', __name__)

multimediaRouter = Api(multimediaBlueprint)

multimediaRouter.add_resource(GenerarLinkDeFoto, '/generar-upload-link')
