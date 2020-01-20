from django.conf.urls import url

from bookstore import views

urlpatterns = [
    url(r'^index$',views.index_view,name='book_index'),
    url(r'^sendemail$', views.sendemail_view),

]