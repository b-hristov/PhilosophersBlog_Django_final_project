const posts = document.querySelectorAll('.post');
const numPosts = posts.length;
if (numPosts === 1) {
    posts[0].style.maxWidth = 'none';
    posts[0].style.flexBasis = 'auto';
}

if (numPosts < 1) {
    const categoriesWidget = document.querySelector(".post-content");
    categoriesWidget.remove()
}
