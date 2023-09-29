from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
#from .models import Product, Brand, Catagory
from django.contrib.auth import login
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

"""
def home(request):
    products = Product.objects.all()
    catagories = Catagory.objects.all()
    recent_product = Product.objects.latest("id")
    context = {
        "products": products,
        "catagories": catagories,
        "recent_product": recent_product,

    }

    return render(request, "brand.html", context=context)


def single_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, "single_product.html", {"product": product})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, "index.html")
        else:
            print("invalid data")
            messages.info(request, "invalid")
            return render(request, "login.html")
    else:
        return render(request, "login.html")


def new_product(request):
    if request.user.username == "tegegn":
        pass
      
        if request.method == "POST":
            title = request.POST["title"]
            slug = request.POST["slug"]
            price = request.POST["price"]
            description = request.POST["description"]
            stock = request.POST["stock"]
            catagory = Catagory.objects.get(id=1)
            brand = Brand.objects.get(id=1)
            user = request.user

            Product.objects.create(
                user=user,
                title=title,
                slug=slug,
                price=price,
                description=description,
                stock=stock,
                brand=brand,
                catagory=catagory,
            )

           Brand.objects.create(name=name, slug=name)
            messages.info(request, f"succussfuly created for {name} - {slug}")

            name = "pro max"
            Brand.objects.create(name=name, slug=name)
            print(Brand.objects.all)
            return HttpResponse(Brand.objects.all)
    else:
        return HttpResponse("only allowed allowed for fikadu")

    return render(request, "create.html")


def catagory_view(request):
    catagories_view = Catagory.objects.all()

    return render(request, "tparts/catagory.html", {"catagories": catagories_view})


def hero(request):
    categories = [
        {"name": "Phones", "image": "images/elec-4.png"},
        {"name": "Computers", "image": "images/elec-5.png"},
        {"name": "Accessories", "image": "images/elec-11.png"},
        # Add more categories as needed
    ]
    # return render(request, 'your_template.html',)
    return render(request, "hero.html", {"categories": categories})
  """