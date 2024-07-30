"""
URL configuration for board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
# from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # articles로 시작되는 경로는 모두 articles/urls.py로 넘겨주기.
    # board/urls.py를 거쳐서 article/urls.py로 넘어감.
    # url들이 너무 많이 쌓여 유지보수가 어려워지는 것을 방지
    # url 패턴을 묶는 작업
    path('articles/', include('articles.urls'))
]
