import colorsys
from distutils.command.upload import upload
from email.mime import audio
from multiprocessing.sharedctypes import Value
import re
from flask import Flask, request, url_for, redirect, render_template, jsonify, flash, session
import random
import sql_code
import os, math
import smtplib
import datetime
import stutter
from werkzeug.utils import secure_filename
from matplotlib.figure import Figure
import base64
from io import BytesIO
import datetime
from nltk.corpus import wordnet
import itertools
import nltk
nltk.download('omw-1.4')

####################################################################################################################################
AUDIO_STORE = 'temp/'
PEOPLE_FOLDER = os.path.join('static', 'images')
styles = os.path.join('static', 'styles')
app = Flask(__name__)

app.jinja_env.filters['zip'] = zip
app.config['UPLOAD_FOLDER'] = 'static/'
app.secret_key = "any rom swegwhgtring"
secur_id = 'vkrnpzrnmsrgfhya'
app.permanent_session_lifetime = datetime.timedelta(days=365)
app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


####################################################################################################################################

@app.route('/')
def index():
    session['loggedin'] = False
    return render_template("home.html", user_image='static/images/logo1.jpg')


######################################################################################################################################

@app.route('/home_page')
def home_page():
    return render_template("main_page.html", user_image='static/images/logo1.jpg')


@app.route('/main_page')
def main_page():
    if True:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("main_functionalities.html", user_image='static/images/logo2.png', settings_image=settings_image)
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################

@app.route('/signup')
def signup():
    # Session["font_size"] = request.form['']
    return render_template("signup.html", user_image='/static/images/logo2.png')


#####################################################################################################################################

@app.route('/signin')
def signin():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################
@app.route('/deleteAcount', methods=['GET', 'POST'])
def delete_account():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'

    print("indeleteacout")
    print(session)
    email = session['email']
    ddeellttee = sql_code.delete_user(email)
    print("try deleting")
    print(ddeellttee)
    flash("account deleted successfully")
    return render_template('signin.html', user_image=full_filename, settings_image=settings_image)



@app.route('/updateinfo', methods=['GET', 'POST'])
def updateinfo():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if request.form.get("Cancel"):
        return render_template('main_functionalities.html', user_image=full_filename)
    elif request.method == 'POST':
        email = request.form['email']
        psw = request.form['psw']
        f_name = request.form['first_name']
        l_name = request.form['last_name']
        rep_pass = request.form['psw-repeat']

        if psw != rep_pass:
            error = "password and repeat password mismatch"
            return render_template('updateinfo.html', error=error, user_image=full_filename,settings_image=settings_image)
        else:
            result = sql_code.update_info(f_name, l_name, email, psw)
            if result == 1:
                flash('Your information updated successfully')
                return render_template('main_functionalities.html', user_image=full_filename, settings_image=settings_image)
            else:
                error = "some thing went wrong"
                return render_template('updateinfo.html', error=error, user_image=full_filename,  settings_image=settings_image)
    return render_template("updateinfo.html", user_image=full_filename, settings_image=settings_image)
    # if session['loggedin']:
    #     full_filename = 'static/images/logo2.png'
    #     return render_template("updateinfo.html", user_image=full_filename)
    # else:
    #     full_filename = 'static/images/logo2.png'
    #     settings_image = 'static/images/settings.png'
    #     return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################

@app.route('/insert_signup', methods=['POST'])
def insert_signup():
    full_filename = 'static/images/logo2.png'
    if request.form.get("Cancel"):
        return render_template('main_page.html', user_image=full_filename)
    elif request.form.get("signup"):
        error = ''
        if (request.form['first_name'] == '' or request.form['last_name'] == '' or request.form['email'] == '' or
                request.form['psw'] == '' or request.form['psw-repeat'] == ''):
            error = "you must insert to all inputs"
        else:
            firstname = request.form['first_name']
            Lastname = request.form['last_name']
            email = request.form['email']
            psw = request.form['psw']
            repsw = request.form['psw-repeat']

            if (psw == repsw):
                sql_code.insertuser(firstname, Lastname, email, psw)
                flash("you are successfully registered")
                return render_template('walkthrough.html', user_image=full_filename)
            else:
                error = "Passowrd and re-passowrd are diffrent"

        return render_template('signup.html', error=error, user_image=full_filename)


#####################################################################################################################################

@app.route('/display_walkthrough')
def display_walkthrough():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template('walkthrough_in.html', user_image=full_filename, settings_image=settings_image)



