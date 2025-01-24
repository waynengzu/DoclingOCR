from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Document(models.Model):
    DOCUMENT_JSON = 'JSON'
    DOCUMENT_CSV = 'CSV'
    DOCUMENT_TXT = 'TXT'
    DOCUMENT_HTML = 'HTML'
    DOCUMENT_PDF = 'PDF'

    DOCUMENT_TYPES = [
        (DOCUMENT_JSON, 'JSON Document'),
        (DOCUMENT_CSV, 'CSV Document'),
        (DOCUMENT_TXT, 'TXT Document'),
        (DOCUMENT_HTML, 'HTML Document'),
        (DOCUMENT_PDF, 'PDF Document')
    ]
    name = models.CharField(max_length=255)
    original_type = models.CharField(max_length=255, choices=DOCUMENT_TYPES)
    converted_type = models.CharField(max_length=255, choices=DOCUMENT_TYPES)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE
    )