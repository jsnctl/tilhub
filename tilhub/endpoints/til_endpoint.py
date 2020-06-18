from flask import jsonify
from flask_restful import Resource
from controllers.til_controller import TILController

controller = TILController()


class TILEndpoint(Resource):

    def get(self, id):
        til = controller.get_til_by_id(id)
        return jsonify(til)
