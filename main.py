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

import os
import webapp2
import jinja2

form="""
<form method="post">
    BLOG POSTS
    <br>
    <label>
        Content
        <input type="textarea" name="Content" value="%(content)s">
    </label>
    <div style="color: black">%(error)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""


def valid_content(content):
    if content != "":
        return True

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", content=""):
        self.response.write(form %{"error": error,
                                   "content": content})

    def get(self):
        #self.response.write("front.html")

    def post(self):
        user_content = self.request.get('content')

        content = valid_content(user_content)
        
        if not (content):
            self.write_form("Not a valid content!", user_content)
        else:
            self.response("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks! That's a valid content!")

app = webapp2.WSGIApplication([('/', MainHandler),
                              ('/thanks', ThanksHandler)],
                             debug=True)

