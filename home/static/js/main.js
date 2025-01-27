const fileInput = document.getElementById('fileInput');
const preview = document.getElementById('preview');
const imagePreview = document.getElementById('imagePreview');

// Event listener for file input
fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const fileData = e.target.result; // Base64 string
            localStorage.setItem('uploadedFileData', fileData); // Save to localStorage
            localStorage.setItem('uploadedFileType', file.type); // Save the file type

            if (file.type === 'application/pdf' || file.type === 'text/csv') {
                imagePreview.style.display = 'none';
                preview.style.display = 'block';
                preview.src = fileData; // Load base64 data in iframe
            } else if (file.type.startsWith('image/')) {
                preview.style.display = 'none';
                imagePreview.style.display = 'block';
                imagePreview.src = fileData; // Load base64 image
            } else {
                alert('Unsupported file type.');
            }
        };
        reader.readAsDataURL(file); // Convert file to base64
    }
});

// Navigate to the next page
function goToNextPage() {
    window.location.href = 'processed/'; // Replace with the actual HTML file path
}