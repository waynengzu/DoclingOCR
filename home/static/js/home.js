function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}

let uploadedFileUrl = '';

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const status = document.getElementById('status');
    const processButton = document.getElementById('processButton');

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
            'X-CSRFToken': getCSRFToken()
        },
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        if (data.id && data.upload) {
            status.innerText = "File processed successfully!";
            uploadedFileUrl = data.upload;
            displayFile(data.upload);
            processButton.disabled = false;
        } else {
            status.innerText = "Process failed.";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        status.innerText = "Error processing file.";
    });
}

function displayFile(fileUrl) {
    const previewText = document.getElementById('preview-text');
    const previewImage = document.getElementById('preview');
    const pdfPreview = document.getElementById('pdf-preview');

    // Hide text placeholder
    previewText.style.display = "none";
    previewImage.style.display = "none";
    pdfPreview.style.display = "none";

    // Determine file type
    if (fileUrl.toLowerCase().endsWith('.pdf')) {
        // PDFs should be displayed in an iframe
        pdfPreview.src = fileUrl;
        pdfPreview.style.display = "block";
    } else {
        // Images should be displayed in an img tag
        previewImage.src = fileUrl;
        previewImage.style.display = "block";
    }
}

function processFile() {
    if (uploadedFileUrl) {
        window.location.href = `/home/processed?file=${encodeURIComponent(uploadedFileUrl)}`;
    }
}