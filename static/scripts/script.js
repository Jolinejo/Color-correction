const dropArea = document.getElementById("drop-area");
const inputFile = document.getElementById("input-file");
const imgView = document.getElementById("img-view");

inputFile.addEventListener("change", uploadImage);
var fired_button = "d"
document.addEventListener("click", function(event) {
  if (event.target.tagName === "BUTTON") {
    fired_button = event.target.value; // Update the value when a button is clicked
    console.log("Clicked button value:", fired_button); // Use the value as needed
  }
});
function uploadImage() {
  const file = inputFile.files[0];
  if (!file) {
      return; // Handle the case where no file is selected
  }

  const formData = new FormData();
  formData.append("image", file);
  url = '/upload/' + fired_button;

  // Clear the image view
  imgView.innerHTML = ''; 
  imgView.style.backgroundImage = ''; // Remove background image

  // Show loading indicator
  document.getElementById("loading").style.display = "block";

  fetch(url, {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      // Hide loading indicator
      document.getElementById("loading").style.display = "none";

      if (data.error) {
          console.error("Error processing image:", data.error);
          // Display an error message to the user
      } else {
          const img = document.createElement('img');
          img.src = 'data:image/jpeg;base64,' + data.image;
          imgView.innerHTML = ''; // Clear any previous content
          imgView.style.backgroundImage = `url(${img.src})`;
          imgView.style.backgroundSize = 'contain'; // or 'cover'
          imgView.style.backgroundRepeat = 'no-repeat';
          imgView.style.backgroundPosition = 'center center';
      }
  })
  .catch(error => {
      // Hide loading indicator in case of error
      document.getElementById("loading").style.display = "none";
      console.error("Error:", error);
  });

  inputFile.value = "";
}
