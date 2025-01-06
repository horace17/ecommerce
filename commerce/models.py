from django.db import models

# Create your models here.
class Slider(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_button = models.CharField(max_length=100)
    slider_image = models.ImageField(upload_to='slides/')

    def __str__(self):
        return self.slider_title

class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = models.TextField(max_length=500)

    def __str__(self):
        return self.service_title

class Mobile(models.Model):
    mobile_button = models.CharField(max_length=100)
    mobile_image = models.ImageField(upload_to='mobiles/')
    mobile_type = models.CharField(max_length=100)
    mobile_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.mobile_button

class Watch(models.Model):
    watch_button = models.CharField(max_length=100)
    watch_image = models.ImageField(upload_to='mobiles/')
    watch_type = models.CharField(max_length=100)
    watch_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.watch_button

class Yearly(models.Model):
    yearly_discount = models.CharField(max_length=100)
    yearly_heading = models.TextField(max_length=500)
    yearly_button = models.CharField(max_length=100)

    def __str__(self):
        return self.yearly_discount

class Latest(models.Model):
    latest_image = models.ImageField(upload_to='latests/')
    latest_date = models.DateField()
    latest_item = models.CharField(max_length=100)
    latest_description = models.TextField(max_length=500)

    def __str__(self):
        return self.latest_item


class Testimonial(models.Model):
    testimonial_description = models.TextField(max_length=500)
    testimonial_author = models.CharField(max_length=100)

    def __str__(self):
        return self.testimonial_description

class Subscription(models.Model):
    subscription_title = models.CharField(max_length=100)
    subscription_description = models.TextField(max_length=500)
    subscription_button = models.CharField(max_length=100)

    def __str__(self):
        return self.subscription_title

class Insta(models.Model):
    insta_image = models.ImageField(upload_to='insta/')

