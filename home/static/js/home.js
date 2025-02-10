function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const status = document.getElementById('status');

    if (fileInput.files.length === 0) {
        status.innerText = "Please select a file.";
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('upload', file);

    fetch('http://127.0.0.1:8000/store/uploads/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCSRFToken() // Send CSRF token
        },
        credentials: 'include' // Ensure cookies are sent
    })
    .then(response => response.json())
    .then(data => {
        if (data.id) {
            status.innerText = "File uploaded successfully!";
        } else {
            status.innerText = "Upload failed.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        status.innerText = "Error uploading file.";
    });
}