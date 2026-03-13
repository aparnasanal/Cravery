from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('all_food/', views.all_food, name='all_food'),
    path('restaurant_food/<rest_name>/', views.restaurant_food, name='restaurant_food'),
    path('category_food/<cat_name>/', views.category_food, name='category_food'),
    path('single_dish/<int:dish_id>/', views.single_dish, name='single_dish'),

    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('save_message/', views.save_message, name='save_message'),

    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('save_user/', views.save_user, name='save_user'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),

    path('add_to_cart/', views.add_to_cart, name="add_to_cart"),
    path('delete_dish/<int:dish_id>/', views.delete_dish, name="delete_dish"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),

]