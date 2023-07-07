
document.getElementById("starButton").addEventListener("click", () => {
    //Reset the list for new template-generated content blocks
    if (getCookie("mode") == "light") {
        stars = document.querySelector('#darkstars');
        stars2 = document.querySelector('#darkstars2');
        stars3 = document.querySelector('#darkstars3');
        stars4 = document.querySelector('#darkstars4');

        stars.classList.contains("paused") ? stars.classList.remove("paused") : stars.classList.add("paused");
        stars2.classList.contains("paused") ? stars2.classList.remove("paused") : stars2.classList.add("paused");
        stars3.classList.contains("paused") ? stars3.classList.remove("paused") : stars3.classList.add("paused");
        stars4.classList.contains("paused") ? stars4.classList.remove("paused") : stars4.classList.add("paused");

    } else if (getCookie("mode") == "dark") {
        stars = document.querySelector('#stars');
        stars2 = document.querySelector('#stars2');
        stars3 = document.querySelector('#stars3');
        stars4 = document.querySelector('#stars4');

        stars.classList.contains("paused") ? stars.classList.remove("paused") : stars.classList.add("paused");
        stars2.classList.contains("paused") ? stars2.classList.remove("paused") : stars2.classList.add("paused");
        stars3.classList.contains("paused") ? stars3.classList.remove("paused") : stars3.classList.add("paused");
        stars4.classList.contains("paused") ? stars4.classList.remove("paused") : stars4.classList.add("paused");

    } else {
        console.log("Animation switch error.");
    }


});


document.getElementById("modeButton").addEventListener("click", () => {
    //Reset the list for new template-generated content blocks
    darkmodeElems = document.querySelectorAll('.has-darkmode');
    //Check for our cookie
    if (getCookie("mode") == "light") {

        darkmodeElems.forEach(function (element) {
            if (element.classList.contains('darkmode') == false) {
                element.classList.add("darkmode");
            }
        })
        stars = document.querySelector('#darkstars');
        stars2 = document.querySelector('#darkstars2');
        stars3 = document.querySelector('#darkstars3');
        stars4 = document.querySelector('#darkstars4');
        stars.id = 'stars';
        stars2.id = 'stars2';
        stars3.id = 'stars3';
        stars4.id = 'stars4';
        createCookie('mode', 'dark', 365);

    } else if (getCookie("mode") == "dark") {

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
        createCookie('mode', 'light', 365);

    } else {
        console.log("Mode switch error.");
    }
});
