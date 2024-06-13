from django.shortcuts import render, get_object_or_404
from sample.models import Sample

def index(request):
    context = {'samples': Sample.objects.all()}
    return render(request, 'index.html', context)

def post(request, pk):
    post = get_object_or_404(Sample, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post.html', context)
