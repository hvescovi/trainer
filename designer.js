// do not move textbox yet
moveBox = false

$(document).bind('mousemove', function(e) {

    if (moveBox) {
        // get current mouse position
        x = e.pageX;
        y = e.pageY;
        // put the textbox there
        $("#msg").css({ left: x, top: y });
        // show the coordinates
        $("#coordinates").text("x=" + x + ", y=" + y);
    }
});

$("#btnMsg").click(function() {
    $("#msg").animate({ left: '250px' });
});

$(document).bind('mousedown', function(e) {
    moveBox = !moveBox; // toogle the moving 
    if (!moveBox) { // if stopped the movement
        // make it real
        $("#msg").animate({ opacity: '1' });
    } else {
        // make it transparent
        $("#msg").animate({ opacity: '0.4' });
    }
});