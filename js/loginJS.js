// JavaScript source code

window.addEventListener("beforeunload", checkLeave);


function checkLeave(e) {
    var user = document.getElementById("lala");
    var pass = document.getElementById("hihi");

    if (user.value != user.defaultValue || pass.value != pass.defaultValue) {
        e.returnValue = "Opozorilo!";
        return "Nekaj si vpisal. Zares želiš oditi?";
    }
    return "OK";
}
