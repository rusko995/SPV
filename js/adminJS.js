document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("zaZajem").addEventListener("click", prikaziZajem);
    document.getElementById("snap").addEventListener("click", dajNaCanvas);
});
function prikaziZajem(event) {
    var prikaz = document.getElementById("zajem");
    if (prikaz.style.visibility == 'visible') {
        prikaz.style.visibility = 'hidden';
    } else {
        prikaz.style.visibility = 'visible';
        var video = document.getElementById('video');
        var errBack = function (e) {
            console.log('An error has occurred!', e)
        }

        // Get access to the camera!
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            // Not adding `{ audio: true }` since we only want video now
            navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
                video.src = window.URL.createObjectURL(stream);
                video.play();
            });
        }
    }
}

function dajNaCanvas(event) {
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    context.drawImage(video, 0, 0, 130, 130);
}


