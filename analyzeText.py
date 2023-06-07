#takes in s3Object

from uploadFile import session,s3_connection,bucket

client = session.client('textract', region_name='us-east-1')

def getText(filename):
    text = client.detect_document_text(
        Document ={
            'S3Object': {
            'Bucket': 'jams122bucket',
            'Name': filename
        }
        }
    )
    response = ""
    for t in text['Blocks']:
        if t.get('Text') != None:
            response = response+" " + t.get('Text')
    return response


# print(getText('testFile'))