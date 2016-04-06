import flask
from flask import Flask, render_template
import flask.ext.login as flask_login

# dummy user information
users = { "user1":{'pw': 'password1'},
					"user2":{'pw': 'password2'}}

app = Flask(__name__)
app.secret_key = 'secretkey'
lm = flask_login.LoginManager()
lm.init_app(app)

class User(flask_login.UserMixin):
	pass

@lm.user_loader
def user_loader(username):
	if username not in users:
		return

	user = User()
	user.id = username
	return user

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about/')
def about():
  return render_template('about.html')

@app.route('/loggedin/')
@flask_login.login_required
def loggedin():
  return render_template('loggedin.html')

@app.route('/login/', methods=['GET','POST'])
def login():
  if flask.request.method == 'GET':
  	return render_template('login.html')

  username = flask.request.form['username']
  if flask.request.form['pw'] == users[username]['pw']:
  	user = User()
  	user.id = username
  	flask_login.login_user(user)
  	return flask.redirect(flask.url_for('loggedin'))

  return "Bad Login"

@app.route('/logout')
def logout():
  flask_login.logout_user()
  return flask.redirect(flask.url_for('home'))

if __name__ == '__main__':
  app.run(debug=True)

