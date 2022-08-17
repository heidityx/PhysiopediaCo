from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.displayStartup, name='displayStartup'),
    path('login/', views.displayLogin, name='displayLogin'),
    path('signUp/', views.displaySignUp, name='displaySignUp'),
    path('selections/', views.displaySelection, name='displaySelection'),
    path('selections-HeadNeckShoulder/', views.displaySelectHeadNeckShoulder, name='displaySelectHNS'),
    path('selections-ChestBackWaist/', views.displaySelectChestBackWaist, name='displaySelectCBW'),
    path('selections-ArmsHands/', views.displaySelectArmsHands, name='displaySelectAH'),
    path('selections-Legs/', views.displaySelectLegs, name='displaySelectLegs'),
    path('currentMilestone/', views.displayMilestone, name='displayMilestone'),
    path('log/', views.displayLog, name='displayLog'),
    path('profile-settings/', views.displaySettings, name='displaySettings'),
    path('store/', views.displayStore, name='displayStore'),
    path('legal/', views.displayLegal, name='displayLegal'),
]