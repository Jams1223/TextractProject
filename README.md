# TextractProject

# This project assumes you have an aws account to work with

To install all dependecies
---------------------------------------

pip install -r requirements.txt

---------------------------------------
To install aws cli
---------------------------------------

$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /

---------------------------------------
To verfiy installation of aws cli
---------------------------------------

$ which aws
  should return -> /usr/local/bin/aws 
$ aws --version
  should return -> aws-cli/2.10.0 Python/3.11.2 Darwin/18.7.0 botocore/2.4.5
  
 
---------------------------------------
Create IAM user that has Textract access role as well as S3 bucket
---------------------------------------

https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html

https://docs.aws.amazon.com/textract/latest/dg/security-iam.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html

---------------------------------------
Follow instructions to log into aws creditinals
---------------------------------------

https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html
---------------------------------------
Things to change
---------------------------------------

In analyzeText.py, change 

```client = session.client('textract', region_name='us-east-1')``` 

the region name to your region

---------------------------------------
```   text = client.detect_document_text(
        Document ={
            'S3Object': {
            'Bucket': 'jams122bucket',
            'Name': filename
        }
        }
    )
```
 change Bucket to your bucket name

---------------------------------------
Running the project
---------------------------------------

cd into project directory and run "flask run" on terminal

