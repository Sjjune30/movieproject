from django.conf.urls.static import static
from django.urls import path

from HomeApp import views
from MovieProject import settings

app_name = 'HomeApp'

urlpatterns = [
    path('',views.home, name='home'),
    path('movie/<int:movie_id>/',views.details, name='details'),
    path('add/',views.add_data,name= 'add_data'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),

]
