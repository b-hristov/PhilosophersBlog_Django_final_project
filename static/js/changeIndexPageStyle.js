const posts = document.querySelectorAll('.post');
const postsContainer = document.querySelector('.post-container')
const pageContent = document.querySelector(".page-content")
const numPosts = posts.length;
if (numPosts === 1) {
    posts[0].style.maxWidth = 'none';
    posts[0].style.flexBasis = 'auto';
    posts[0].style.maxheight = '300px';
    pageContent.style.margin = '0';
    pageContent.style.alignItems = 'center';
}

if (numPosts === 2) {
    postsContainer.style.flexWrap = 'nowrap';
}
