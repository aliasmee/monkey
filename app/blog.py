from flask import Flask, url_for,render_template,request,redirect,url_for,session
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone,User.password == password).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '您输入的手机号或密码不正确，请检查确认后再提交！'

@app.route('/register/', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return '该用户或手机号已经存在，请更换手机号码/重新提交！'
        else:
            if password != password1:
                return '两次输入的密码不一样，请确认后重新提交。'
            else:
                user = User(telephone=telephone, username=username, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/question')
def question()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
