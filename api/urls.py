from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    ...,
    url(r'^rest-auth/', include('rest_auth.urls'))
]