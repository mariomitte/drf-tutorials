from django.urls import path
from django.conf.urls import url

from frontend import views



urlpatterns = [
    path('', views.index_view),      # For the empty url
    url(r'^.*/$', views.index_view)  # All other urls. Regex matches, then lets routing be handled by the frontend. Still needs a / at end.
]
