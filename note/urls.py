from django.conf.urls import url
from dwebsocket.middleware import WebSocketMiddleware

from . import views
urlpatterns = [
    url(r'^index$',views.index_view),
    url(r'^add$', views.add_view),
    url(r'^list$', views.list_view),

]
