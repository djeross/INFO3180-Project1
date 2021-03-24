"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app,db
from flask import render_template, request, redirect, url_for, send_from_directory,flash
from .forms import PropertyForm
from werkzeug.utils import secure_filename
from app.models import MyProperty


def allowed_file(filename):
    parts=filename.split('.')
    return parts[1].lower() in app.config['VALID_EXTENSIONS']

def get_uploaded_images():
    images=[]
    rootdir = os.getcwd()
    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            images.append( file)
    return images


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/property',methods=['GET', 'POST'])
def property():
    pform=PropertyForm()
    if request.method == 'POST':
        if (allowed_file(secure_filename(pform.image.data.filename))):
            if pform.validate_on_submit():
                title=pform.title.data
                desc=pform.description.data
                num_rooms=pform.rooms.data
                num_bath=pform.bathrooms.data
                price=pform.price.data
                buildtype=pform.ptype.data
                location=pform.location.data
                img=pform.image.data
                #save data for retrieval
                imagename = secure_filename(img.filename)
                newproperty= MyProperty(title,desc,num_rooms,num_bath,price,buildtype,location,imagename)
                db.session.add(newproperty)
                db.session.commit()
                img.save(os.path.join(app.config['UPLOAD_FOLDER'], imagename))
                flash('Property Successfully Added', 'success')
                return redirect(url_for("properties"))
            else:
                flash_errors(pform)
        else:
            flash('File must be of type JPEG or PNG', 'danger')
    return render_template('property.html',form=pform)

@app.route('/properties')
def properties():
    allproperties=MyProperty.query.with_entities(MyProperty.id,MyProperty.filename,MyProperty.title,MyProperty.location,MyProperty.price).all()
    return render_template('properties.html',allproperties=allproperties)

@app.route('/property/<propertyid>')
def individualProperty(propertyid):
    dlist=[]
    details= MyProperty.query.filter_by(id=propertyid).first()
    dlist.append(details.title)
    dlist.append(details.description)
    dlist.append(details.rooms+" Bedrooms")
    dlist.append(details.bathrooms+" Bathrooms")
    dlist.append("$"+details.price)
    dlist.append(details.ptype)
    dlist.append(details.location)
    dlist.append(details.filename) 
    return render_template('details.html',details=dlist)

@app.route('/uploads/<filename>')
def get_image(filename):
    root_dir = os.getcwd()
    return send_from_directory(os.path.join(root_dir,app.config['UPLOAD_FOLDER']),filename)
    

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
