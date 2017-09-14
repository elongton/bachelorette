from django.conf.urls import url
from questions import views

app_name = 'questions'

urlpatterns = [
    url(r'^interface', views.ControlView.as_view(), name="control_panel"),
    url(r'^place/(?P<pk>\d+)/$', views.PlaceDetail.as_view(), name='place_detail'),
]
