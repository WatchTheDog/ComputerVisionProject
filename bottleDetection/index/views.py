from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['searchImage']
        if myfile:
            fs = FileSystemStorage()
            if fs.exists('image.jpg'):
                fs.delete('image.jpg')
            filename = fs.save('image.jpg', myfile)
            uploaded_file_url = fs.url(filename)

            return render(request, 'index/index.html', {
                'uploaded_file_url': uploaded_file_url
            })
    return render(request, 'index/index.html')
