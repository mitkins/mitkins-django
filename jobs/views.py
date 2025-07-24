from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Mitkins. You're at the jobs index.")
