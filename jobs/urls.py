from django.urls import path

from . import views

urlpatterns = [
    path("lookahead/3916206", views.qsic_resume, name="qsic_resume"),
    path("lookahead/3916206/letter", views.qsic_letter, name="qsic_letter"),
]
