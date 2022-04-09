from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name='dhun'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('signup/',views.Signupview.as_view(),name='signup'),
    path('login/',views.Signinview.as_view(),name='signin'),
    path('logout/',views.signout,name='signout'),
    path('myalbums/',views.Myalbum.as_view(),name='myalbum'),
    path('addalbum/',views.Addalbum.as_view(),name='addalbum'),
    path('addsong/',views.Addsong.as_view(),name='addsong'),
    path('playing/<int:pk>',views.Albumplaying.as_view(),name='play'),
    path('all_album/',views.Seeallalbum.as_view(),name='seeallalbum'),
    path('all_songs/',views.Seeallsong.as_view(),name='seeallsongs'),
    path('editsong/<int:pk>',views.Editsong.as_view(),name='editsong'),
    path('editalbum/<int:pk>',views.EditAlbum.as_view(),name='editalbum'),
    path('deletesong/<int:pk>',views.deletesong,name='deletesong'),
    

]