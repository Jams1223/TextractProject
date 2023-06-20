# TextractProject

To install all dependecies

pip install -r requirements.txt

to install aws cli

$ curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
$ sudo installer -pkg AWSCLIV2.pkg -target /

To verfiy installation of aws cli run

$ which aws
  should return -> /usr/local/bin/aws 
$ aws --version
  should return -> aws-cli/2.10.0 Python/3.11.2 Darwin/18.7.0 botocore/2.4.5
  
cd into project directory and run "flask run" on terminal

