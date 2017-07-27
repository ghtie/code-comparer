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
import json
import logging
from google.appengine.ext import ndb

sys.path.append('source/')
#Import source code
import tableitem
from tableitem import TableItem


env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        desc_list = []
        #Querying entities from datastore into language-separated lists
        java_data = TableItem.query(TableItem.language == 'Java').order(TableItem.category, TableItem.description)
        java_list = []
        javascript_data = TableItem.query(TableItem.language == 'Javascript').order(TableItem.category, TableItem.description)
        javascript_list = []
        python_data = TableItem.query(TableItem.language == 'Python').order(TableItem.category, TableItem.description)
        python_list = []

        java_ex_list = []
        javascript_ex_list = []
        python_ex_list = []


        queryToListDesc(python_data, desc_list)

        queryToList(java_data, java_list)
        queryToList(javascript_data, javascript_list)
        queryToList(python_data, python_list)

        queryToListExample(java_data, java_ex_list)
        queryToListExample(javascript_data, javascript_ex_list)
        queryToListExample(python_data, python_ex_list)




        template_vars = {
            'desc_items': desc_list,

            'java_items': java_list,                     #{{ java_items }} in the html
            'javascript_items': javascript_list,
            'python_items': python_list,

            'j_examples': java_ex_list,
            'js_examples': javascript_ex_list,
            'p_examples': python_ex_list
        }

        template = env.get_template('templates/index.html')
        self.response.out.write(template.render(template_vars))


#Only to construct entities in datastore
class AdminHandler(webapp2.RequestHandler):
    def get(self):
        ndb.delete_multi([m.key for m in TableItem.query()])
        tableitem.constructAll()
        self.response.out.write('Success')



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/admin', AdminHandler)
], debug=True)




#Helper Functions
def queryToList(query_data, query_list):
    for item in query_data:
        query_list.append(item.syntax)

def queryToListDesc(query_data, query_list):
    for item in query_data:
        query_list.append(item.description)

def queryToListExample(query_data, query_list):
    for item in query_data:
        query_list.append(item.example)
