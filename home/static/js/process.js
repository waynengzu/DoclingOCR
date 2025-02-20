document.addEventListener('DOMContentLoaded', function () {
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

function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
}