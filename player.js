currentSlide = 0; // current slide/line of the text file
loaded = false; // the sequence file is not loaded yet
lines = []

$.ajax({
    url: "sequence.txt",
    dataType: "text",
    success: function(data) {
        lines = data.split("\n");
        loaded = true; // file loaded!
        loadSlide(currentSlide); // load it!
    }
});

function getImageFileName(i) {
    parts = lines[i].split("|");
    return parts[0]
}

function loadSlide(i) {
    parts = lines[i].split("|");
    image = parts[0]
    msg = parts[1]
    xy = parts[2]
    playxy = parts[3]

    $('body').css("background-image", "url('/" + image + "'");
    //$('#screenshot').attr("src", image);

    coords = xy.split(",")
    x = coords[0] + "px";
    y = coords[1] + "px";
    $("#msg").css({ left: x, top: y, position: 'absolute' }); // put the box in its place
    $("#msg").html(msg);

    wbox = $("#msg").width();
    hbox = $("#msg").height();
    //alert(x + " <> " + (parseInt(coords[0]) + wbox + 35));
    xresize = (parseInt(coords[0]) + wbox + 34) + "px";
    yresize = (parseInt(coords[1]) + hbox + 34) + "px";
    $("#btnResizeMsgBox").css({ left: xresize, top: yresize, position: 'absolute' });
    //alert(y);

    coords2 = playxy.split(",");
    px = coords2[0] + "px";
    pxTmp = parseInt(coords2[0])
        //pxNext = (pxTmp + 45).toString() + "px";
        //pxMove = (pxTmp + 85).toString() + "px";
    py = coords2[1] + "px";
    $("#navigator").css({ left: px, top: py, position: 'absolute' }); // put the box in its place
    //$("#btnPrevious").css({ left: px, top: py, position: 'absolute' }); // put the box in its place
    //$("#btnNext").css({ left: pxNext, top: py, position: 'absolute' }); // put the box in its place
    //$("#btnNext").css({ left: pxNext, top: py, position: 'absolute' }); // put the box in its place
    //alert(lines[i]);

    //alert(currentSlide);
    //alert(currentSlide + '/' + lines.length);
    $("#currentSlide").text((currentSlide + 1) + '/' + (lines.length));
}

$("#btnNext").click(function() {
    if (loaded) {
        // do not move textbox
        moveBox = false
            //alert(currentSlide + "/" + lines.length);
        if ((currentSlide + 1) < lines.length) {
            currentSlide = currentSlide + 1;
            if (!(typeof lines[currentSlide] === 'undefined')) {
                loadSlide(currentSlide);
            }
        }
    }
});

$("#btnPrevious").click(function() {
    if (loaded) {
        // do not move textbox
        moveBox = false
        if (currentSlide > 0) {
            currentSlide = currentSlide - 1;
            if (!(typeof lines[currentSlide] === 'undefined')) {
                loadSlide(currentSlide);
            }
        }
    }
});