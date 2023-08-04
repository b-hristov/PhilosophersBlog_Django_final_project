const posts = document.querySelectorAll('.post');
const postsContainer = document.querySelector('.post-container')
const pageContent = document.querySelector(".page-content")
const categoriesWidget = document.querySelector(".widget")
const numPosts = posts.length;
if (numPosts === 1) {
    posts[0].style.maxWidth = 'none';
    posts[0].style.flexBasis = 'auto';
    posts[0].style.maxheight = '300px';
    categoriesWidget.remove()
    pageContent.style.margin = '0';
    pageContent.style.alignItems = 'center';


}

if (numPosts === 2) {
    postsContainer.style.flexWrap = 'nowrap';
}

if (numPosts < 1) {
    pageContent.remove();
}
