from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('registration/', include('rest_auth.urls'))
]