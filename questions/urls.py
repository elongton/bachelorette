from django.conf.urls import url
from questions import views

app_name = 'questions'

urlpatterns = [
    url(r'^interface', views.ControlView.as_view(), name="control_panel"),
    url(r'^place/(?P<pk>\d+)/$', views.PlaceDetail.as_view(), name='place_detail'),
    url(r'^place/success/(?P<pk>\d+)/$', views.SuccessView.as_view(), name='success_view'),
    url(r'^place/fail/(?P<pk>\d+)/$', views.FailView.as_view(), name='fail_view'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks_view'),
    url(r'^bonus/$', views.BonusView.as_view(), name='bonus_view'),
]
