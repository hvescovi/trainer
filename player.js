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
    $('body').css("background-image", "url(/" + image);
    if (i == 0) { // first message? centered.
        x = $(window).width() / 2;
        y = $(window).height() / 2;
    } else { // place specified in the sequence
        coords = xy.split(",")
        x = coords[0]
        y = coords[1]
    }
    $("#msg").css({ left: x, top: y }); // put the box in its place
    $("#msg").html(msg);
    //alert(lines[i]);
}

$("#btn").click(function() {
            if (loaded) {
                if (currentSlide < lines.length {
                        currentSlide = currentSlide + 1;
                        loadSlide(currentSlide);
                    }
                }
                // $("#msg").animate({ left: '250px' });
            });