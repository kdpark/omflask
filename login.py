import flask, flask.views

# Dictionary of username and password
users = {'jrimchala':'bacon', 
        'redstar':'redstar123'};

class Login(flask.views.MethodView):
    def get(self):
        return flask.render_template('signin.html')
    
    def post(self):
    	# Check if user need to log out
    	if 'logout' in flask.request.form:
    		# Pop user out of session
    		flask.session.pop('usr', None)
    		return flask.redirect(flask.url_for('login'))

    	required = ['usr','pswd']
    	for r in required:
    		if r not in flask.request.form:
    			flask.flash("Error: {0} is required.".format(r))
    			return flask.redirect(flask.url_for('login'))
    	# Receive usr, pwd input
    	usr = flask.request.form['usr']
    	pswd = flask.request.form['pswd']
    	# Check that usr and pwd exist in dictionary
    	if usr in users and users[usr] == pswd:
    		# Accept user
    		flask.session['usr'] = usr
    	else:
    		flask.flash("Username does not exist or incorrect password")
    	# Return to login page
    	return flask.redirect(flask.url_for('login'))

class Logout(flask.views.MethodView):
    def get(self):
        flask.session.pop('usr', None)
        return flask.redirect(flask.url_for('login'))

class Signup(flask.views.MethodView):
    def get(self):
        return flask.render_template('signup.html')


# class Welcome(flask.views.MethodView):
#     def get(self):
#         return flask.render_template('welcome.html')
    
#     def post(self):
#         # Check if user need to log out
#         if 'logout' in flask.request.form:
#             # Pop user out of session
#             flask.session.pop('usr', None)
#             return flask.redirect(flask.url_for('login'))

#         required = ['usr','pswd']
#         for r in required:
#             if r not in flask.request.form:
#                 flask.flash("Error: {0} is required.".format(r))
#                 return flask.redirect(flask.url_for('login'))
#         # Receive usr, pwd input
#         usr = flask.request.form['usr']
#         pswd = flask.request.form['pswd']
#         # Check that usr and pwd exist in dictionary
#         if usr in users and users[usr] == pswd:
#             # Accept user
#             flask.session['usr'] = usr
#         else:
#             flask.flash("Username does not exist or incorrect password")
#         # Return to login page
#         return flask.redirect(flask.url_for('login'))