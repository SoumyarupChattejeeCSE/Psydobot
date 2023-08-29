from django.urls import path
from django.contrib import admin

from prediction import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login_1/',views.login_1, name='login_1'),
    path('signup',views.signup, name='signup'),
    path('admin/',admin.site.urls),
    path('home/',views.home,name='home'),
    path('stress/',views.stress,name='stress'),
    path('low_stress/',views.lowstress,name='low_stress'),
    path('high_stress/',views.highstress,name='high_stress'),
    path('moderate_stress/',views.moderatestress,name='moderate_stress'),
    path('map/',views.map,name='map'),
]