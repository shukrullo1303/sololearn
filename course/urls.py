from django.urls import path
from . import views

urlpatterns = [
    path("lesson/<str:url_name>/<int:pk>/<int:pk2>/", views.lesson, name="complete_page"),
    path("check_answer/<int:pk>/<int:pk2>/", views.check_answer, name="check_answer"),
    path("check_input/<int:pk>/", views.check_input, name="check_input"),
    path("<str:url_name>/", views.coursehome, name="course"),
    # path("<str:url_name>/<int:pk>/<int:pk2>/", views.lesson, name="lesson"),
    path('certificate/<int:pk>', views.get_certificate, name="get_certificate"),

]

