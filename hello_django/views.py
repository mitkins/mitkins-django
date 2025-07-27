from django.shortcuts import render

def index(request):
    context = {"title": "mitkins · Hamish Murphy"}
    return render(request, "home/index.djhtml", context)

def custom_404(request, exception):
    context = {"title": "Not Found · Hamish Murphy"}
    return render(request, "404.djhtml", context, status=404)
