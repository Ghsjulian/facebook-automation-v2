"use strict";

const checkCookie = () => {
    var username = getCookie("username");
    if (username != "") {
        alert("Welcome again " + username);
    } /*
  else {
    username = prompt("Please enter your name:", "");
    if (username != "" && username != null) {
      setCookie("username", username, 365);
    }
  }*/
};

const getCookie = cname => {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(";");
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
};

const facebook = async () => {
    const url = "http://m.facebook.com";
    //const url = "config/cookies.json";
    let request = await fetch(url);
    let response = await request.text();
    console.log(response);
};
const loadDoc = async () => {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        
        console.log(this.responseText);
    };
    xhttp.open("GET", "https://m.facebook.com/", true);
    xhttp.send();
};

const btn = document.getElementById("get-cookie");
btn.onclick = async () => {
    // await facebook();
    await loadDoc();
};
