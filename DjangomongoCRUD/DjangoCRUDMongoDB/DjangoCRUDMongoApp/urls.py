from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/',admin.site.urls) ,
    path('add_post/',views.add_post) ,
    path('update_post/<str:id>',views.update_post) ,
    path('delete_post/<str:id>',views.delete_post) ,
    path('read_one_post/<str:id>',views.read_one_post) ,
    path('read_all_post/',views.read_all_post) ,
]
