from django.urls import include, path
from .import views

urlpatterns = [
    path('currentMilestone/', views.displayMilestone, name='displayMilestone'),
]