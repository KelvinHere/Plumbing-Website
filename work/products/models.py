from django.db import models


class BrandManager(models.Manager):
    ''' To allow foreign key from fixtures to find correct brand pk'''
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Brand(models.Model):
    ''' Products Brand with DG plumbing brand code'''
    name = models.CharField(max_length=254, null=True, blank=True, unique=True)
    code = models.CharField(max_length=8, null=True, blank=True)
    objects = BrandManager()

    def __str__(self):
        return self.name


class CategoryManager(models.Manager):
    ''' To allow foreign key from fixtures to find correct category pk'''
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Category(models.Model):
    ''' Category of item, ie Tap, shower, etc... '''
    class Meta:
        verbose_name = "Categorie"

    name = models.CharField(max_length=254, null=True, blank=False, unique=True)
    objects = CategoryManager()

    def __str__(self):
        return f'ID: {str(self.id)} - {self.name}'


class ShopManager(models.Manager):
    ''' To allow foreign key from fixtures to find correct category pk'''
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Shop(models.Model):
    ''' Shop item belongs in ie, Bathroom, Heating, Plumbing '''
    name = models.CharField(max_length=254, null=True, blank=False, unique=True)
    objects = ShopManager()

    def __str__(self):
        return f'{self.name} - ID: {str(self.id)}'


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=False, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.CharField(max_length= 1024, null=True, blank=True)
    active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=1, related_name='brand_name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name='category_name')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, default=1, related_name='shop_name')

    def __str__(self):
        return self.name
