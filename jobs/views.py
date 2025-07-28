from django.shortcuts import render

def qsic_resume(request):
    context = {"title": "Resume · QSIC · Hamish Murphy"}
    return render(request, "qsic/resume.djhtml", context)

def qsic_letter(request):
    context = {"title": "Letter · QSIC · Hamish Murphy"}
    return render(request, "qsic/letter.djhtml", context)
