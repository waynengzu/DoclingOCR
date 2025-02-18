document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const fileUrl = urlParams.get('file');

    if (fileUrl) {
        displayOriginalFile(fileUrl);
        processFileWithOCR(fileUrl);
    }
});

function displayOriginalFile(fileUrl) {
    const previewImage = document.getElementById('preview');
    const pdfPreview = document.getElementById('pdf-preview');

    if (fileUrl.toLowerCase().endsWith('.pdf')) {
        pdfPreview.src = fileUrl;
        pdfPreview.style.display = "block";
    } else {
        previewImage.src = fileUrl;
        previewImage.style.display = "block";
    }
}

function processFileWithOCR(fileUrl) {
    fetch('http://127.0.0.1:8000/store/OCRs/')
    .then(response => response.json())
    .then(data => {
        if (data.length > 0) {
            // Get the latest OCR entry
            const latestOCR = data[data.length - 1];

            // Display the extracted HTML in the iframe
            const ocrOutput = document.getElementById('ocr-output');
            ocrOutput.src = latestOCR.html;
        } else {
            console.error("No OCR data available.");
        }
    })
    .catch(error => {
        console.error("Error fetching OCR data:", error);
    });
}

function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}