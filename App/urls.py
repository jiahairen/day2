from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'addpersons/', views.add_persons),
    url(r'get_persons',views.get_persons),
    url(r'get_exclude',views.get_exclude),
    url(r'^add_person',views.add_person),
]