@app.route('/alert')
def alert():
    full_filename = 'static/images/logo2.png'
    return render_template("alert.html", user_image=full_filename)


#####################################################################################################################################

@app.route('/insert_signin', methods=['POST'])
def insert_signin():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if request.form.get("Cancel"):
        return render_template('main_page.html', user_image=full_filename)
    elif request.form.get("SignIn"):
        email = request.form['email']
        psw = request.form['psw']
        result = sql_code.signin(email, psw)
        if (result == 1):
            user_data = sql_code.get_userdata(email, psw)
            session['id'] = user_data[0]
            session['email'] = email
            session['loggedin'] = True
            print(session)
            flash(u'logged in successfully')
            return render_template('main_functionalities.html', user_image=full_filename, settings_image=settings_image)
        else:
            error = "Invalid data, your email or password is wrong"
            return render_template('signin.html', user_image=full_filename, error=error, settings_image=settings_image)


#####################################################################################################################################

@app.route('/sign_up_in', methods=['POST'])
def sign_up_in():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    font_size = request.form['font_size']
    session['font_size'] = font_size
    if request.form.get("signup"):
        return render_template('signup.html', user_image=full_filename)
    elif request.form.get("signin"):
        return render_template('signin.html', user_image=full_filename, settings_image=settings_image)


@app.route('/not_sign_up_in', methods=['POST'])
def not_sign_up_in():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    font_size = request.form['font_size']
    session['font_size'] = font_size

    return render_template('main_functionalities.html', user_image=full_filename, settings_image=settings_image)

@app.route('/font_size', methods=['GET'])
def reinsert_font_size():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template('font_size.html', user_image=full_filename, settings_image=settings_image)

#####################################################################################################################################

@app.route('/forget_password')
def forget_password():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template('forget_password.html', user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################

@app.route('/before_presentaion', methods=['POST'])
def before_presentaion():
    if True:
        # print (session)
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        if request.form.get("before"):
            return render_template('before_presentation.html', user_image=full_filename, settings_image=settings_image)
        elif request.form.get("live"):
            return render_template('live.html', user_image=full_filename, settings_image=settings_image)
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################

@app.route('/Upload', methods=['GET', 'POST'])
def Upload():
    if True:
        settings_image = 'static/images/settings.png'
        arg1 = request.args.get("Upload", default=None, type=None)
        arg2 = request.args.get("Record", default=None, type=None)
        type = ""
        print("args")
        if arg1:
            print(arg1)
            type = "before_upload_audio"
        elif arg2:
            print(arg2)
            type = "uploader"
        # if 'Record=Record' in rule.rule:
        #     type ="uploader"
        #
        # elif 'Upload=Upload' in rule.rule:
        #     type="before_upload_audio"
        return render_template('Upload.html', settings_image=settings_image, type=type)
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################
@app.route('/Upload_live', methods=['GET', 'POST'])
def Upload_live():
    if True:
        settings_image = 'static/images/settings.png'
        return render_template('Upload_live.html', settings_image=settings_image)
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################
@app.route('/uploader_live', methods=['GET', 'POST'])
def upload_file_live():
    print("boolean")
    print(session)
    if True:
        if request.method == 'POST':
            f = request.files['file']
            if f.filename.split('.')[1] == 'pdf':
                f.filename = 'q.pdf'
                f.save(f'static/pdfs/{f.filename}')
                return redirect(url_for('recorder_live'))
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#####################################################################################################################################

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    print("we are inside upload_file")
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if True:
        if request.method == 'POST':
            f = request.files['file']
            print(f.filename.split('.')[0])

            if f.filename.split('.')[1] == 'pdf':
                f.filename = 'q.pdf'
                f.save(f'static/pdfs/{f.filename}')
                return redirect(url_for('recorder'))
            else:
                error = "invalid data, upload pdf"
                return render_template("Upload.html", user_image=full_filename, settings_image=settings_image)
            # print(session)
            id = session['id']
            email = session['email']
            record_number = sql_code.get_record_number(id)[0]
            dt = datetime.datetime.now()
            ts = dt.strftime("%d-%m-%Y_%H:%M:%S")
            formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
            f.filename = f'{id}_{record_number}_{ts}.wav'
            audio_path = f'static\audio\{f.filename}'
            session['current_audio'] = audio_path
            f.save(audio_path)
            sql_code.insert_audio_data(id, audio_path, formatted_date)
            # return "<html>done</html>"
            return redirect(url_for('tomodel'))
    else:
        full_filename = 'static/images/logo2.png'
        settings_image = 'static/images/settings.png'
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################
@app.route('/tomodel', methods=['GET', 'POST'])
def tomodel():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if True:
        if request.method == 'POST' or 'GET':
            print(session)
            aud = session['current_audio']
            if aud:
                result, play_ts, score = stutter.main(aud)
                if len(result) == 0:
                    print('11')
                    minutes = ['no stutter', 'no stutter']
                    return render_template('timestamps.html', minutes=minutes, ts=play_ts, aud=aud, score =int(score))
                else:
                    print('22')
                    print(result)
                    print(play_ts)
                    print(score)
                    minutes = [divmod(x, 60) for x in result]
                    sql_code.insert_score(aud, score)
                    # session['current_audio']=''
                    return render_template(
                        'timestamps.html', minutes=minutes, ts=play_ts, aud=aud.replace('\\', '/'),
                        user_image=full_filename, settings_image=settings_image, score =int(score)
                    )
            else:
                return redirect(url_for('Upload'))
    else:
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)



