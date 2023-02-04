from django.urls import path
from . import views
app_name = 'cutoff'

urlpatterns = [
    path('',views.round1,name='sem5'),
]
