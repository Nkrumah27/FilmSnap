function uploadImage() {
    const uploadInput = document.getElementById("upload");
    const file = uploadInput.files[0];
    
    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    // Create FormData object to send the image
    const formData = new FormData();
    formData.append("image", file);

    // Send image to the backend (Flask)
    fetch("/identify-movie", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the result
        const resultDiv = document.getElementById("result");
        if (data.title) {
            resultDiv.innerHTML = `<p>Movie: <strong>${data.title}</strong></p>`;
        } else {
            resultDiv.innerHTML = `<p>Sorry, no match found.</p>`;
        }
    })
    .catch(error => {
        console.error("Error uploading image:", error);
        alert("Something went wrong. Try again.");
    });
}
