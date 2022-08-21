from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import website.algo
auth = Blueprint('auth', __name__)


@auth.route('/fastingbg', methods=['GET', 'POST'])
def login():
    basal_insulin = ""
    if request.method == 'POST':
        sugar = request.form.get('sugar')
        basal_insulin = request.form.get('basal-insulin')
        basal_insulin = website.algo.fasting_bg(basal_insulin=int(basal_insulin), blood_glucose=int(sugar))
        # user = User.query.filter_by(email=email).first()
        # if user:
        #     if check_password_hash(user.password, password):
        #         flash('Logged in successfully!', category='success')
        #         login_user(user, remember=True)
        #         return redirect(url_for('views.home'))
        #     else:
        #         flash('Incorrect password, try again.', category='error')
        # else:
        #     flash('Email does not exist.', category='error')

    return render_template("fastingbg.html", user=current_user, basal_insulin=basal_insulin)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/prandialbg', methods=['GET', 'POST'])
def sign_up():
    lunch_insulin = ""
    dinner_insulin = ""
    bedtime_insulin = ""
    if request.method == 'POST':
        sugar = request.form.get('lunch-sugar')
        insulin = request.form.get('lunch-insulin')
        if insulin != "" and sugar != "":
            lunch_insulin = website.algo.post_prandial_BG(prandial_insulin=int(insulin), blood_glucose=int(sugar), meal="lunch")
        
        sugar = request.form.get('dinner-sugar')
        insulin = request.form.get('dinner-insulin')
        print(insulin)
        if insulin != "" and sugar != "":
            dinner_insulin = website.algo.post_prandial_BG(prandial_insulin=int(insulin), blood_glucose=int(sugar), meal="dinner")
        
        sugar = request.form.get('bedtime-sugar')
        insulin = request.form.get('bedtime-insulin')
        if insulin != "" and sugar != "":
            bedtime_insulin = website.algo.post_prandial_BG(prandial_insulin=int(insulin), blood_glucose=int(sugar), meal="bedtime")
        

    return render_template("prandialbg.html", user=current_user, lunch_insulin=lunch_insulin, dinner_insulin=dinner_insulin, bedtime_insulin=bedtime_insulin)
