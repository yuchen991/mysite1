"""mysite1 URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^page1$',views.page1_view),
    url(r'^page(/d+)$',views.pagen_view),
    url(r'^login$',views.login_view),
    # url(r'^index$', views.index_view),
    url(r'^test_html$', views.test_view),
    url(r'^test_if$', views.test_if),
    url(r'^test_static$',views.test_static),
    url(r'^set_cookies$',views.set_cookies),
    url(r'^user/',include('user.urls')),
    url(r'^note/', include('note.urls')),
    url(r'^testmiddle$',views.test_middle),
    url(r'^test/$',views.test),
    url(r'^test_load$',views.test_load),
    url(r'^make_csv$', views.make_csv,name='make_csv'),
    url(r'^bookstore/',include('bookstore.urls')),
]
