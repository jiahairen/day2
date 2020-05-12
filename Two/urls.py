
from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'get_user/', views.get_user),
    url(r'get_usera/', views.get_usera),

]