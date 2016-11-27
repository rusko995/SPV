// JavaScript source code
/*
//vedno, ko skrola, ga poslusa
function yHandler() {
    var wrap = document.getElementById('main');
    var contentHeight = main.offsetHeight;  //dobi visino 
    var yOffset = window.pageYOffset;       //dobi polozaj scrollerja
    var y = yOffset + window.innerHeight;   //poscrolano + notranje mere okna
    if (y >= contentHeight) {
        main.innerHTML += '<div class="newData"></div>';
        //ajax poklice nove podatke
    }
}
window.onscroll = yHandler;
*/
window.addEventListener("beforeunload", checkLeave);

function checkLeave(e) {
    var iskalnik = document.getElementById("hihi");
    if (iskalnik.value != iskalnik.defaultValue) {
        e.returnValue = "Opozorilo!";
        return "Nekaj si vpisal. Zares želiš oditi?";
    }
    return "OK";
}


//dobi elemente
var kontaktt = document.getElementById('kontaktt');
var gumbek = document.getElementById("gumb");
var span = document.getElementsByClassName("zapri")[0];

// odpri popup, ko klikne na gumb 
gumbek.onclick = function () {
    kontaktt.style.display = "block";
}

//zapri popup
span.onclick = function () {
    kontaktt.style.display = "none";
}
window.onclick = function (event) {
    if (event.target == kontaktt) {
        kontaktt.style.display = "none";
    }
}