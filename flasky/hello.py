from flask import Flask,url_for,request,render_template,redirect
from test_mongo import collection

# import os


app = Flask(
            __name__,
            #  static_url_path='/different',
            # static_folder='C:/Users/Admin/Pictures'
            )

# os.environ['DEBUG'] = 'True'

@app.route("/")
def index():
    return '<h1>Hello, 1World!</h1>'

@app.route("/user/<name>")
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/image')

def image():
    return '<image src="/static/a.png">'

@app.route('/image1')

def image1():
    return '<image src="/different/a.PNG">' #cau hinh

# def image1():
#     url = url_for('static', filename='a.png')
#     return '<img src="{url}">'

# C:/Users/Admin/Pictures

def do_the_login():
    return '<h1>method POST</h1>'
def show_the_login_form():
    return '<h1>method GET</h1>'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


# @app.route('/')
# def home():
#     return '<h1>this home page</h1>'
# def index():
#     return '<h1>Hello, World!</h1>'
# @app.route("/")
# def home():
#     with app.app_context():
#         url = url_for('abc')
#         return render_template("static\\b.html", url=url)
    
   # return '<h1>this home page</h1>' flasky\static\b.html


@app.route("/welcome/<facon>")
def welcome(facon):
    return render_template("b.html", fav=facon)

@app.route('/cricket/<favteam>') 
def cricket(favteam): 
    return render_template('b.html',fav = favteam) 
  

@app.route('/sport/<name>/<team>') 
def game(name,team): 
    if name == 'cricket': 
        return redirect(url_for('cricket',favteam = team)) 
    



@app.route('/mne')
def mne():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

# {% macro render_comment(comment) %}
#     <li>{{ comment }}</li>
# {% endmacro %}
# <ul>
#     {% for comment in comments %}
#         {{ render_comment(comment) }}
#     {% endfor %}
# </ul>


app.config['DEBUG'] = True
if __name__ == "__main__":
    app.run(debug=True)