
function checkLike(id) {
    if (getCookie('likes') == "") {
        // no posts liked yet
        return false;
    } else {
        var likes_str = getCookie('likes');
        var likes_arr = JSON.parse(likes_str);

        if (likes_arr.includes(id)) {
            // this has been liked
            return true;

        } else {
            // likes array doesn't contain id
            return false;
        }
    }
}



function addLike(id) {
    if (getCookie('likes') == "") {
        // no posts liked yet, initialize likes cookie
        likes_arr = new Array();
        likes_arr.push(id);
        likes_str = JSON.stringify(likes_arr);
        createCookie('likes', likes_str, 365);

    } else {
        var likes_str = getCookie('likes');
        var likes_arr = JSON.parse(likes_str);

        if (likes_arr.includes(id)) {
            // already liked this, hmmm
        } else {
            // add id to likes array and update cookie
            likes_arr.push(id);
            likes_str = JSON.stringify(likes_arr);
            createCookie('likes', likes_str, 365);
        }
    }
}

function removeLike(id) {
    if (getCookie('likes') == "") {
        // no posts liked yet, nothing to do
        return;

    } else {
        var likes_str = getCookie('likes');
        var likes_arr = JSON.parse(likes_str);

        if (likes_arr.includes(id)) {
            // locate and terminate like
            var index = likes_arr.indexOf(id);
            if (index !== -1) {
                likes_arr.splice(index, 1);
                likes_str = JSON.stringify(likes_arr);
                createCookie('likes', likes_str, 365);
            }
        } else {
            // didn't like this already, nothing to do
            return;
        }
    }
}