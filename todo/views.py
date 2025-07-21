from django.shortcuts import render, redirect
from todo.models import AboutPage, CategoryPage, Categories, Product, HomePage
from todo.forms import ContactForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from todo.forms import RegisterForm, LoginForms
from django.db.models import Q


# Create your views here.


def index(request):
    context = {
        "category_page": CategoryPage.objects.last(),
        "categories": Categories.objects.all(),
        "about_page": AboutPage.objects.last(),
        "home_page": HomePage.objects.last(),
    }
    return render(request, "index.html", context)


def about(request):
    context = {"about_page": AboutPage.objects.last()}
    return render(request, "about.html", context)


def categories(request):
    context = {
        "category_page": CategoryPage.objects.last(),
        "categories": Categories.objects.all(),
    }
    return render(request, "categories.html", context)


def contact(request):
    context = {
        "form": ContactForm(),
    }
    return render(request, "contact.html", context)


def faq(requet):
    return render(requet, "faq.html")


def blog(requet):
    return render(requet, "blog-list.html")


def services(requet):
    return render(requet, "services.html")


def contact_message(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "ugula qeyde alindi ")
    return redirect("index")


def projects(requet):
    return render(requet, "projects.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")
    context = {"form": LoginForms()}
    if request.method == "POST":
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["form"] = form
                context["error"] = "Username və ya şifrə yanlişdir."

    return render(request, "login.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    context = {"form": RegisterForm()}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password"]
            user = form.save()
            user.set_password(password)
            user.save()
            messages.success(request, f"{user.username} Uğurla qeydiyyatdan keçdiniz!")
            return redirect("login")
        else:
            context["form"] = form
    return render(request, "register.html", context)


def logout_views(request):
    logout(request)
    return redirect("login")


def search_views(request):
    query = request.GET.get("q")
    print(query)

    context = {
        "products": Product.objects.filter(
            Q(title__icontains=query) | Q(note__icontains=query)
        )
    }
    return render(request, "search.html", context)


# Create your views here.
