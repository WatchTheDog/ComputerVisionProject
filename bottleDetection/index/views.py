from django.http import HttpResponse
from django.shortcuts import render
from .forms import *


# Create your views here.
def search_image_view(request):
    if request.method == 'POST':
        form = SearchImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = SearchImageForm()
    return render(request, 'index.html', {'form': form})


def index(request):
    return render(request, 'index/index.html', {})
