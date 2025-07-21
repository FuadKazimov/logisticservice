from django.db import models

# Create your models here.


class AboutPage(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return "{}".format(self.tittle)

    class Meta:
        verbose_name_plural = "About Page"


class CategoryPage(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.tittle)

    class Meta:
        verbose_name_plural = "Category Page"


class Categories(models.Model):
    tittle = models.CharField(max_length=50)
    images = models.ImageField(upload_to="images/", null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.tittle)

    class Meta:
        verbose_name_plural = "Categories"


class HomePage(models.Model):
    title = models.CharField(max_length=50)
    images = models.ImageField(upload_to="home/", null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.title)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.name)


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True)
    logo_navbar = models.FileField(
        upload_to="todo/site_settings", null=True, blank=True
    )

    logo_navbar_alt_data = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Add data for increasing SEO performance",
    )

    logo_footer = models.FileField(
        upload_to="todo/site_settings", null=True, blank=True
    )

    logo_footer_alt_data = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Add data for increasing SEO performance",
    )

    favicon = models.FileField(upload_to="todo/site_settings", null=True, blank=True)
    favicon_alt_data = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Add data for increasing SEO performance",
    )

    address = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=17, decimal_places=15, null=True, blank=True
    )
    latitude = models.DecimalField(
        max_digits=17, decimal_places=15, null=True, blank=True
    )
    iframe = models.TextField(
        help_text="Just paste iframe src data from googlemap", null=True, blank=True
    )
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Enter phone number starting with the code",
    )

    fax = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Enter fax number starting with the code",
    )

    facebook = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your facebook url"
    )
    instagram = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your instagram url"
    )
    twitter = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your twitter url"
    )
    linkedin = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your linkedin url"
    )
    youtube = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your youtube url"
    )
    website = models.URLField(
        max_length=255, null=True, blank=True, help_text="Enter your website url"
    )

    def _str_(self):
        return self.company_name

    class Meta:
        verbose_name_plural = "Site Settings"


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories)
    price = models.FloatField(default=1)
    currency = models.CharField(max_length=3, default="AZN")
    note = models.TextField()

    def __str__(self):
        return "{}".format(self.title)


class ProductImage(models.Model):
    image = models.ImageField(upload_to="book/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image.name)


# Create your models here.
