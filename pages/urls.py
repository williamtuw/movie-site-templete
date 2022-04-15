from django.contrib import admin
from django.urls import path
from pages import views as pv

urlpatterns = [

    path(r'<int:page_id>/', pv.page, name='page'),

]
