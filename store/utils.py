import os
import time
import logging
from pathlib import Path
import pandas as pd
from django.core.files import File
from django.core.files.base import ContentFile
from .models import OCR
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
from docling.models.easyocr_model import EasyOcrOptions

_log = logging.getLogger(__name__)


def process_file_with_ocr(upload_instance):
    """
    Processes the uploaded file using the OCR engine and stores the result in the OCR model.
    """
    if not upload_instance.upload:
        return

    input_doc_path = Path(upload_instance.upload.path)  # Get path of uploaded file
    output_dir = Path("media/store/OCRs")  # Ensure directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    pipeline_options = PdfPipelineOptions()
    pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE
    pipeline_options.do_ocr = True
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.do_cell_matching = True
    pipeline_options.generate_page_images = True
    pipeline_options.ocr_options = EasyOcrOptions(lang=['en'], recog_network='fine_tuned_model')

    doc_converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
    )

    start_time = time.time()
    conv_res = doc_converter.convert(input_doc_path)

    # Generate an HTML file
    doc_filename = conv_res.input.file.stem
    element_html_filename = output_dir / f"{doc_filename}-table.html"

    # Save HTML table
    with element_html_filename.open("w") as fp:
        for table in conv_res.document.tables:
            fp.write(table.export_to_html())

    end_time = time.time() - start_time
    _log.info(f"Document converted and tables exported in {end_time:.2f} seconds.")

    # Store the HTML file in the OCR model
    with element_html_filename.open("rb") as html_file:
        ocr_instance = OCR.objects.create(html=File(html_file, name=element_html_filename.name))

    return ocr_instance
