# project/server/auth/views.py

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User
import json

list_blueprint = Blueprint('list', __name__)

class ListAPI(MethodView): 
    """
    User Registration Resource
    """

    def post(self):
        # get the post data
        post_data = request.get_json(); print(request)
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if user:
            userList = User.query.all()
            userEmails=[]
            for i in userList:
                userEmails.append(i.email)
            try:
                responseObject = {
                    'status': 'success',
                    'message': json.dumps(userEmails),
                    #'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202


# define the API resources
list_view = ListAPI.as_view('list_api')

# add Rules for API Endpoints
list_blueprint.add_url_rule(
    '/users/index',
    view_func=list_view,
    methods=['POST']
)