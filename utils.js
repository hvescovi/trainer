function moveResizeMsgBox() {

    // move resize box
    wbox = $("#msg").width();
    hbox = $("#msg").height();
    //alert(x + " <> " + (parseInt(coords[0]) + wbox + 35));
    xresize = parseInt($("#msg").position().left + wbox + 34) + "px";
    yresize = parseInt($("#msg").position().top + hbox + 34) + "px";
    $("#btnResizeMsgBox").css({ left: xresize, top: yresize, position: 'absolute' });

}