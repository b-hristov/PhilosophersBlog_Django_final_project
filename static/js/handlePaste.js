function handlePaste(event) {
    // Prevent the default paste behavior
    event.preventDefault();
    const pastedText = (event.clipboardData || window.clipboardData).getData('text/plain');
    tinyMCE.activeEditor.execCommand('mceInsertContent', false, pastedText);
}