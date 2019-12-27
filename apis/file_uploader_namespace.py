from flask_restplus import Namespace, Resource
from flask import request
from google.cloud import storage

api = Namespace('FileUploader', description='Upload file to Google bucket')


@api.route("/uploadFile")
class FileUploader(Resource):
    def post(self):

        try:
            client = storage.Client.from_service_account_json("path_to_your_credential_json_file")
            bucket = client.bucket("your_bucket_name")
            bucket.blob(request.headers['FileName']).upload_from_string(request.data)

            return {'task': 'Success'}, 200

        except Exception as e:
            return {'task': e}, 500

