from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from .ml import ml


def index(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['searchImage']
        if myfile:
            fs = FileSystemStorage()
            if fs.exists('image.jpg'):
                fs.delete('image.jpg')
            filename = fs.save('image.jpg', myfile)
            isBeerInImage = ml()

            return render(request, 'index/index.html', {
                'result': isBeerInImage
            })
    return render(request, 'index/index.html')
