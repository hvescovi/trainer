// do not move textbox yet
moveBox = false
moveNav = false
    //$("#btnMsg").click(function() {
    //$("#msg").animate({ left: '250px' });
    //});

$("#msg").click(function() {
    moveBox = !moveBox; // toogle the moving 
    moveNav = false;
    if (!moveBox) { // if stopped the movement
        // make it real
        $("#msg").animate({ opacity: '1' });

        updateCurrentScreen();
    } else {
        // make it transparent
        $("#msg").animate({ opacity: '0.4' });
    }
});

function updateCurrentScreen() {
    // get data
    img = getImageFileName(currentSlide);
    msg = $("#msg").text();
    msgcoord = $("#msg").position().left + ", " + $("#msg").position().top;
    navcoord = $("#navigator").position().left + ", " + $("#navigator").position().top;

    //alert(img + " | " + msg + "|" + msgcoord + "|" + navcoord);
    // update text file
    updateLine(img, msg, msgcoord, navcoord);

    // update internal data
    lines[currentSlide] = img + "|" + msg + "|" + msgcoord + "|" + navcoord;
}

function updateLine(img, msg, msgcoord, navcoord) {

    var dataToSend = JSON.stringify({ img: img, msg: msg, msgcoord: msgcoord, navcoord: navcoord })

    myip = $("#myip").text();
    $.ajax({
        url: 'http://' + myip + ':5000/update_line',
        type: 'POST',
        dataType: 'json', // answer is received in json
        data: dataToSend,
        //contentType: "application/json",
        success: function(result) {
            var ok = result.message == "ok";

            // coloca a resposta no gabarito
            $("#coordinates").text(result.details);
            // alert(resultado.details);
            //mostrar_resultado_acao(deu_certo);
            if (!ok) {
                alert(result.message + ":" + resultado.details);
            }

        },
        error: function() {
            alert("error reading data, check the backend");
        }
    });

}

$("#btnMoveNavigator").click(function() {
    moveNav = !moveNav; // toogle the moving 
    moveBox = false;
    if (!moveNav) { // if stopped the movement
        // make it real
        $("#navigator").animate({ opacity: '1' });

        updateCurrentScreen();
    } else {
        // make it transparent
        $("#navigator").animate({ opacity: '0.4' });
    }
});

$(document).mousemove(function(e) {
    if (moveBox) {
        // get current mouse position
        x = e.pageX - 5;
        y = e.pageY - 5;
        // put the textbox there
        $("#msg").css({ left: x, top: y });
        // show the coordinates
        $("#coordinates").text(x + "," + y);
    }

    if (moveNav) {
        // get current mouse position
        x = e.pageX - 120;
        y = e.pageY - 25;
        // put the textbox there
        $("#navigator").css({ left: x, top: y });
        // show the coordinates
        $("#coordinates").text("x=" + x + ", y=" + y);
    }

});