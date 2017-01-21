from flask import Flask, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy  import *
from models import *
import flask_admin as admin
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose, form
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.routing import RequestRedirect, MethodNotAllowed, NotFound
from flask_admin.form.upload import ImageUploadField
from jinja2 import Markup


basedir = os.path.abspath(os.path.dirname(__file__))
img_stat_rel="kartoj"
img_rel='static/'+img_stat_rel
img_path = os.path.join(basedir, img_rel)

def karto_prev(view, context, model, name):
	if not model.bildo or not model.bildo.loko:
		return ''

	kart='<div class="karto">'

	if model.supra_top != "":
		kart+='<p class="supra_top">%s</p>' % model.supra_top
	if model.supra != "":
		kart+='<p class="supra">%s</p>' % model.supra
	if model.supra_sub != "":
		kart+='<p class="supra_sub">%s</p>' % model.supra_sub 
	if model.bildo != "":
		kart+='<img class="bildo img-responsive" src="%s">' % url_for('static',filename=img_stat_rel+"/"+form.thumbgen_filename(model.bildo.loko))
	if model.klarigo_ega_teksto != "":
		kart+='<p class="klarigo_ega_teksto">%s</p>' % model.klarigo_ega_teksto
	if model.klarigo_eta_teksto != "":
		kart+='<p class="klarigo_eta_teksto">%s</p>' % model.klarigo_eta_teksto
	if model.piedo_dekstra != "":
		kart+='<p class="piedo_dekstra">%s</p>' % model.piedo_dekstra
	if model.piedo_maldekstra  != "":
		kart+='<p class="piedo_maldekstra">%s</p>' % model.piedo_maldekstra 
	kart+='</div>'

	return Markup(kart)

class KartoView(ModelView):
    #edit_template = 'microblog_edit.html'
    create_template = 'create_preview.html'

class BildoView(ModelView):
    def _list_thumbnail(view, context, model, name):
        if not model.loko:
            return ''

        return Markup('<img src="%s">' %
            url_for('static',filename=img_stat_rel+"/"+form.thumbgen_filename(model.loko)))

    column_formatters = {'loko': _list_thumbnail}

    form_extra_fields = {
        'loko': form.ImageUploadField('Bildo', base_path=img_path, thumbnail_size=(150, 150, True))
    }

class KartoView(ModelView):
    column_formatters = {'bildo': karto_prev}

app = Flask(__name__)

admin = Admin(app, name='munĉkinilo', template_mode='bootstrap3')
app.config['SECRET_KEY'] = '123456790'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///visualalchemist.db"
# Add administrative views here
db = SQLAlchemy(app)

# Flask views
@app.route('/')
def index():
    return render_template('index.html')

admin.add_view(ModelView(Kartaro, db.session))
admin.add_view(KartoView(Karto, db.session))#ModelView(Karto, db.session))
admin.add_view(BildoView(Bildo, db.session))
app.run()

