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

$(document).ready(function(){
    $("#testappend1").click(function(){
        $("#panel2").slideToggle();
    });
  });
  $(document).ready(function(){
      $("#testappend").click(function(){
          $("#panel").slideToggle();
      });
    });
  //function handleExample() {
    //$("#testappend").click();
    //$("#panel").slideToggle("slow")
  //}
//function slidePanel() {
  //  $("#panel").slideToggle("slow")
    //$("#panel2").slideToggle("slow")

//}



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
