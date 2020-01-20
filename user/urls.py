from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^registe$',views.registe_view),
    url(r'^login$',views.login_view),
    url(r'^logout$', views.logout_view)
]