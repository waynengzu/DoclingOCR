const preview = document.getElementById('preview');
const imagePreview = document.getElementById('imagePreview');

// Retrieve file data from localStorage
const fileData = localStorage.getItem('uploadedFileData');
const fileType = localStorage.getItem('uploadedFileType');

if (fileData && fileType) {
    if (fileType === 'application/pdf' || fileType === 'text/csv') {
        imagePreview.style.display = 'none';
        preview.style.display = 'block';
        preview.src = fileData;
    } else if (fileType.startsWith('image/')) {
        preview.style.display = 'none';
        imagePreview.style.display = 'block';
        imagePreview.src = fileData;
    }
} else {
    alert('No uploaded file found! Redirecting back.');
    window.location.href = '/'; // Redirect to the first page
}

// Back button functionality
const backButton = document.getElementById('backButton');
backButton.addEventListener('click', () => {
    window.location.href = '/home/page/'; // Replace with the actual path to the first page
});

