from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    
]
