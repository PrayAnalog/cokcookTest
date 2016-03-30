# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class AuthUser(models.Model):
	id = models.IntegerField(primary_key=True)
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	is_superuser = models.IntegerField()
	username = models.CharField(unique=True, max_length=30)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	is_staff = models.IntegerField()
	is_active = models.IntegerField()
	date_joined = models.DateTimeField()

	class Meta:
		managed = False
		db_table = 'auth_user'

class Chef(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    explanation = models.TextField(db_column='explanation', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='image_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    house = models.ForeignKey('homepage.House', related_name='chef', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'chef'


class Deliverer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    deliverer_image_url = models.CharField(db_column='deliverer_image_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deliverer_phone_number = models.IntegerField(db_column='deliverer_phone_number', blank=True, null=True)  # Field name made lowercase.
    deliverer_feeling = models.TextField(db_column='deliverer_feeling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'deliverer'


class Food(models.Model):
    id = models.AutoField(primary_key=True)
    chef = models.ForeignKey('homepage.Chef', related_name='food_chef', on_delete=models.CASCADE)
    name = models.CharField(db_column='name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='image_url', max_length=255, blank=True, null=True)  # Field name made lowercase.
    explanation = models.TextField(db_column='explanation', max_length=1024)
    price = models.IntegerField(db_column='price', blank=True, null=True)
    ingredient = models.TextField(blank=True, null=True)
    calorie = models.IntegerField(blank=True, null=True)
    area = models.CharField(db_column='area', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='state', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stars = models.FloatField(blank=True, null=True)
    star_count = models.IntegerField(blank=True, null=True)
    ordered_count = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

    def get_chef_image_url(self):
		return get_object_or_404(Chef, user=self.chef).image_url

    def get_chef_name(self):
		return get_object_or_404(Chef, user=self.chef).user.first_name

    class Meta:
        db_table = 'food'


class House(models.Model):
    id = models.BigIntegerField(primary_key=True)
    address = models.CharField(db_column='address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    call_number = models.IntegerField(db_column='call_number', blank=True, null=True)  # Field name made lowercase.

    class Meta:
       db_table = 'house'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey('homepage.Consumer', related_name='order_user', on_delete=models.CASCADE)
    house = models.ForeignKey('homepage.House', related_name='order_house', on_delete=models.CASCADE)
    chef = models.ForeignKey('homepage.Chef', related_name='order_chef', on_delete=models.CASCADE)
    deliverer = models.ForeignKey('homepage.Deliverer', related_name='order_deliverer', on_delete=models.CASCADE)
    cook_list = models.TextField(db_column='cook_list')  # Field name made lowercase.
    whole_price = models.IntegerField()  # Field name made lowercase.
    address = models.CharField(max_length=255)  # Field name made lowercase.
    time_order = models.DateTimeField()  # Field name made lowercase.
    time_complete = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=5)  # Field name made lowercase.
    payment_way = models.CharField(max_length=10, blank=True, null=True)  # Field name made lowercase.
    consumer_request = models.TextField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
       db_table = 'order'


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    consumer = models.ForeignKey('homepage.Consumer', related_name='review_user', on_delete=models.CASCADE)
    food = models.ForeignKey('homepage.Food', related_name='review_food', on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)  # Field name made lowercase.
    image_url_list = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    stars = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
       db_table = 'review'


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    house = models.ForeignKey('homepage.House', related_name='schedule_house', on_delete=models.CASCADE)
    chef = models.ForeignKey('homepage.Chef', related_name='schedule_chef', on_delete=models.CASCADE)
    food = models.ForeignKey('homepage.Food', related_name='schedule_food', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    end_datetime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    food_limit = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    food_count = models.IntegerField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
       db_table = 'schedule'


class Consumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    login_info = models.TextField(blank=True, null=True)  # Field name made lowercase.
    log_csv_url = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    address_list = models.TextField(blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(blank=True, null=True)
    discount = models.TextField(blank=True, null=True)
    postscript = models.TextField(blank=True, null=True)

    class Meta:
       db_table = 'consumer'