@app.route('/before_upload_audio', methods=['GET', 'POST'])
def toModelFromBefore():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if True:
        if request.method == 'POST':
            f = request.files['file']
            print(f.filename.split('.')[0])
            print(session)
            if f.filename.split('.')[1] == 'wav':
                #f.filename = 'q.wav'
                f.save(f'./static/audio/{f.filename}')
                result, play_ts, score = stutter.main(f'./static/audio/{f.filename}')
                if len(result) == 0:
                    print('11')
                    minutes = ['no stutter', 'no stutter']
                    return render_template('timestamps.html', user_image=full_filename, settings_image=settings_image,
                         minutes=minutes, ts=play_ts, aud=f.filename, score=int(score))
                else:
                    print('22')
                    print(result)
                    print(play_ts)
                    print(score)
                    minutes = [divmod(x, 60) for x in result]
                    sql_code.insert_score(f.filename, score)
                    # session['current_audio']=''
                    return render_template(
                        'timestamps.html', minutes=minutes, ts=play_ts, aud=f'./static/audio/{f.filename}'.replace('\\', '/'),
                        user_image=full_filename, settings_image=settings_image, score =int(score)
                    )
            else:
                error = "invalid data, upload pdf"
                return render_template("Upload.html", user_image=full_filename, settings_image=settings_image)
        else:
           return redirect(url_for('Upload'))
    else:
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)

#######################################################################################################################################

@app.route("/recorder_live", methods=['POST', 'GET'])
def recorder_live():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if True:
        if request.method == "POST":
            f = request.files['audio_data']
            id = session['id']
            email = session['email']
            record_number = sql_code.get_record_number(id)[0]
            dt = datetime.datetime.now()
            ts = dt.strftime("%d-%m-%Y_%H:%M:%s")
            formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
            f.filename = f'{id}_{record_number}_{ts}.wav'
            audio_path = f'static/audio/{f.filename}'
            with open(audio_path, 'wb') as audio:
                f.save(audio)
            print('file uploaded successfully')
            sql_code.insert_audio_data(id, audio_path, formatted_date)
            session['current_audio'] = audio_path

            return render_template('recorder_live.html', request="POST", user_image=full_filename, settings_image=settings_image)
        else:
            return render_template("recorder_live.html", user_image=full_filename, settings_image=settings_image)
    else:
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################

@app.route("/recorder", methods=['POST', 'GET'])
def recorder():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    num = random.randint(1, 7)
    if True:
        if request.method == "POST":
            f_ = request.files['audio_data']
            id = session['id']
            email = session['email']
            record_number = sql_code.get_record_number(id)[0]
            dt = datetime.datetime.now()
            ts = dt.strftime("%d-%m-%Y_%H:%M:%S")
            formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
            f_.filename = f'{id}_{record_number}_{ts}.wav'
            # C:\folder1\folder2\file (windows)
            # /home/folder1/folder2/file
            # audio_path=f'static/audio/{f.filename}'
            audio_path = os.path.join('static', 'audio', f_.filename).replace(':', '_')
            # with open(audio_path, 'wb') as audio:
            f_.save(audio_path)
            print('file uploaded successfully')
            sql_code.insert_audio_data(id, audio_path, formatted_date)
            session['current_audio'] = audio_path

            return render_template('recorder.html', request="POST", user_image=full_filename, settings_image=settings_image, num=num)
        else:
            return render_template("recorder.html", user_image=full_filename, settings_image=settings_image, num=num)
    else:
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################################

