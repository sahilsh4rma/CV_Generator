from django.urls import path
from . import views
app_name = 'pdf'

urlpatterns =[
    path('',views.accept,name='accept'),
    path('<int:id>/',views.resume,name='resume'),
    path('profile_list/',views.list,name='profile_list'),
]