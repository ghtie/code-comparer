
$(document).ready(syntaxChoice);

function syntaxChoice(){
  $("#java").click(displayJava)
  $("#javascript").click(displayJavascript)
  $("#python").click(displayPython)
}
$(document).ready(function(){
    $("#loop").click(function(){
        $("#panel, div.flex-item2 ").slideDown("slow");
    });
});
function displayJava(){
  $('div.flex-item2, div.flex-item5 ').toggle();
}

function displayJavascript(){
  $('div.flex-item3, div.flex-item6').toggle();
}

function displayPython(){
  $('div.flex-item4, div.flex-item7').toggle();
}
window.onload=function()
 {
   if (document.getElementById)
   {
var c = document.getElementById("java");
           c.checked = true;
}
if (document.getElementById)
{
var d = document.getElementById("javascript");
        d.checked = true;
}
if (document.getElementById)
{
var e = document.getElementById("python");
        e.checked = true;
}
}
