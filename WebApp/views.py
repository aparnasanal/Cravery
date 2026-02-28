from django.shortcuts import render, redirect
from django.contrib import messages


from AdminApp.models import *
from WebApp.models import *

# Create your views here.

def homepage(request):
    restaurant = RestaurantDb.objects.all()
    category = CategoryDb.objects.all()
    selected_dish = DishDb.objects.order_by('-id')[:2]
    selected_dish1 = DishDb.objects.order_by('-id')[:8]
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "home.html",
                  {"rest" : restaurant,
                            "cat" : category,
                            "sel_dish" : selected_dish,
                            "sel_dish1" : selected_dish1,
                            "count" : count})

def all_food(request):
    food = DishDb.objects.all()
    category = CategoryDb.objects.all()
    restaurant = RestaurantDb.objects.all()
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "all_food.html",
                  {"food" : food,
                            "cat" : category,
                            "restaurant": restaurant,
                            "count" : count})

def restaurant_food(request, rest_name):
    rest_food = DishDb.objects.filter(Restaurant_Name=rest_name)
    category = CategoryDb.objects.all()
    restaurant = RestaurantDb.objects.all()
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "restaurant_food.html",
                  {"rest": rest_food,
                            "category" : category,
                           "restaurant": restaurant,
                            "count" : count})

def category_food(request, cat_name):
    cat_food = DishDb.objects.filter(Category_Name=cat_name)
    category = CategoryDb.objects.all()
    restaurant = RestaurantDb.objects.all()
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "category_food.html",
                  {"cat" : cat_food,
                            "category" : category,
                            "restaurant" : restaurant,
                            "count" : count})

def single_dish(request, dish_id):
    dish = DishDb.objects.get(id=dish_id)
    restaurant = RestaurantDb.objects.all()
    fav_dishes = DishDb.objects.order_by('-id')[5:10]
    category = CategoryDb.objects.all()
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "single_dish.html",
                  {"dish" : dish,
                            "restaurant" : restaurant,
                            "fav" : fav_dishes,
                            "category" : category,
                            "count" : count})
#_________________________________________________________________________________________________

def services(request):
    uname = request.session.get('Username')
    categories = CategoryDb.objects.all()
    restaurants = RestaurantDb.objects.all()
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "services.html",
                                {"count" : count,
                                        "cat" : categories,
                                        "rest" : restaurants})

def contact(request):
    category = CategoryDb.objects.all()
    uname = request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    return render(request, "contact.html",
                  {"cat" : category,
                            "count" : count})

def save_message(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        msg = request.POST.get('msg')

        obj = ContactDb(Name=name, Email=email, Subject=sub, Message=msg)
        obj.save()
        return redirect(contact)


#__________________________________________________________________________________________________________

def signin(request):
    return render(request, "signin.html")
def signup(request):
    return render(request, "signup.html")

def save_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        c_password = request.POST.get('password2')

        obj = RegistrationDb(Username=username, Email=email, Password=password, C_Password=c_password)
        if RegistrationDb.objects.filter(Username=username).exists():
            messages.warning(request, "Username Already Exists")
            return redirect(signup)
        elif RegistrationDb.objects.filter(Email=email).exists():
            messages.warning(request, "Email Already Exists")
            return redirect(signup)
        else:
            obj.save()
            return redirect(signin)

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        pswd=request.POST.get('password')

        if RegistrationDb.objects.filter(Username=uname, Password=pswd).exists():
            request.session['Username'] = uname
            request.session['Password'] = pswd
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(signin)
    else:
        return redirect(signin)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(signin)

#______________________________________________________________________________________________________________

def add_to_cart(request):
    if request.method=="POST":
        uname = request.POST.get('uname')
        dname = request.POST.get('dname')
        rname = request.POST.get('rname')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        total = request.POST.get('totalprice')
        pro = DishDb.objects.filter(DishName=dname).first()
        img = pro.DishImage if pro else None
        obj = CartDb(Username=uname, Restaurant=rname,  Dish_Name=dname, Price=price,
                     Quantity=quantity, Total_Price=total, Dish_Image=img)
        obj.save()

        return redirect(cart)

def cart(request):
    foods = CartDb.objects.filter(Username=request.session['Username'])
    categories = CategoryDb.objects.all()
    restaurants = RestaurantDb.objects.all()
    uname =request.session.get('Username')
    count = 0
    if uname:
        count = CartDb.objects.filter(Username=uname).count()
    sub_total = 0
    delivery = 0
    grand_total = 0

    for i in foods:
        sub_total += i.Total_Price
        if sub_total > 500:
            delivery = 0
        elif sub_total > 400:
            delivery = 50
        else:
            delivery = 100
        grand_total = sub_total + delivery

    return render(request, "cart.html",
                  {"foods" : foods,
                            "cat" : categories,
                            "rest" : restaurants,
                            "count" : count,
                            "delivery" : delivery,
                            "sub_total" : sub_total,
                            "grand_total" : grand_total,})

def delete_dish(request, dish_id):
    dish = CartDb.objects.get(id=dish_id)
    dish.delete()
    return redirect(cart)