from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from .forms import RegisterForm
from .models import SharedFile
from django.contrib import messages
import os
from django.conf import settings


def landing(request):
    return render(request, 'fileshare/landing.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'fileshare/register.html', {'form': form})

@login_required
def upload_view(request):
    if request.method == "POST" and request.FILES.get('file'):
        upfile = request.FILES['file']
        new_file = SharedFile.objects.create(
            file=upfile,
            filename=upfile.name,
            size=upfile.size,
            uploader=request.user
        )
        return render(request, 'fileshare/upload.html', {'success': True})
    return render(request, 'fileshare/upload.html')

@login_required
def delete_file(request, file_id):
    file_obj = get_object_or_404(SharedFile, id=file_id)

    # Delete file from storage
    file_path = file_obj.file.path
    if os.path.exists(file_path):
        os.remove(file_path)

    # Delete from database
    file_obj.delete()
    messages.success(request, "File deleted successfully.")
    return redirect('file_list')


@login_required
def file_list(request):
    files = SharedFile.objects.all().order_by('-upload_date')
    return render(request, 'fileshare/file_list.html', {'files': files})

@login_required
def download_file(request, file_id):
    file_obj = SharedFile.objects.get(id=file_id)
    return FileResponse(file_obj.file.open('rb'), as_attachment=True, filename=file_obj.filename)
