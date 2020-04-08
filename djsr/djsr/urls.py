from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
]

# React frontend url needs to be included at the end of urlpatterns.
# This way, anything not matching Django URLs will be handled by the
# frontend, which lets us use React’s router to manage frontend views
# while still hosting it on the same server.
# Thus nicely avoiding CORS madness.
urlpatterns += [
    path('', include('frontend.urls'))
]
