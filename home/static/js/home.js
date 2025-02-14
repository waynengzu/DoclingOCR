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
    const progressContainer = document.getElementById("progress-container");
    const progressBar = document.getElementById("progress-bar");

    if (fileInput.files.length === 0) {
        status.innerText = "Please select a file.";
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('upload', file);

    // Show and reset progress bar
    progressContainer.style.display = "block";
    progressBar.style.width = "0%";

    let progress = 0;
    const duration = 120000; // 120 seconds (2 minutes) in milliseconds
    const intervalTime = duration / 100; // 100 steps (1200ms per step)

    const interval = setInterval(() => {
        progress += 1; // Increase by 1% per step
        progressBar.style.width = progress + "%";

        if (progress >= 100) {
            clearInterval(interval);
        }
    }, intervalTime);

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
        clearInterval(interval); // Ensure progress stops

        if (data.id && data.upload) {
            progressBar.style.width = "100%";
            status.innerText = "File processed successfully!";
            uploadedFileUrl = data.upload;
            displayFile(data.upload);
            processButton.disabled = false;
        } else {
            status.innerText = "Process failed.";
            progressContainer.style.display = "none"; // Hide progress bar on failure
        }
    })
    .catch(error => {
        clearInterval(interval);
        console.error("Error:", error);
        status.innerText = "Error processing file.";
        progressContainer.style.display = "none"; // Hide progress bar on error
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