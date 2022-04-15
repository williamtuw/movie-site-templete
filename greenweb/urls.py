"""greenweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from pages import views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path(r'', pv.home, name="home"),
    path(r'delopy/', pv.getDelopyPage, name='delopy'),


    path(r'<int:video_id>.html', pv.getPlayHtml, name="play_html"),
    path(r'register/', pv.register, name="register"),
    path(r'login/', pv.login, name="login"),
    path(r'logout/', pv.logout, name="logout"),

    path(r"user/<str:tab>", pv.user, name="user"),
]

