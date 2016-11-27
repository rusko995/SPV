// JavaScript source code
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("log").addEventListener("click", izpisiLog);
});

function izpisiLog(event) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var lines = this.responseText.split('\n');
            for (var line = 0; line < lines.length; line++) {
                var node = document.createElement("LI");
                var textnode = document.createTextNode(lines[line]);
                node.appendChild(textnode);
                document.getElementById("myList").appendChild(node);
                //console.log(lines[line]);
            }
            //document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "log.txt", true);
    xhttp.send();
}
