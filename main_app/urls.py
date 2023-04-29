from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:city_id>/", views.detail, name="detail"),
    path("create/", views.NewTrip.as_view(), name="new_trip"),
    path("<int:pk>/update/", views.UpdateTrip.as_view(), name="update_trip"),
    path("<int:pk>/delete/", views.DeleteTrip.as_view(), name="delete_trip"),
    path('accounts/signup/', views.signup, name='signup'),
    path("users/", views.allusers, name="allusers"),
    path("<int:city_id>/add_photo/", views.add_photo, name="add_photo"),
    path("users/<int:user_id>/", views.userprofile, name="userprofile"),
    path("users/<int:user_id>/addfriend", views.add_friend, name="add_friend"),
]