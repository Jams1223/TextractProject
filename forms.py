from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField,SelectField, StringField

# class Additem(FlaskForm):
#     id = IntegerField(label= 'id', validators=[DataRequired()])
#     item_name = StringField(label='item_name',  validators=[DataRequired()])
#     item_price = IntegerField(label='item_price',  validators=[DataRequired()])
#     item_image = StringField(label='image_path',validators=[DataRequired()])
#     item_type = StringField(label='type',  validators=[DataRequired()])
#     item_c = IntegerField(label='c type',  validators=[DataRequired()])
#     submit = SubmitField(label='add')

class InputImage(FlaskForm):
    fileName = StringField()
    image = FileField(validators=[FileRequired(),FileAllowed(['jpg','png'],'Images only!')])
    submit = SubmitField(label='Upload image')

class AnalyzeImage(FlaskForm):
    image_ = SelectField(u"Choose Image ",choices=[],validate_choice=True)
    submit = SubmitField(label="Analyze Image")