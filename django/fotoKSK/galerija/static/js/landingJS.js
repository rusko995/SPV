// JavaScript source code
/*
//vedno, ko skrola, ga poslusa in pol doda vsebino na stran
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
document.addEventListener("DOMContentLoaded", function () {
    document.getElementsByClassName("zapri")[0].addEventListener("click", span);
    document.getElementById("gumb").addEventListener("click", gumbek);
});
window.addEventListener("beforeunload", checkLeave);

function checkLeave(e) {
    var iskalnik = document.getElementById("hihi");
    if (iskalnik.value != iskalnik.defaultValue) {
        e.returnValue = "Opozorilo!";
        return "Nekaj si vpisal. Zares želiš oditi?";
    }
    return "OK";
}

function gumbek (event){
		kontaktt.style.display = "block";
}
function span (event){
		kontaktt.style.display = "none";
	}
window.onload = function(){ 
	//dobi elemente
	var kontaktt = document.getElementById('kontaktt');

	window.onclick = function (event) {
		if (event.target == kontaktt) {
			kontaktt.style.display = "none";
		}
	}

};