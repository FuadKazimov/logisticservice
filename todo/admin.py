from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from todo.models import (
    AboutPage,
    CategoryPage,
    Categories,
    Contact,
    SiteSettings,
    Author,
    Product,
    ProductImage,
    HomePage,
)

# Register your models here.
admin.site.register(AboutPage)
admin.site.register(CategoryPage)
admin.site.register(Categories)
admin.site.register(Contact)
admin.site.register(SiteSettings)
admin.site.register(Author)
admin.site.register(HomePage)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "note"]
    inlines = [ProductImageInline]


# Register your models here.
