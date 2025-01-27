const fileInput = document.getElementById('fileInput');
const preview = document.getElementById('preview');
const imagePreview = document.getElementById('imagePreview');

fileInput.addEventListener('change', (event) => {
    const file = event.target.files[0];
    if (file) {
        const url = URL.createObjectURL(file);
        if (file.type === 'application/pdf' || file.type === 'text/csv') {
            imagePreview.style.display = 'none';
            preview.style.display = 'block';
            preview.src = url;
        } else if (file.type.startsWith('image/')) {
            preview.style.display = 'none';
            imagePreview.style.display = 'block';
            imagePreview.src = url;
        } else {
            alert('Unsupported file type.');
        }
    }
});

function goToNextPage() {
    window.location.href = 'processed/'; // Replace with the actual HTML file path
}