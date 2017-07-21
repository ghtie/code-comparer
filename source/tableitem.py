from google.appengine.ext import ndb

class TableItem(ndb.Model):
    syntax = ndb.StringProperty()
    language = ndb.StringProperty()
    category = ndb.StringProperty()




def construct(syntax1, language1, category1):
    return TableItem(syntax=syntax1,
                    language=language1,
                    category = category1)
