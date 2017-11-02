$(document).ready(setup);

//Setup Functions
function setup() {
    syntaxChoice();
    loadChecked();
    handleHighlight();
    /*$(".j-panel").hide();
    $(".js-panel").hide();
    $(".p-panel").hide();*/
    handleExample();
    openNav();
    closeNav();
}

//Loads window with boxes default checked
function loadChecked() {
    $(".language-box").prop("checked", true);
}

//Navigation bar open & close
function openNav() {
    document.getElementById("navBar").style.width = "250px";
}

function closeNav() {
    document.getElementById("navBar").style.width = "0";
}

//Calls other functions to show/ hide the column after checkbox is clicked
function syntaxChoice() {
    $("#javaBox").click(displayJava);
    $("#jSBox").click(displayJavascript);
    $("#pythonBox").click(displayPython);
}

//When mouse hovered over row, highlight row
function handleHighlight() {
    $(".flex-container").hover(addHighlight)
    $(".flex-container").mouseleave(removeHighlight)
}

//Expands the boxes to reveal example links
function handleExample() {
    $(".flex-container").click(slidePanel);
}

//Shows or hide the columns
function displayJava() {
    $('.j-col').fadeToggle(700);
}
function displayJavascript() {
    $('.js-col').fadeToggle(700);
}
function displayPython() {
    $('.p-col').fadeToggle(700);
}

//Highlight functions when mouse hovers over elements
function addHighlight() {
    $(this).addClass("highlighted");
}
function removeHighlight(){
    $(this).removeClass("highlighted");
}

//Panel slide functions
function slidePanel() {
    $(this).find(".j-panel").slideToggle("medium");
    $(this).find(".js-panel").slideToggle("medium");
    $(this).find(".p-panel").slideToggle("medium");
}
