import boto3
import io
from PIL import Image, ImageDraw

session = boto3.Session()
s3_connection = session.resource('s3')
bucket = s3_connection.Bucket('jams122bucket')
client = session.client('textract', region_name='us-east-1')


# bucket.upload_file('text3.png',"testIMage2")
# response = ""
# for obj in bucket.objects.all():
#     text = client.detect_document_text(
#         Document ={
#             'S3Object': {
#             'Bucket': 'jams122bucket',
#             'Name': 'text.jpg'
#         }
#         }
#     )
#     for t in text['Blocks']:
#         if t.get('Text') != None:
#             response = response+" " + t.get('Text')

#prints the fileName of all things in the s3 bucket
for obj in bucket.objects.all():
    print(obj.key)

# print(response)




