$(document).ready(syntaxChoice);

//checks all boxes
function loadChecked() {
    $(".language-box").prop("checked", true);
}
//Setup Functions
function syntaxChoice() {
    $(".flex-container").hover(addHighlight)
    $(".flex-container").mouseleave(removeHighlight)
    $("#java").click(displayJava);
    $("#javascript").click(displayJavascript);
    $("#python").click(displayPython);
}
function addHighlight(){
  $(this).addClass("highlighted");

}

function removeHighlight(){
  $(this).removeClass("highlighted");
}

$(document).ready(function(){
    $(".j-col").click(function(){
        $("#panel").slideToggle();
    });
});
$(document).ready(function(){
    $(".js-col").click(function(){
        $("#panel").slideToggle();
    });
});
  /*function handleExample() {
    $("#testappend").click();
    $("#panel").slideToggle("slow")
  }
function slidePanel() {
    $("#panel").slideToggle("slow")
    $("#panel2").slideToggle("slow")
}*/

//Toggle Functions
function displayJava() {
    $('.j-col').toggle(270);
}

function displayJavascript() {
    $('.js-col').toggle(270);
}

function displayPython() {
    $('.p-col').toggle(270);
}


function setup() {
    syntaxChoice();
    loadChecked();
  //  handleExample();
}

window.onload=loadChecked;
