from django.conf.urls import url

from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'devices'
urlpatterns = [
    url(r'^$', csrf_exempt(views.IndexView.as_view()), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', csrf_exempt(views.DetailView.as_view()), name='detail'),
    url(r'^recognition$', csrf_exempt(views.RecognitionView.as_view()), name='recognition'),
    url(r'^create$', csrf_exempt(views.CreateView.as_view()), name='create'),
    url(r'^update$', csrf_exempt(views.UpdateView.as_view()), name='update'),
    url(r'^data$', csrf_exempt(views.DeviceMacDataView.as_view()), name='data_device_mac'),
    url(r'^task$', csrf_exempt(views.DeviceMacTaskView.as_view()), name='task_device_mac'),
    url(r'^(?P<pk>[0-9]+)/data$', csrf_exempt(views.DeviceDataView.as_view()), name='data'),
    url(r'^(?P<pk>[0-9]+)/tasks$', csrf_exempt(views.DeviceTaskView.as_view()), name='task'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/$', csrf_exempt(views.DeviceDataDayView.as_view()), name='device_data_day'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<month>\d{2})/(?P<year>\d{4})/$', csrf_exempt(views.DeviceDataMonthView.as_view()), name='device_data_month'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<day1>\d{2})/(?P<month1>\d{2})/(?P<year1>\d{4})/(?P<day2>\d{2})/(?P<month2>\d{2})/(?P<year2>\d{4})/$', csrf_exempt(views.DeviceDataBetweenDaysView.as_view()), name='device_data_between_days'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})/(?P<hour>\d{2})/$', csrf_exempt(views.DeviceDataHourView.as_view()), name='device_data_hour'),
    url(r'^(?P<pk>[0-9]+)/data/(?P<day1>\d{2})/(?P<month1>\d{2})/(?P<year1>\d{4})/(?P<hour1>\d{2})/(?P<day2>\d{2})/(?P<month2>\d{2})/(?P<year2>\d{4})/(?P<hour2>\d{2})/$', csrf_exempt(views.DeviceDataBetweenHoursView.as_view()), name='device_data_between_hours'),
]
