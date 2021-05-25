from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.login,name='home'),
    path('signup/',views.signup,name='signup'),
    path('createEvent/',views.createEvent,name='createEvent'),
    path('UserProfile/', views.UserProfile, name='UserProfile'),
 #  path('bfh2pageorg', views.bfh2pageorg, name='bfh2page'),
    path('upcomingorg/<int:pk>',views.showEvent , name='upcomingorg'),
    #url(r'^createEvent$',views.createEvent,name='createEvent'),
    path('Eventgenerator/',views.createEvent , name='Eventgenerator'),
    path('',views.logout , name='logout'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)