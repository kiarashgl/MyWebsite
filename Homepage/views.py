from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')

def Research(request):
    return render(request, 'research.html')
