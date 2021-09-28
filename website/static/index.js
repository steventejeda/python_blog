const commentArea = document.getElementById('content');

const characterCount = document.getElementById('cCount');

commentArea.oninput = () => {
    let characters = commentArea.value;
    characterCount.textContent = characters.length;
}