from django.urls import path
from lolz2 import views
app_name = 'lolz2'
urlpatterns = [
    path('', views.home, name='home'),
    path('one/', views.file_one, name='file1'),
    path('two/', views.file_two, name='file2'),
    path('login/', views.form_one, name='form1'),
    path('result/', views.result, name='result'),
]
