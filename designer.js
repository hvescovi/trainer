// do not move textbox yet
moveBox = false
moveNav = false
resizeMsg = false

//$("#btnMsg").click(function() {
//$("#msg").animate({ left: '250px' });
//});

$("#msg").click(function() {

    // playing or editing?
    if  ($("#myip").text() == "localhost") {

        moveBox = !moveBox; // toogle the moving 
        moveNav = false;
        resizeMsg = false;
        //alert($("#msg").width() + "," + $("#msg").height());
        if (!moveBox) { // if stopped the movement
            // make it real
            $("#msg").animate({ opacity: '1' });

            // move resize box
            moveResizeMsgBox();

            updateCurrentScreen();
        } else {
            // make it transparent
            $("#msg").animate({ opacity: '0.4' });
        }

    }
});

function updateCurrentScreen() {
    // get data
    img = getImageFileName(currentSlide);
    msg = $("#msg").text();
    msgcoord = $("#msg").position().left + ", " + $("#msg").position().top;
    navcoord = $("#navigator").position().left + ", " + $("#navigator").position().top;
    msgboxsize = $("#msg").width() + "," + $("#msg").height();

    //alert(msgboxsize);

    //alert(img + " | " + msg + "|" + msgcoord + "|" + navcoord);
    // update text file
    updateLine(img, msg, msgcoord, navcoord, msgboxsize);

    // update internal data
    lines[currentSlide] = img + "|" + msg + "|" + msgcoord + "|" + navcoord + "|" + msgboxsize;
}

function updateLine(img, msg, msgcoord, navcoord, msgboxsize) {

    var dataToSend = JSON.stringify({ img: img, msg: msg, msgcoord: msgcoord, navcoord: navcoord, msgboxsize: msgboxsize })

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
    resizeMsg = false;
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

    // $("#coordinates").text($("#msg").width() + "," + $("#msg").height());

    if (moveBox) {
        // get current mouse position
        x = e.pageX - 10;
        y = e.pageY - 10;
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

    if (resizeMsg) {
        // get current mouse position
        x = e.pageX;
        y = e.pageY;

        h = y - $("#msg").position().top;
        w = x - $("#msg").position().left - 15;

        // resize!
        $("#msg").css({ height: h, width: w });

        $("#coordinates").text(h + "," + w);

        moveResizeMsgBox();

    }

});

function moveResizeMsgBox() {
    // move resize box
    wbox = $("#msg").width();
    hbox = $("#msg").height();
    //alert(x + " <> " + (parseInt(coords[0]) + wbox + 35));
    xresize = parseInt($("#msg").position().left + wbox + 34) + "px";
    yresize = parseInt($("#msg").position().top + hbox + 34) + "px";
    $("#btnResizeMsgBox").css({ left: xresize, top: yresize, position: 'absolute' });
}

$("#btnResizeMsgBox").click(function() {
    resizeMsg = !resizeMsg; // toogle the moving 
    moveBox = false;
    moveNav = false;
    if (!resizeMsg) {
        // make it real
        $("#btnResizeBoxMsg").animate({ opacity: '1' });

        updateCurrentScreen();
    } else {
        // make it transparent
        $("#btnResizeBoxMsg").animate({ opacity: '0.4' });
    }
});