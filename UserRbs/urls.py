from django.conf.urls import url
from UserRbs import views

app_name = 'UserRbs'

urlpatterns = [
    url(r'^$', views.signIn)
]