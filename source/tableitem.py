from google.appengine.ext import ndb

class TableItem(ndb.Model):
    syntax = ndb.StringProperty()
    language = ndb.StringProperty()
    category = ndb.StringProperty()
    find = ndb.StringProperty()
    description = ndb.StringProperty()




def construct(syntax1, language1, category1, find1, description1):
    return TableItem(syntax = syntax1,
                    language = language1,
                    category = category1,
                    find = find1,
                    description = description1)

def constructAll():
    #Boilerplate Code
    construct('class Main {\npublic static void main(String[] args) { ... \n}\n}', 'Java', 'Basics', 'j_boilerplate', 'Boilerplate Code').put()
    construct('n/a', 'Javascript', 'Basics', 'js_boilerplate', 'Boilerplate Code').put()
    construct('n/a', 'Python', 'Basics', 'p_boilerplate', 'Boilerplate Code').put()
    #Commenting
    construct('//\t/* ... */', 'Java', 'Basics', 'j_comment', 'Commenting').put()
    construct('//\t/* ... */', 'Javascript', 'Basics', 'js_comment', 'Commenting').put()
    construct('#', 'Python', 'Basics', 'p_comment', 'Commenting').put()
    #Line Wrapping
    construct(';','Java', 'Basics', 'j_linewrap', 'Line Wrapping').put()
    construct(';','Javascript', 'Basics','js_linewrap', 'Line Wrapping').put()
    construct('\n','Python', 'Basics','p_linewrap', 'Line Wrapping').put()
    #Grouping Expressions
    construct('{ ... }','Java', 'Basics', 'j_group', 'Grouping Expressions').put()
    construct('{ ... }','Javascript', 'Basics','js_group', 'Grouping Expressions').put()
    construct('\t','Python', 'Basics','p_group', 'Grouping Expressions').put()

    #Function Definition
    construct('public returnType myFunc(type param1, type param2, ...) { ... }', 'Java', 'Functions', 'j_deffunc', 'Function Definition').put()
    construct('function myFunc(param1, param2, ...) { ... }', 'Javascript', 'Functions', 'js_deffunc', 'Function Definition').put()
    construct('def myFunc(param1, param2, ...):\n\t ... ', 'Python', 'Functions', 'p_deffunc', 'Function Definition').put()
    #Function Call
    construct('myFunc(param1, param2, ...)', 'Java', 'Functions', 'j_callfunc', 'Function Call').put()
    construct('myFunc(param1, param2, ...)', 'Javascript', 'Functions', 'js_callfunc', 'Function Call').put()
    construct('myFunc(param1, param2, ...)', 'Python', 'Functions', 'p_callfunc', 'Function Call').put()

    #Class Definition
    construct('class MyClass{ ... }', 'Java', 'Object-Oriented Programming', 'j_defclass', 'Class Definition').put()
    construct('function MyClass (type) {\nthis.type = type; ... }', 'Javascript', 'Object-Oriented Programming', 'js_defclass', 'Class Definition').put()
    construct('class MyClass:\n\t ... ', 'Python', 'Object-Oriented Programming', 'p_defclass', 'Class Definition').put()
    #Constructor Definition
    construct('public MyClass(type param1, type param2...) { ... }', 'Java', 'Object-Oriented Programming', 'j_defconstruct', 'Constructor Definition').put()
    construct('same as class definition (see js_defclass)', 'Javascript', 'Object-Oriented Programming', 'js_defconstruct', 'Constructor Definition').put()
    construct('\t__init__(self):\n\t ... ', 'Python', 'Object-Oriented Programming', 'p_defconstruct', 'Constructor Definition').put()
    #Constructor Call
    construct('new MyClass()', 'Java', 'Object-Oriented Programming', 'j_callconstruct', 'Constructor Call').put()
    construct('new MyClass()', 'Javascript', 'Object-Oriented Programming', 'js_callconstruct', 'Constructor Call').put()
    construct('MyClass()', 'Python', 'Object-Oriented Programming', 'p_callconstruct', 'Constructor Call').put()

    #Arithmetic Operators - Addition
    construct('+', 'Java', 'Arithmetic Operators', 'j_add', 'Addition').put()
    construct('+', 'Javascript', 'Arithmetic Operators', 'js_add', 'Addition').put()
    construct('+', 'Python', 'Arithmetic Operators', 'p_add', 'Addition').put()
    #Arithmetic Operators - Subtraction
    construct('-', 'Java', 'Arithmetic Operators', 'j_subtract', 'Subtraction').put()
    construct('-', 'Javascript', 'Arithmetic Operators', 'js_subtract', 'Subtraction').put()
    construct('-', 'Python', 'Arithmetic Operators', 'p_subtract', 'Subtraction').put()
    #Arithmetic Operators - Multiplication
    construct('*', 'Java', 'Arithmetic Operators', 'j_multiply', 'Multiplication').put()
    construct('*', 'Javascript', 'Arithmetic Operators', 'js_multiply', 'Multiplication').put()
    construct('*', 'Python', 'Arithmetic Operators', 'p_multiply', 'Multiplication').put()
    #Arithmetic Operators - Division
    construct('/', 'Java', 'Arithmetic Operators', 'j_divide', 'Division').put()
    construct('/', 'Javascript', 'Arithmetic Operators', 'js_divide', 'Division').put()
    construct('/', 'Python', 'Arithmetic Operators', 'p_divide', 'Division').put()
    #Arithmetic Operators - Modulus/Remainder
    construct('%', 'Java', 'Arithmetic Operators', 'j_modulo', 'Modulus').put()
    construct('%', 'Javascript', 'Arithmetic Operators', 'js_modulo', 'Modulus').put()
    construct('%', 'Python', 'Arithmetic Operators', 'p_modulo', 'Modulus').put()
    #Arithmetic Operators - Exponent
    construct('Math.pow(base, exponent)', 'Java', 'Arithmetic Operators', 'j_exp', 'Exponent').put()
    construct('Math.pow(base, exponent)', 'Javascript', 'Arithmetic Operators', 'js_exp', 'Exponent').put()
    construct('**', 'Python', 'Arithmetic Operators', 'p_exp', 'Exponent').put()

    #Comparison/Relational Operators - Equal
    construct('==\t.equals()', 'Java', 'Comparison/Relational Operators', 'j_equal', 'Equal').put()
    construct('==\t===', 'Javascript', 'Comparison/Relational Operators', 'js_equal', 'Equal').put()
    construct('==\tis', 'Python', 'Comparison/Relational Operators', 'p_equal', 'Equal').put()
    #Comparison/Relational Operators - Not Equal
    construct('!=', 'Java', 'Comparison/Relational Operators', 'j_notequal', 'Not Equal').put()
    construct('!=\t!==', 'Javascript', 'Comparison/Relational Operators', 'js_notequal', 'Not Equal').put()
    construct('!=\tis not', 'Python', 'Comparison/Relational Operators', 'p_notequal', 'Not Equal').put()
    #Comparison/Relational Operators - Less Than
    construct('<', 'Java', 'Comparison/Relational Operators', 'j_lessthan', 'Less Than').put()
    construct('<', 'Javascript', 'Comparison/Relational Operators', 'js_lessthan', 'Less Than').put()
    construct('<', 'Python', 'Comparison/Relational Operators', 'p_lessthan', 'Less Than').put()
    #Comparison/Relational Operators - Greather Than
    construct('>', 'Java', 'Comparison/Relational Operators', 'j_greaterthan', 'Greater Than').put()
    construct('>', 'Javascript', 'Comparison/Relational Operators', 'js_greaterthan', 'Greater Than').put()
    construct('>', 'Python', 'Comparison/Relational Operators', 'p_greaterthan', 'Greater Than').put()
    #Comparison/Relational Operators - Less Than or Equal To
    construct('<=', 'Java', 'Comparison/Relational Operators', 'j_lessthanequal', 'Less Than or Equal To').put()
    construct('<=', 'Javascript', 'Comparison/Relational Operators', 'js_lessthanequal', 'Less Than or Equal To').put()
    construct('<=', 'Python', 'Comparison/Relational Operators', 'p_lessthanequal', 'Less Than or Equal To').put()
    #Comparison/Relational Operators - Greater Than or Equal To
    construct('>=', 'Java', 'Comparison/Relational Operators', 'j_greaterthanequal', 'Greater Than or Equal To').put()
    construct('>=', 'Javascript', 'Comparison/Relational Operators', 'js_greaterthanequal', 'Greater Than or Equal To').put()
    construct('>=', 'Python', 'Comparison/Relational Operators', 'p_greaterthanequal', 'Greater Than or Equal To').put()

    #Logical Operators - And
    construct('&&', 'Java', 'Logical Operators', 'j_and', 'And').put()
    construct('&&', 'Javascript', 'Logical Operators', 'js_and', 'And').put()
    construct('and', 'Python', 'Logical Operators', 'p_and', 'And').put()
    #Logical Operators - Or
    construct('||', 'Java', 'Logical Operators', 'j_or', 'Or').put()
    construct('||', 'Javascript', 'Logical Operators', 'js_or', 'Or').put()
    construct('or', 'Python', 'Logical Operators', 'p_or', 'Or').put()
    #Logical Operators - Not
    construct('!', 'Java', 'Logical Operators', 'j_not', 'Not').put()
    construct('!', 'Javascript', 'Logical Operators', 'js_not', 'Not').put()
    construct('not', 'Python', 'Logical Operators', 'p_not', 'Not').put()

    #For Loop
    construct('for (int i=incl; i<excl; i+increment) { ... }', 'Java', 'Loops', 'j_forloop', 'For Loop').put()
    construct('for (int i=incl; i<excl; i+increment)', 'Javascript', 'Loops','js_forloop', 'For Loop').put()
    construct('for i in range(incl, excl):\n\t...', 'Python', 'Loops','p_forloop', 'For Loop').put()
    #Enhanced For Loop
    construct('for (type element : myArray) { ... }', 'Java', 'Loops', 'j_enhancedforloop', 'Enhanced For Loop').put()
    construct('for (var element in myArray)) { ... }', 'Javascript', 'Loops','js_enhancedforloop', 'Enhanced For Loop').put()
    construct('for element in myArray:\n\t...', 'Python', 'Loops','p_enhnacedforloop', 'Enhanced For Loop').put()
    #While Loop
    construct('while (condition) { ... }', 'Java', 'Loops', 'j_whileloop', 'While Loop').put()
    construct('while (condition) { ... }', 'Javascript', 'Loops','js_whileloop', 'While Loop').put()
    construct('while (condition):\n\t...', 'Python', 'Loops','p_whileloop', 'While Loop').put()

    #List Constructor
    construct('List myList = new ArrayList()', 'Java', 'Lists', 'j_list', 'Dynamic List').put()
    construct('var myList = [item1, item2, ...]', 'Javascript', 'Lists','js_list', 'Dynamic List').put()
    construct('myList = [item1, item2, ...]','Python', 'Lists','p_list', 'Dynamic List').put()
