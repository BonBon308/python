function myFunction() {
    document.getElementById("p3").innerHTML = "Paragraph changed.";
  }

  function consoleLog(){
      console.log('console log accepts results');
  }
function createLink(){
    var a = document.createElement('a');
    var linkText = document.createTextNode("my title text");
    a.appendChild(linkText);
    a.title = "my title text";
    a.href = "http://google.com";
    document.body.appendChild(a);
}