$(document).ready(setup);




//Setup Functions
function syntaxChoice() {
  $("#java").click(displayJava);
  $("#javascript").click(displayJavascript);
  $("#python").click(displayPython);
}

function loadChecked() {
    $(".language-box").prop("checked", true);
}

function handleExample() {
    $("#test").click(function(){$("#panel").slideToggle("slow");})
}

function testAppend() {
    $("#testappend").append('<div class="p-col"><br>box 6 </div>')
}




//Toggle Functions
function displayJava() {
  $('.j-col').toggle();
}

function displayJavascript() {
  $('.js-col').toggle();
}

function displayPython() {
  $('.p-col').toggle();
}




function setup() {
    syntaxChoice();
    loadChecked();
    handleExample();
}

window.onload=loadChecked;
