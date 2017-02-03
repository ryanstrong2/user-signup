#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import cgi
import re

form = """
<form method = "post" >

    <label>
        Username
        <input name="username" value="%(username)s">
    </label>
    <br>
    <label>
        Password
        <input type="password" name="password">
    </label>
    <br>
    <label>
        Verfiy password
        <input type="password" name="verify">
    </label>
    <br>
    <label>
        E-mail (optional)
        <input type ="email" name="email" value="%(email)s">
    </label>
    <br>
    <div style ="color: red">%(error)s</div>
    <br>
    <input type="submit" value="Submit">
</form>
"""
# username = "^[a-zA-Z0-9_-]{3,20}$"
# password= "^.{3,20}$"
# email= "^[\S]+@[\S]+.[\S]+$"
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    if email== "":
        return True
    else:
        return EMAIL_RE.match(email)
# class BaseHandler(webapp2.RequestHandler):
#     def render(self, template, **kw):
#         self.response.out.write(render_str(template, **kw))
#     def write (self, *a , **kw):
        # self.response.out.write(*a, **kw)
class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", username="", password="", verify="", email=""):
        self.response.out.write(form % {
                                        "error" : error,
                                        "username" : cgi.escape(username),
                                        "password" : cgi.escape(password),
                                        "verify" : cgi.escape(verify),
                                        "email" : cgi.escape(email)
                                        })
    def get(self):
        self.write_form()
# day off 2-23-17
    def post(self):
        username  = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')
# login.info
        user_username = valid_username(username)
        user_password = valid_password(password)
        user_verify = valid_password(verify)
        user_email = valid_email(email)
        if not valid_username(username):
            # username = valid_username(username)
            error =  self.request.get('error')
            self.write_form("Not a valid username.",
                            username, password, verify, email)
        elif not password:
            self.write_form("Invalid password", username, password, verify, email)

        elif password != verify:
            self.write_form("Passwords do not match", username, password, verify , email)
        elif valid_email('email'):
            self.write_form("Invalid email", username, password, verify, email)
        else:
            self.redirect("/thanks?email="+email + "&username=" + username)

welcome = """
    <h2> Welcome, <div>%(m)s</div></h2>"""
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        use = self.request.get('username')
        content = "<p> Welcome, "+ use + "</p>"
        self.response.out.write(content)
# class FormHandler(webapp2.RequestHandler):
#     def get(self):
#
#         self.response.out.write("write_form")
        #self.render("signup-form.html")
    # def post(self):
    #     have_error = False
    #     username = self.request.get('username')
    #     user_password = self.request.get('password')
    #     user_verify = self.request.get('verify')
    #     user_email = self.request.get('email')
# class Welcome(BaseHandler):
#     def get(self):
#         user = self.request.get ('username')
#         if valid_username(username):
#             self.render('welcome.html', username= username)
#         else:
#             self.redirect('/unit2/signup')
app = webapp2.WSGIApplication([
    ('/', MainHandler), ('/thanks', WelcomeHandler)
], debug=True)

#
# The form elements where the user inputs their username, password, password
# again, and email address must be named "username", "password", "verify", and "email", respectively.
# The form method must be POST, not GET.
# Upon invalid user input, your web app should re-render the form for the user.
# Upon valid user input, your web app should redirect to a welcome page for the user.
#
#     This page must include both "Welcome" and the user's username.
# database is
