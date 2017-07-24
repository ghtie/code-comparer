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
import jinja2
import os
import webapp2
import sys

sys.path.append('source/')
#import source code
import tableitem
from tableitem import TableItem


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Construct All
        #tableitem.constructAll()

        java_data = TableItem.query(TableItem.language == 'Java').fetch(limit=100)
        java_list = ""
        for item in java_data:
            java_list += (item.find + '\t')
            
        template_vars = {
        'java_items': java_list         #{{ java_items }} in the html
        }


        template = env.get_template('templates/index.html')
        self.response.out.write(template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
