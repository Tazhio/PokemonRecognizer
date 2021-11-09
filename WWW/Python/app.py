from flask import Flask
from flask import url_for, escape
from flask import request
from flask import render_template
from flask import redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory
import os
import sys
import run_command
from werkzeug.utils import secure_filename
import pypokedex

#special attention: flask的url转换是按照函数名字来命名的，不是按html，不过也合理，它才不管html呢。
app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % escape(name)

@app.route('/pokedex')
def pokedex():
    return render_template('/pokedex.html')


@app.route('/test')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('hello'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    return 'Test page'

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('404.html'), 404  # 返回模板和状态码

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result=run_command.get_pokemon_ID(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if result==-1:
                return render_template('somethingwrong.html')
            return render_template('pokemon-info.html', pokemonid=result, val="Initial Data")
            # return redirect(url_for('uploaded_file',
            #                         filename=filename))
    return render_template('uploads.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/references')
def references():
    return render_template('references.html')

@app.route('/new1')
def news1():
    return render_template('news1.html')

@app.route('/new2')
def news2():
    return render_template('news2.html')

@app.route('/new3')
def news3():
    return render_template('news3.html')
@app.route('/new4')
def news4():
    return render_template('news4.html')
@app.route('/new5')
def news5():
    return render_template('news5.html')

@app.route('/new6')
def news6():
    return render_template('news6.html')