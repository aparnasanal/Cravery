from django.urls import path
from AdminApp import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('view_messages/', views.view_messages, name="view_messages"),

    path('add_restaurant/', views.add_restaurant, name="add_restaurant"),
    path('save_restaurant/', views.save_restaurant, name="save_restaurant"),
    path('view_restaurants/', views.view_restaurants, name="view_restaurants"),
    path('edit_restaurant/<int:rest_id>/', views.edit_restaurant, name="edit_restaurant"),
    path('update_restaurant/<int:rest_id>/', views.update_restaurant, name="update_restaurant"),
    path('delete_restaurant/<int:r_id>/', views.delete_restaurant, name="delete_restaurant"),

    path('add_category/', views.add_category, name="add_category"),
    path('view_categories/', views.view_categories, name="view_categories"),
    path('save_category/', views.save_category, name="save_category"),
    path('edit_category/<int:cat_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:c_id>/', views.delete_category, name="delete_category"),


    path('add_dish/', views.add_dish, name="add_dish"),
    path('view_dishes/', views.view_dishes, name="view_dishes"),
    path('save_dish/', views.save_dish, name="save_dish"),
    path('edit_dish/<int:dish_id>/', views.edit_dish, name="edit_dish"),
    path('update_dish/<int:dish_id>/', views.update_dish, name="update_dish"),
    path('delete_dish/<int:d_id>/', views.delete_dish, name="delete_dish"),

    path('admin_loginpage/', views.admin_loginpage, name="admin_loginpage"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),

]