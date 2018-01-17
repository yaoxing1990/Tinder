#!/usr/bin/python3
import fb_auth_token
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
api = Api(app)

class GetToken(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, help='id')
        parser.add_argument('password', type=str, help='password')
        args = parser.parse_args()
        fb_username = args['id']
        fb_password = args['password']
        fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
        fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
        result = {'fb_access_token' : fb_access_token, 'fb_user_id' : fb_user_id}
        return jsonify(result)


api.add_resource(GetToken, '/')


if __name__ == '__main__':
     app.run()
