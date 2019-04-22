"""dj01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #定义访问路径：http://xxx/01-show
    url(r'^01-show/$',views.show_vie),
    url(r'^login/$',views.show_vie),
    url(r'^register/$',views.show_vie),

    url(r'^02-url/(\d{4})/$',views.show_url),

    url(r'^03-url/(\d{4})/(\d{2})/(\d{2})/$',views.show_int),
    url(r'^04-url/(\S{2,})/(\d{2})/$',views.show_name),
]