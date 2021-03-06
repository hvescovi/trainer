$(function() {

currentSlide = 0; // current slide/line of the text file
loaded = false; // the sequence file is not loaded yet
lines = []

$.ajax({
    url: "sequence.txt",
    dataType: "text",
    cache: false,
    success: function(data) {
        lines = data.split("\n");
        loaded = true; // file loaded!
        loadSlide(currentSlide); // load it!
    }
});

function loadSlide(i) {

    // playing or editing?
    if  ($("#myip").text() != "localhost") {

        // hide designer components
        $("#btnResizeMsgBox").hide();
        $("#btnMoveNavigator").hide();
      //  alert("playing!");
    } else {
       // alert("editiing");
    }


    parts = lines[i].split("|");
    image = parts[0]
    msg = parts[1]
    xy = parts[2]
    playxy = parts[3]
    sizemsgbox = parts[4]

    $('body').css("background-image", "url('" + image + "'");
    //$('#screenshot').attr("src", image);

    sizesbox = sizemsgbox.split(",")
    wbox = sizesbox[0] + "px";
    hbox = sizesbox[1] + "px";

    //alert("carregando ==> " + sizesbox);

    coords = xy.split(",")
    x = coords[0] + "px";
    y = coords[1] + "px";
    $("#msg").css({ left: x, top: y, position: 'absolute' }); // put the box in its place
    $("#msg").width(wbox);
    //alert("ok");
    //$("#msg").height(hbox);
    $("#msg").html(msg);

    //moveResizeMsgBox();

    wbox = $("#msg").width();
    hbox = $("#msg").height();
    //alert(x + " <> " + (parseInt(coords[0]) + wbox + 35));
    xresize = parseInt($("#msg").position().left + wbox + 34) + "px";
    yresize = parseInt($("#msg").position().top + hbox + 34) + "px";
    $("#btnResizeMsgBox").css({ left: xresize, top: yresize, position: 'absolute' });
    
    coords2 = playxy.split(",");
    px = coords2[0] + "px";
    pxTmp = parseInt(coords2[0])
    py = coords2[1] + "px";
    $("#navigator").css({ left: px, top: py, position: 'absolute' }); // put the box in its place
    $("#currentSlide").text((currentSlide + 1) + '/' + (lines.length));
}

$("#btnNext").click(function() {
    if (loaded) {
        // do not move textbox
        moveBox = false
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

});