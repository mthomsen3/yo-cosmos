
let popUp = document.getElementById("cookiePopup");
let screenOverlay = document.getElementById("cookiePopupOverlay");
let darkmodeElems = document.querySelectorAll('.has-darkmode');


//Check if cookie exists when page loads
window.onload = () => {
    checkmode();
    setTimeout(() => {
        checkcookieAccept();
    }, 300);
};

function createCookie(name, value, days) {
    var expires;
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toGMTString();
    }
    else {
        expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
}


// Returns cookie by key
/*
function getCookie(cookieName) {
    let cookie = {};
    document.cookie.split(';').forEach(function (el) {
        let [key, value] = el.split('=');
        cookie[key.trim()] = value;
    })
    return cookie[cookieName];
}
*/

function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) {
                c_end = document.cookie.length;
            }
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}




//When user clicks the accept button
document.getElementById("acceptCookie").addEventListener("click", () => {

    createCookie('cookieAccept', 'true', 365);

    //Hide the popup
    popUp.classList.add("hide");
    popUp.classList.remove("show");
    screenOverlay.classList.add("hide");
    screenOverlay.classList.remove("show");
    document.body.style.overflowY = "visible";
});


const checkcookieAccept = () => {

    //Check for our cookie
    if (getCookie("cookieAccept") == "true") {
        //Hide the popup
        popUp.classList.add("hide");
        popUp.classList.remove("show");
        screenOverlay.classList.add("hide");
        screenOverlay.classList.remove("show");
        document.body.style.overflowY = "visible";
    } else {
        //Show the popup
        popUp.classList.add("show");
        popUp.classList.remove("hide");
        screenOverlay.classList.add("show");
        screenOverlay.classList.remove("hide");
        document.body.style.overflowY = "hidden";
    }
};

const checkmode = () => {
    //Check for our cookie
    if (getCookie("mode") == "light") {
        darkmodeElems.forEach(function (element) {
            if (element.classList.contains('darkmode')) {
                element.classList.remove("darkmode");
            }
        })
        stars = document.querySelector('#stars');
        stars2 = document.querySelector('#stars2');
        stars3 = document.querySelector('#stars3');
        stars4 = document.querySelector('#stars4');
        stars.id = 'darkstars';
        stars2.id = 'darkstars2';
        stars3.id = 'darkstars3';
        stars4.id = 'darkstars4';
    } else if (getCookie("mode") == "dark") {
        darkmodeElems.forEach(function (element) {
            if (element.classList.contains('darkmode') == false) {
                element.classList.add("darkmode");
            }
        })

    } else {
        // Mode state cookie instantiates to dark mode if no mode cookie found
        createCookie('mode', 'dark', 365);
        //document.cookie = "mode=dark; expires = " + d + ";";
        //console.log("Unrecognized MODE value. Please reset cookies.");
    }
};


