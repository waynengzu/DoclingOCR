from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Upload, OCR

@receiver(post_save, sender=Upload)
def create_ocr_entry(sender, instance, created, **kwargs):
    if created:  # Ensures this runs only when a new file is uploaded
        OCR.objects.create(html=instance.upload)  # Copy file to OCR model
