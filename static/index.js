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
    $("#testappend").click(slidePanel);
}

function slidePanel() {
    $("#panel").slideToggle("slow");

}
function handle() {
    $("#testappend1").click(slide);
}

function slide() {
    $("#panel2").slideToggle("slow");

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


//$(document).ready(function() {$('#test').append('<div class="flex-item4"><br>box 6<div>)'}
