from flask_restplus import Api
from apis.file_uploader_namespace import api as file_uploader_ns

api = Api(
    title='File Uploader',
    version='1.0',
    description='Api to upload file to Google bucket'
)

api.add_namespace(file_uploader_ns)
