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

# The form elements where the user inputs their username, password, password again, and email address must be named "username", "password", "verify", and "email", respectively.
# The form method must be POST, not GET.
# Upon invalid user input, your web app should re-render the form for the user.
# Upon valid user input, your web app should redirect to a welcome page for the user.
#
#     This page must include both "Welcome" and the user's username.
#

import webapp2
import cgi
import re

class MainHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write('Welcome', username)
    if not (username and password and verify):
        self.form("Not a valid username.")
    else:
        self.redirect('/welcome')


    Username: "^[a-zA-Z0-9_-]{3,20}$"
    Password: "^.{3,20}$"
    Email: "^[\S]+@[\S]+.[\S]+$"

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    retrun USER_RE.match(username)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
