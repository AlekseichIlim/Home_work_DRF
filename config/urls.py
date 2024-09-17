
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('school/', include('school.urls', namespace='school')),
    path('users/', include('users.urls', namespace='users')),

]
