// Prevent form submission if only space characters are entered
function validateComment() {
    const commentContent = document.getElementById('comment-content').value;
    if (commentContent.trim() === '') {
        alert("Comment content cannot be empty.");
        return false;
    }
    return true;
}