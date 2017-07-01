function loadDoc() {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        document.getElementById("all").innerHTML = this.responseText;
    }
    };
    //var input2 = '{\"name\":\"" + "mStringTextPostText" + "\",\"IntID\":\"" + "mIntTextPostText" + "\",\"FloatID\":\"" + "mFloatTextPostText" + "\"}';

    var dd = document.getElementById("dd");
    var ddValue = dd.options[dd.selectedIndex].value;

    var textArea = document.getElementById("textCode").value;
    textArea = encodeURI(textArea);
    //textArea = textArea.replace(/\r?\n?/g, '\\n');

    var question = document.getElementById("problem").innerHTML

    var group = document.getElementById("textGroup").value

    group = group.replace(/[\/:*?"<>|.]/g, "");
    encodeURI(group)
    

    var d = new Date();

    var hour = d.getHours()
    var minutes = d.getMinutes();
    var seconds = d.getSeconds();
    var milliSeconds = d.getMilliseconds();

    var input = "{\"source\":\"" + textArea +
    "\",\"lang\":\"" + ddValue +
    "\",\"question\":\"" + question +
    "\",\"group\":\"" + group +
    "\",\"hour\":\"" + hour +
    "\",\"minutes\":\"" + minutes +
    "\",\"seconds\":\"" + seconds +
    "\",\"milliseconds\":\"" + milliSeconds +
    "\"}";

    xhttp.open("POST", "/post", true);

    xhttp.setRequestHeader("Content-Type", "application/json");
    //xhttp.setRequestHeader("Accept", "application/json");

    xhttp.send(input);

}