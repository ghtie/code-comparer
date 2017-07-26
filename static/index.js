$(document).ready(setup);


//Setup Functions
function loadChecked() {                               //Loads window with boxes default checked
    $(".language-box").prop("checked", true);
}

function syntaxChoice() {                               //When checkbox selected, show language column
    $("#java").click(displayJava);
    $("#javascript").click(displayJavascript);
    $("#python").click(displayPython);
}

function handleHighlight() {                            //When mouse hovered over row, highlight row
    $(".flex-container").hover(addHighlight)
    $(".flex-container").mouseleave(removeHighlight)
}

function handleExample() {                              //"#idPanel"
    $(".flex-container").click(slidePanel);
}




//Helper Functions
function displayJava() {                                //Toggle Functions
    $('.j-col').toggle(270);
}
function displayJavascript() {
    $('.js-col').toggle(270);
}
function displayPython() {
    $('.p-col').toggle(270);
}

function addHighlight() {                               //Highlight Functions
    $(this).addClass("highlighted");
}
function removeHighlight(){
    $(this).removeClass("highlighted");
}

function slidePanel() {                                 //Panel Slide Functions
    $(this).find(".j-panel").slideToggle("slow");
    $(this).find(".js-panel").slideToggle("slow");
}


function setup() {
    syntaxChoice();
    loadChecked();
    handleHighlight();
    handleExample()
    }

//window.onload=loadChecked;
