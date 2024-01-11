const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imgView = document.getElementById("img-view");

inputFile.addEventListener("change", uploadImage);


function uploadImage(){
    let imgLink = URL.createObjectURL(inputFile.files[0]);
    imgView.style.backgroundImage = `url(${imgLink})`;
    imgView.textContent = "";
    imgView.style.backgroundSize = 'contain'; // or 'cover'
    imgView.style.backgroundRepeat = 'no-repeat';
    imgView.style.backgroundPosition = 'center center';
}
