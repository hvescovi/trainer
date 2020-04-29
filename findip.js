// when the document is ready...
$(function() {
    if (document.URL.startsWith("http://localhost")) {
        $("#myip").text("localhost");
    } else if (document.URL.startsWith("http://k8master")) {
        $("#myip").text("k8master.blumenau.ifc.edu.br");
    } else {
        $("#myip").text("ERROR");
    }
});