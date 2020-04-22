currentSlide = 0; // current slide/line of the text file
loaded = false; // the sequence file is not loaded yet
lines = []

// first values of x and y (centered)
//x = $(window).width() / 2;
//y = $(window).height() / 2;

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
    $('body').css("background-image", "url('/" + image + "'");
    //if (i > 0) { // is not the first time? update coordinates
    coords = xy.split(",")
    x = coords[0] + "px";
    y = coords[1] + "px";
    //}
    $("#msg").css({ left: x, top: y, position: 'absolute' }); // put the box in its place
    $("#msg").html(msg);
    //alert(lines[i]);
}

$("#btn").click(function() {
    if (loaded) {
        currentSlide = currentSlide + 1;
        if (!(typeof lines[currentSlide] === 'undefined')) {
            loadSlide(currentSlide);
        }
    }
});