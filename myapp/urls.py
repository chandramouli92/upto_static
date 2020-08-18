from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name="base"),
    path('home/',views.home,name="home"),
    path('profile/',views.profile,name="profile"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multi,name="multi"),
    path('img_upld/',views.img_upld,name='img_upld'),
    path('image_display/',views.image_display,name='image_display'),
    path('builtin/',views.builtinforms,name="builtinforms")
    
]
