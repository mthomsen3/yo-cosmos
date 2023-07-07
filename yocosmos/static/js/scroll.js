// Get references to the dom elements
var scroller = document.querySelector("#scroller");
var template = document.querySelector('#post_template');
var loaded = document.querySelector("#loaded");
var sentinel = document.querySelector('#sentinel');

// Set a counter to count the items loaded
var pagecounter = 0;

// Function to request new items and render to the dom
function loadItems() {

    // Use fetch to request data and pass the counter value in the QS
    fetch(`/load?c=${pagecounter}`).then((response) => {

        // Convert the response data to JSON
        response.json().then((data) => {

            // If empty JSON, exit the function
            if (data.posts == undefined || !data.posts.length) {

                // Replace the spinner with "No more posts"
                sentinel.innerHTML = "No more posts";
                return;
            }


            // Iterate over the items in the response
            for (var i = 0; i < data.posts.length; i++) {

                // Clone the HTML template
                let template_clone = template.content.cloneNode(true);

                // Unpack data from response, including posts and like counts (ip-based)
                postdata = JSON.parse(data.posts[i]);
                likedata = JSON.parse(data.likes[i]);

                let tempDateArray = postdata.date_posted.split(" ")


                // Query & update the template content
                template_clone.querySelector("#post_date").innerHTML = tempDateArray[0];
                template_clone.querySelector("#post_time").innerHTML = tempDateArray[1];
                template_clone.querySelector("#post_id").innerHTML = `<a href="/post/${postdata.id}">#${postdata.id}</a>`;
                template_clone.querySelector("#post_content").innerHTML = escapeHtml(postdata.content);
                template_clone.querySelector("#post_img").src = "/static/avatars/" + postdata.avatar_image;
                // this one is stored to modify for likes 
                let post_likecount = template_clone.querySelector("#post_likecount");
                let post_id = postdata.id;
                post_likecount.innerHTML = likedata;


                if (getCookie("mode") == "light") {
                    template_clone.querySelector("#post_content_area").classList.remove("darkmode");
                    template_clone.querySelector("#content_section_area").classList.remove("darkmode");
                    template_clone.querySelector("#post_precontent_area").classList.remove("darkmode");
                }

                // Setup like button fill based on user cookie
                // No longer need to worry about count, since that is done with ip counts now
                let heart = template_clone.querySelector("#heart");
                if (checkLike(postdata.id) == true) {
                    heart.setAttribute('fill', '#A9A9A9');
                    heart.classList.add("liked");
                }

                // Add listener to like button

                heart.addEventListener("click", () => {
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

                // Append template to dom
                scroller.appendChild(template_clone);

            }

            // Increment the pagecounter
            pagecounter += 1;
        })
    })
}


const escapeHtml = (unsafe) => {
    return unsafe.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#039;');
}


// Create a new IntersectionObserver instance
var intersectionObserver = new IntersectionObserver(entries => {

    // Uncomment below to see the entry.intersectionRatio when
    // the sentinel comes into view

    //entries.forEach(entry => {
    //  console.log(entry.intersectionRatio);
    //})

    // If intersectionRatio is 0, the sentinel is out of view
    // and we don't need to do anything. Exit the function
    if (entries[0].intersectionRatio <= 0) {
        return;
    }

    // Call the loadItems function
    loadItems();

});

// Instruct the IntersectionObserver to watch the sentinel
intersectionObserver.observe(sentinel);