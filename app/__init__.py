import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '813325e329ada54fd27a3c1248a14529'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
bstr = Bootstrap5(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '96a011ee0096bf'
app.config['MAIL_PASSWORD'] = '113b1ed9f10732'
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USERNAME'] = 'johngrant685@gmail.com'
# app.config['MAIL_PASSWORD'] = 'bmnuwpwykxoytdwv'
# app.config['MAIL_DEFAULT_SENDER'] = 'noreply@gmail.com'
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_MAX_EMAILS'] = None

mail = Mail(app)


from app import routes
