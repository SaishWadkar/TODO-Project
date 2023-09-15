from django.contrib import admin
from django.urls import path
from note_app import views
urlpatterns = [
    path('',views.index,name="index"),
    path('create',views.create,name="create"),
    path('view',views.view,name="view"),
    path('delete/<id>',views.delete,name="delete"),
    path('update/<id>',views.update,name="update"),
    path('about',views.about,name="about"),

]
