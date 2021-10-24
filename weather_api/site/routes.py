from flask import Blueprint, render_template
from flask_login import login_required

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

# def login_ckeck():
#     def profile():
#         return render_template('profile.html')
#     if current_user.is_authenticated:
#         return profile()
#     else:
#         return 'Please log in to do that'