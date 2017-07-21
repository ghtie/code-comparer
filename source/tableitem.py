from google.appengine.ext import ndb

class TableItem(ndb.Model):
    syntax = ndb.StringProperty()
    language = ndb.StringProperty()
    category = ndb.StringProperty()
    find = ndb.StringProperty()




def construct(syntax1, language1, category1, find1):
    return TableItem(syntax = syntax1,
                    language = language1,
                    category = category1,
                    find = find1)

def constructAll():
    #Boilerplate Code
    construct('class Main {\npublic static void main(String[] args) { ... \n}\n}', 'Java', 'Boilerplate Code', 'j_boilerplate').put()
    construct('n/a', 'Javascript', 'Boilerplate Code', 'js_boilerplate').put()
    construct('n/a', 'Python', 'Boilerplate Code', 'p_boilerplate').put()
    #Commenting
    construct('//\t/* ... */', 'Java', 'Commenting', 'j_comment').put()
    construct('//\t/* ... */', 'Javascript', 'Commenting', 'js_comment').put()
    construct('#', 'Python', 'Commenting', 'p_comment').put()
    #Function Definition
    construct('public returnType myFunc(type param1, type param2) { ... }', 'Java', 'Function Definition', 'j_deffunc').put()
    construct('function myFunc(param1, param2) { ... }', 'Javascript', 'Function Definition', 'js_deffunc').put()
    construct('def myFunc(param1, param2):\n\t ... ', 'Python', 'Function Definition', 'p_deffunc').put()
    #Class Definition
    construct('class MyClass{ ... }', 'Java', 'Class Definition', 'j_defclass').put()
    construct('function MyClass (type) {\nthis.type = type; ... }', 'Javascript', 'Class Definition', 'js_defclass').put()
    construct('class MyClass:\n\t ... ', 'Python', 'Class Definition', 'p_defclass').put()
    #Constructor Definition
    construct('public MyClass(type param1, type param2) { ... }', 'Java', 'Constructor Definition', 'j_defconstruct').put()
    construct('same as class definition (see js_defclass)', 'Javascript', 'Constructor Definition', 'js_defconstruct').put()
    construct('\t__init__(self):\n\t ... ', 'Python', 'Constructor Definition', 'p_defconstruct').put()
    #Constructor Call
    construct('new MyClass();', 'Java', 'Constructor Call', 'j_callconstruct').put()
    construct('new MyClass();', 'Javascript', 'Constructor Call', 'js_callconstruct').put()
    construct('MyClass()', 'Python', 'Constructor Call', 'p_callconstruct').put()

    #Arithmetic Operators - Addition
    construct('+', 'Java', 'Arithmetic Operators', 'j_add').put()
    construct('+', 'Javascript', 'Arithmetic Operators', 'js_add').put()
    construct('+', 'Python', 'Arithmetic Operators', 'p_add').put()
    #Arithmetic Operators - Subtraction
    construct('-', 'Java', 'Arithmetic Operators', 'j_subtract').put()
    construct('-', 'Javascript', 'Arithmetic Operators', 'js_subtract').put()
    construct('-', 'Python', 'Arithmetic Operators', 'p_subtract').put()
    #Arithmetic Operators - Multiplication
    construct('*', 'Java', 'Arithmetic Operators', 'j_multiply').put()
    construct('*', 'Javascript', 'Arithmetic Operators', 'js_multiply').put()
    construct('*', 'Python', 'Arithmetic Operators', 'p_multiply').put()
    #Arithmetic Operators - Division
    construct('/', 'Java', 'Arithmetic Operators', 'j_divide').put()
    construct('/', 'Javascript', 'Arithmetic Operators', 'js_divide').put()
    construct('/', 'Python', 'Arithmetic Operators', 'p_divide').put()
    #Arithmetic Operators - Modulus/Remainder
    construct('%', 'Java', 'Arithmetic Operators', 'j_modulo').put()
    construct('%', 'Javascript', 'Arithmetic Operators', 'js_modulo').put()
    construct('%', 'Python', 'Arithmetic Operators', 'p_modulo').put()
    #Arithmetic Operators - Addition
    construct('+', 'Java', 'Arithmetic Operators', 'j_add').put()
    construct('+', 'Javascript', 'Arithmetic Operators', 'js_add').put()
    construct('+', 'Python', 'Arithmetic Operators', 'p_add').put()

    #Comparison/Relational Operators - Equal
    construct('==\t.equals()', 'Java', 'Comparison/Relational Operators', 'j_equal').put()
    construct('==\t===', 'Javascript', 'Comparison/Relational Operators', 'js_equal').put()
    construct('==', 'Python', 'Comparison/Relational Operators', 'p_equal').put()
    #Comparison/Relational Operators - Not Equal
    construct('!=', 'Java', 'Comparison/Relational Operators', 'j_notequal').put()
    construct('!=\t!==', 'Javascript', 'Comparison/Relational Operators', 'js_notequal').put()
    construct('!=', 'Python', 'Comparison/Relational Operators', 'p_notequal').put()
    #Comparison/Relational Operators - Less Than
    construct('<', 'Java', 'Comparison/Relational Operators', 'j_lessthan').put()
    construct('<', 'Javascript', 'Comparison/Relational Operators', 'js_lessthan').put()
    construct('<', 'Python', 'Comparison/Relational Operators', 'p_lessthan').put()
    #Comparison/Relational Operators - Greather Than
    construct('>', 'Java', 'Comparison/Relational Operators', 'j_greaterthan').put()
    construct('>', 'Javascript', 'Comparison/Relational Operators', 'js_greaterthan').put()
    construct('>', 'Python', 'Comparison/Relational Operators', 'p_greaterthan').put()
    #Comparison/Relational Operators - Less Than or Equal To
    construct('<=', 'Java', 'Comparison/Relational Operators', 'j_lessthanequal').put()
    construct('<=', 'Javascript', 'Comparison/Relational Operators', 'js_lessthanequal').put()
    construct('<=', 'Python', 'Comparison/Relational Operators', 'p_lessthanequal').put()
    #Comparison/Relational Operators - Greater Than or Equal To
    construct('>=', 'Java', 'Comparison/Relational Operators', 'j_greaterthanequal').put()
    construct('>=', 'Javascript', 'Comparison/Relational Operators', 'js_greaterthanequal').put()
    construct('>=', 'Python', 'Comparison/Relational Operators', 'p_greaterthanequal').put()

    #Logical Operators - And
    construct('&&', 'Java', 'Logical Operators', 'j_').put()
    construct('&&', 'Javascript', 'Logical Operators', 'js_').put()
    construct('and', 'Python', 'Logical Operators', 'p_').put()
    #Logical Operators - Or
    construct('||', 'Java', 'Logical Operators', 'j_').put()
    construct('||', 'Javascript', 'Logical Operators', 'js_').put()
    construct('or', 'Python', 'Logical Operators', 'p_').put()
    #Logical Operators - Not
    construct('!', 'Java', 'Logical Operators', 'j_').put()
    construct('!', 'Javascript', 'Logical Operators', 'js_').put()
    construct('not', 'Python', 'Logical Operators', 'p_').put()
