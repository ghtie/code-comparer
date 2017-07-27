class DisplayMoreInfo:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def listString(self, page_id):
        return "<a href='post?page_id=" + str(page_id) + "'>" + self.title + "</a>"

language_list = [
    DisplayMoreInfo(
        "Java",
        """<h1 id="jhead"> What is Java</h1>
        <p id='jp1'> Java is a general-purpose computer programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers \'write once, run anywhere\', meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typically compiled to bytecode that can run on any Java virtual machine regardless of computer architecture.
        <br> <br> Example <br><br> </p>"""
        """<p id='jp2'>
        class Integers { <br>
  public static void main(String[] arguments) {<br>
    <div id="test2"> int c; //declaring a variable</div><br>

  /* Using for loop to repeat instruction execution */<br>

    <div id="test2">for (c = 1; c <= 10; c++) {</div><br>
     <div id="test2"> System.out.println(c);</div><br>
    }<br>
  }<br>
}<br>
</p>
        """
        ),
    DisplayMoreInfo(
        "JavaScript",
        """<h1 id="jhead"> What is javascript</h1>
        <p id='jp1'>JavaScript is an interpreted programming or script language from Netscape. It is somewhat similar in capability to Microsoft'sVisual Basic, Sun's Tcl, the UNIX-derived Perl, and IBM's REXX. In general, script languages are easier and faster to code in than the more structured and compiled languages such as C and C++. Script languages generally take longer to process than compiled languages, but are very useful for shorter programs.JavaScript uses some of the same ideas found in Java, the compiled object-oriented programming derived from C++. JavaScript code can be imbedded in HTML pages and interpreted by the Web browser (or client). JavaScript can also be run at the server as in Microsoft's Active Server Pages before the page is sent to the requestor. Both Microsoft and Netscape browsers support JavaScript, but sometimes in slightly different ways.<br> <br> Example <br><br></p>"""
        """<p id='jp2'>$(document).ready(syntaxChoice);<br>

        //checks all boxes<br>
        function loadChecked() {<br>
            <div id="test2">$(".language-box").prop("checked", true);</div><br>
        }<br>
        //Setup Functions<br>
        function syntaxChoice() {<br>
            <div id="test2">$(".flex-container").hover(addHighlight)</div><br>
            <div id="test2">$(".flex-container").mouseleave(removeHighlight)</div><br>
            <div id="test2">$("#java").click(displayJava);</div><br>
            <div id="test2">$("#javascript").click(displayJavascript);</div><br>
            <div id="test2">$("#python").click(displayPython);</div><br>
        }<br>
        function addHighlight(){<br>
         <div id="test2"> $(this).addClass("highlighted");</div><br>

        }<br>

        function removeHighlight(){<br>
         <div id="test2"> $(this).removeClass("highlighted");</div><br>
        }<br>"""
),
    DisplayMoreInfo(
        "Python",
        """<h1 id="jhead"> What is Python</h1>
        <p id='jp1'>Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy that emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax that allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.[22][23] The language provides constructs intended to enable writing clear programs on both a small and large scale.[24]

Python features a dynamic type system and automatic memory management and supports multiple programming paradigms, including object-oriented, imperative, functional programming, and procedural styles. It has a large and comprehensive standard library.<br> <br> Example <br><br></p>"""
"""<p id='jp2'>!/usr/bin/python<br>

import random<br>

 #Using the back ticks, which convert to string.<br>
for n in range(0,5):<br>
    <div id="test2">a = random.randrange(0, 101)<br>
    <div id="test2">b = random.randrange(0, 201)<br>
    <div id="test2">print `a` + '+' + `b`, '=', `a+b`<br>
print<br>

 #Using the % operator, similar to printf.<br>
for n in range(0,5):<br>
    <div id="test2">a = random.randrange(0, 101)<br>
    <div id="test2">b = random.randrange(0, 201)<br>
    <div id="test2">print '%d+%d = %d' % (a, b, a + b)<br>
print<br>

 #% allows field sizes as well.<br>
for n in range(0,5):<br>
    <div id="test2">a = random.randrange(-100, 101)<br>
    <div id="test2">b = random.randrange(-50, 201)<br>
    <div id="test2">print '%4d + %4d = %4d' % (a, b, a + b)<br>
print<br>

 #Some other formatting.<br>
dribble = { 'onion' : 1.4,<br>
            <div id="test2">'squash' : 2.02,<br>
            <div id="test2">'carrots' : 1.0,<br>
            <div id="test2">'pixie toenails' : 43.22,<br>
            <div id="test2">'lemon drops' : .75 }<br>
for n in dribble.keys():
    <div id="test2">print '%-15s %6.2f' % (n + ':', dribble[n])</p>"""
)
]
