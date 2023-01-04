from django.contrib import admin
from django.urls import path, include
from studentApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/',StudentListView.as_view(), name="student"),
    path('',include('studentApp.urls')),
]
