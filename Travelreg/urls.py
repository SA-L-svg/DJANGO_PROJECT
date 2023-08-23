from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Bookingapp import views

urlpatterns = [
    url(r'^student$',views.bookingApi),
    url(r'^student$',views.bookingApi), 
    url(r'^student/([0-9]+)$',views.bookingApi),
    path('admin/', admin.site.urls),
]