// do not move textbox (designer mode)
moveBox = false

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

function loadSlide(i) {
    parts = lines[i].split("|");
    image = parts[0]
    msg = parts[1]
    xy = parts[2]
    playxy = parts[3]

    $('body').css("background-image", "url('/" + image + "'");

    coords = xy.split(",")
    x = coords[0] + "px";
    y = coords[1] + "px";
    $("#msg").css({ left: x, top: y, position: 'absolute' }); // put the box in its place
    $("#msg").html(msg);
    //alert(y);

    coords2 = playxy.split(",");
    px = coords2[0] + "px";
    py = coords2[1] + "px";
    $("#btn").css({ left: px, top: py, position: 'absolute' }); // put the box in its place
    //alert(lines[i]);
}

$("#btn").click(function() {
    if (loaded) {
        // do not move textbox
        moveBox = false
        currentSlide = currentSlide + 1;
        if (!(typeof lines[currentSlide] === 'undefined')) {
            loadSlide(currentSlide);
        }
    }
});