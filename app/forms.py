from flask_wtf import FlaskForm
from wtforms import FileField,TextAreaField,SelectField,StringField
from wtforms.validators import DataRequired,Regexp



class PropertyForm(FlaskForm):
    
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description [500 words max]', validators=[DataRequired()])
    rooms=StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms=StringField('No. of Bathrooms', validators=[DataRequired()])
    price=StringField('Price', validators=[DataRequired()])
    ptype=SelectField(u'Property Type', choices=[('House'),('Apartment')], default='House')
    location=StringField('Location', validators=[DataRequired()])
    #email = StringField('Email', validators=[DataRequired(),Email()])
    #subject = StringField('Subject', validators=[DataRequired()])
    image= FileField(u'Photo', validators=[DataRequired()])
