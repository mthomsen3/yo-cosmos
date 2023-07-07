// Get references to the dom elements
//var loaded = document.querySelector("#loaded");
//var sentinel = document.querySelector('#sentinel');



window.addEventListener("load", setupHeart(), false); 


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



function setupHeart() {
    let heart = document.querySelector("#heart");

    var url = window.location.href;
    //var match = url.replace(/\D/g,'');
    //var match = url.match(/post\/(\D)/);
    var post_id = parseInt(url.match(/\/post\/(\d+)/)[1]);
    //console.log(match);
    //tempid = match;

    if (checkLike(post_id) == true) {
        heart.setAttribute('fill', '#A9A9A9');
        heart.classList.add("liked");
    }

    // Add listener to like button

    heart.addEventListener("click", () => {
        let post_likecount = document.querySelector("#post_likecount");
        //console.log('handle likes...');
        if (heart.classList.contains("liked")) {

            post_likecount.innerHTML = parseInt(post_likecount.innerHTML) - 1;
            heart.setAttribute('fill', 'none');
            heart.classList.remove("liked");
            removeLike(post_id)
            htmx.ajax('POST', `/unlike/${post_id}`, { swap: 'none' })

        } else {

            heart.setAttribute('fill', '#A9A9A9');
            heart.classList.add("liked");
            post_likecount.innerHTML = parseInt(post_likecount.innerHTML) + 1;
            addLike(post_id);
            htmx.ajax('POST', `/like/${post_id}`, { swap: 'none' })

        }
    });
}




