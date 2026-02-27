from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from AdminApp.models import *
from WebApp.models import *


# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")
#_________________________________________________________________________________________________________
def add_restaurant(request):
    return render(request, "add_restaurant.html")

def save_restaurant(request):
    if request.method=="POST":
        r_name = request.POST.get('rname')
        r_place = request.POST.get('rplace')
        r_desc = request.POST.get('rdesc')
        r_img = request.FILES['rimg']

        obj = RestaurantDb(RestaurantName=r_name, RestaurantPlace=r_place,
                           RestDescription=r_desc, RestaurantImage=r_img)
        obj.save()

        return redirect(add_restaurant)

def view_restaurants(request):
    restaurants = RestaurantDb.objects.all()
    return render(request, "view_restaurants.html",
                  {"rest" : restaurants})

def edit_restaurant(request, rest_id):
    restaurants = RestaurantDb.objects.get(id=rest_id)
    return render(request, "edit_restaurant.html",
                  {"rest" : restaurants})

def update_restaurant(request, rest_id):
    if request.method=="POST":
        r_name = request.POST.get('rname')
        r_place = request.POST.get('rplace')
        r_desc = request.POST.get('rdesc')
        try:
            r_img = request.FILES['rimg']
            fs = FileSystemStorage()
            file = fs.save(r_img.name, r_img)
        except MultiValueDictKeyError:
            file = RestaurantDb.objects.get(id=rest_id).RestaurantImage
        RestaurantDb.objects.filter(id=rest_id).update(RestaurantName=r_name, RestaurantPlace=r_place,
                           RestDescription=r_desc, RestaurantImage=file)
        return redirect(view_restaurants)

def delete_restaurant(request, r_id):
    rest = RestaurantDb.objects.get(id=r_id)
    rest.delete()
    return redirect(view_restaurants)

#__________________________________________________________________________________________________________
def add_category(request):
    return render(request, "add_category.html")
def save_category(request):
    if request.method=="POST":
        c_name = request.POST.get('category_name')
        c_desc = request.POST.get('description')
        c_img = request.FILES['category_image']

        obj = CategoryDb(CategoryName=c_name, Description=c_desc, CategoryImage=c_img)
        obj.save()
        return redirect(add_category)

def view_categories(request):
    categories = CategoryDb.objects.all()
    return render(request, "view_categories.html",
                  {"cat" : categories})

def edit_category(request, cat_id):
    cat = CategoryDb.objects.get(id=cat_id)
    return render(request, "edit_category.html",
                  {"cat" : cat})

def update_category(request, cat_id):
    if request.method == "POST":
        c_name = request.POST.get('category_name')
        c_desc = request.POST.get('description')
        try:
            c_img = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(c_img.name, c_img)
        except MultiValueDictKeyError:
            file = CategoryDb.objects.get(id=cat_id).CategoryImage
        CategoryDb.objects.filter(id=cat_id).update(CategoryName=c_name, Description=c_desc,
                                                    CategoryImage=file)
        return redirect(view_categories)

def delete_category(request, c_id):
    cat = CategoryDb.objects.get(id=c_id)
    cat.delete()
    return redirect(view_categories)




#_______________________________________________________________________________________________________
def add_dish(request):
    category = CategoryDb.objects.all()
    restaurant = RestaurantDb.objects.all()
    return render(request, "add_dish.html",
                  {"cat": category,
                            "rest": restaurant})

def save_dish(request):
    if request.method=="POST":
        d_name = request.POST.get('dname')
        c_name = request.POST.get('cname')
        r_name = request.POST.get('rname')
        d_price = request.POST.get('dprice')
        d_desc = request.POST.get('desc')
        d_img = request.FILES.get('dimg')

        obj = DishDb(DishName=d_name, Category_Name=c_name, Restaurant_Name=r_name,
                     DishDescription=d_desc,DishPrice=d_price, DishImage=d_img)
        obj.save()
        return redirect(add_dish)

def view_dishes(request):
    dishes = DishDb.objects.all()
    return render(request, "view_dishes.html",
                  {"dishes" : dishes})

def edit_dish(request, dish_id):
    dish = DishDb.objects.get(id=dish_id)
    category = CategoryDb.objects.all()
    restaurant = RestaurantDb.objects.all()
    return render(request, "edit_dish.html",
                  {"dish" : dish,
                            "cat" : category,
                            "rest" : restaurant})

def update_dish(request, dish_id):
    if request.method=="POST":
        d_name = request.POST.get('dname')
        c_name = request.POST.get('cname')
        r_name = request.POST.get('rname')
        d_desc = request.POST.get('desc')
        d_price = request.POST.get('dprice')
        try:
            d_img = request.FILES['dimg']
            fs = FileSystemStorage()
            file = fs.save(d_img.name, d_img)
        except MultiValueDictKeyError:
            file = DishDb.objects.get(id=dish_id).DishImage
        DishDb.objects.filter(id=dish_id).update(DishName=d_name, Category_Name=c_name, Restaurant_Name=r_name,
                     DishDescription=d_desc,DishPrice=d_price, DishImage=file)
        return redirect(view_dishes)


def delete_dish(request, d_id):
    dish = DishDb.objects.get(id=d_id)
    dish.delete()
    return redirect(view_dishes)

#________________________________________________________________________________________________________

def admin_loginpage(request):
    return render(request, "admin_login.html")
def admin_login(request):
    if request.method=="POST":
        u_name = request.POST.get('username')
        pass_w = request.POST.get('password')

        if User.objects.filter(username__contains=u_name).exists():
            user = authenticate(username=u_name, password=pass_w)
            if user is not None:
                login(request, user)
                request.session['username'] = u_name
                request.session['password'] = pass_w
                return redirect(dashboard)
            else:
                return redirect(admin_loginpage)
        else:
            return redirect(admin_loginpage)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_loginpage)

#____________________________________________________________________________________________________

def view_messages(request):
    message = ContactDb.objects.all()
    return render(request, "view_messages.html",
                  {"msg" : message})

