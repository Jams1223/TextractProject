# using python flask, have user upload a file, upload this file to AWS s3 bucket
import boto3
import io
from PIL import Image, ImageDraw

session = boto3.Session()
s3_connection = session.resource('s3')
bucket = s3_connection.Bucket('jams122bucket')

def uploadS3(file,fileName):
    bucket.upload_file(file,fileName)