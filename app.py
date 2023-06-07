from flask import Flask,render_template, redirect,url_for
from forms import InputImage,AnalyzeImage
from werkzeug.utils import secure_filename
from uploadFile import uploadS3,bucket
from analyzeText import getText
app = Flask(__name__)
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/",methods ={"POST" ,"GET"})
def upload_image():
    form = InputImage()

    if form.validate_on_submit():
        f = form.image.data
        filename = secure_filename(f.filename)
        f.save(filename)
        uploadS3(filename,form.fileName.data)

        return redirect('/')
    
    aform = AnalyzeImage()
    aform.image_.choices = [(obj.key,obj.key) for obj in bucket.objects.all()]

    if aform.validate_on_submit():
        text = getText(aform.image_.data)
        return render_template('home2.html', form = form,aform=aform,text=text)

    
    return render_template('home.html', form = form,aform=aform)