@app.route("/plotgraph")
def plotgraph():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    if session['loggedin']:
        fig = Figure()
        ax = fig.subplots()
        id = session['id']
        c = sql_code.get_graph_data(id)
        if c:
            y, x = c
            print(x)
            print(y)
            # x=([1, 2,3,5,9,10])
            # y=([2,3,45,9,4,8])
            ax.bar(x, y)
            ax.axhline(0, color='grey', linewidth=0.8)
            ax.set_ylabel('stuttering rate', color='red')
            buf = BytesIO()
            fig.savefig(buf, format="png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            # return f"<img src='data:image/png;base64,{data}'/>"
            return render_template('graph.html', data=data, user_image=full_filename, settings_image=settings_image)
        else:
            return render_template('nograph.html', user_image=full_filename, settings_image=settings_image)
    else:
        return render_template("signin.html", user_image=full_filename, settings_image=settings_image)


#######################################################################################################################################

@app.route('/otpver', methods=['POST'])
def otpver():
    error = ''
    settings_image = 'static/images/settings.png'
    full_filename = 'static/images/logo2.png'
    if request.form.get("Cancel"):
        return render_template('signin.html', user_image=full_filename, settings_image=settings_image)
    elif request.form.get("Verfication"):
        if (request.form['email'] == ''):
            error = 'you must input email to verification'
        else:
            mail = request.form['email']

            digits = "0123456789"
            OTP = ""
            for i in range(6):
                OTP += digits[math.floor(random.random() * 10)]
            msg = 'Your OTP Verification for app is ' + OTP + ' Note..  Please enter otp within 2 minutes and 3 attempts, otherwise it becomes invalid'
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("pstapp2022@gmail.com", "odmvlckxuhtokmoj")
            s.sendmail('pstapp2022@gmail.com', mail, msg)
            s.close()
            f = open("OTP.txt", "w")
            f.write(OTP)
            f.close()

            return render_template('alert.html', email=mail, user_image=full_filename)

        return render_template('forget_password.html', user_image=full_filename, error=error)


#######################################################################################################################################

@app.route('/verfication', methods=['POST'])
def verfication():
    error = ''
    settings_image = 'static/images/settings.png'
    full_filename = 'static/images/logo2.png'
    if request.form.get("Cancel"):
        return render_template('signin.html', user_image=full_filename, settings_image=settings_image)
    elif request.form.get("update"):
        if (request.form['OTP'] == '' or request.form['psw'] == '' or request.form['repsw'] == ''):
            error = "you must insert to all inputs"
            return render_template('alert.html', error=error, user_image=full_filename)

        else:

            f = open('OTP.txt', 'r')
            otp = f.read()
            email = request.form['email']
            password = request.form['psw']
            repassword = request.form['repsw']

            if str(otp) == str(request.form['OTP']):
                if (password == repassword):
                    result = sql_code.update_password(email, password)
                    flash('Your password updated successfully')
                    return render_template('signin.html', user_image=full_filename, settings_image=settings_image)
                else:
                    error = 'error!. password and Retype Password didnt have same value'
                    return render_template('alert.html', error=error, email=email, user_image=full_filename)
            else:
                error = 'error!. OTP verification is not correct'
                return render_template('alert.html', error=error, email=email, user_image=full_filename)


########################################################################################


@app.route('/developer_contact')
def developer_connect():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template("developer_contact.html", user_image=full_filename, settings_image=settings_image)


@app.route('/synonyms', methods=["GET","POST"])
def synonyms():
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    my_text = ""
    return_value = ""
    if request.method == "POST":
        my_text =  request.form.get('my_text')
        if(my_text):
            
            synonyms = [] 
            for syn_set in wordnet.synsets(my_text): 
                for l in syn_set.lemmas(): 
                    synonyms.append(l.name())

        return_value = itertools.islice(set(synonyms), 5)


    return render_template("synonyms.html", my_text= my_text, return_value = return_value, user_image=full_filename, settings_image=settings_image)


@app.route('/signout')
def signout():
    print(session)
    # session.clear()
    session['loggedin'] = False
    full_filename = 'static/images/logo2.png'
    settings_image = 'static/images/settings.png'
    return render_template("main_page.html", user_image=full_filename, settings_image=settings_image)


########################################################################################
if __name__ == '__main__':
    app.debug = True
    app.run()
