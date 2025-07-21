from django.urls import path
from todo.views import (
    index,
    categories,
    contact,
    about,
    contact_message,
    blog,
    faq,
    login_view,
    register,
    logout_views,
    search_views,
    faq,
    services,
    projects,
    blog,
    contact,
)


urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("categories/", categories, name="categories"),
    path("contact/", contact, name="contact"),
    path("contact_message/", contact_message, name="contact_message"),
    path("blog/", blog, name="blog"),
    path("logout/", logout_views, name="logout"),
    path("search/", search_views, name="search_views"),
    path("faq/", faq, name="faq"),
    path("services/", services, name="services"),
    path("projects/", projects, name="projects"),
]
