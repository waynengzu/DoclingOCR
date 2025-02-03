from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']

class Document(models.Model):
    DOCUMENT_JSON = 'JSON'
    DOCUMENT_CSV = 'CSV'
    DOCUMENT_TXT = 'TXT'
    DOCUMENT_HTML = 'HTML'
    DOCUMENT_PDF = 'PDF'
    DOCUMENT_PNG = 'PNG'
    DOCUMENT_JPEG = 'JPEG'
    DOCUMENT_JPG = 'JPG'

    DOCUMENT_TYPES = [
        (DOCUMENT_JSON, 'JSON Document'),
        (DOCUMENT_CSV, 'CSV Document'),
        (DOCUMENT_TXT, 'TXT Document'),
        (DOCUMENT_HTML, 'HTML Document'),
        (DOCUMENT_PDF, 'PDF Document'),
        (DOCUMENT_PNG, 'PNG Document'),
        (DOCUMENT_JPEG, 'JPEG Document'),
        (DOCUMENT_JPG, 'JPG Document')
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=DOCUMENT_TYPES)
    path = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.document.name

    class Meta:
        ordering = ['created_at']