from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.

def display_index(request):
    return render(request, 'index.html')

def display_process(request):
    return render(request, 'process.html')

def display_analyze(request):
    return render(request, 'analyze.html')

def get_latest_json(request):
    """Fetch the most recent JSON file from /media/store/OCRs/"""
    directory = os.path.join(settings.MEDIA_ROOT, 'store', 'OCRs')

    if not os.path.exists(directory):
        return JsonResponse({'error': 'Directory not found'}, status=404)

    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    if not json_files:
        return JsonResponse({'error': 'No JSON files found'}, status=404)

    # Get the most recent file by modification time
    latest_file = max(json_files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))

    latest_file_path = os.path.join(directory, latest_file)

    # Load JSON content
    with open(latest_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return JsonResponse({'filename': latest_file, 'data': data})

@csrf_exempt  # Only for testing, use CSRF token properly in production
def save_json(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            filename = data.get("filename")  # Get the original filename
            updated_data = data.get("data")  # Get the modified JSON

            if not filename:
                return JsonResponse({"error": "Filename not provided"}, status=400)

            file_path = os.path.join(settings.MEDIA_ROOT, "store", "OCRs", filename)

            if not os.path.exists(file_path):
                return JsonResponse({"error": "File not found"}, status=404)

            # Save the updated JSON back to the original file
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(updated_data, file, indent=4)

            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
