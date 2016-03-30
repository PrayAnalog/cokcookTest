# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
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


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chef(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)
    chef_explanation = models.TextField(blank=True, null=True)
    chef_age = models.IntegerField(blank=True, null=True)
    chef_gender = models.CharField(max_length=10, blank=True, null=True)
    chef_image_url = models.CharField(max_length=255, blank=True, null=True)
    house = models.ForeignKey('House', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chef'


class Deliverer(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)
    deliverer_image_url = models.CharField(max_length=255, blank=True, null=True)
    deliverer_phone_number = models.IntegerField(blank=True, null=True)
    deliverer_feeling = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deliverer'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Food(models.Model):
    id = models.BigIntegerField(primary_key=True)
    food_name = models.CharField(max_length=50, blank=True, null=True)
    food_image_url = models.CharField(max_length=255, blank=True, null=True)
    explanation = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    ingredient = models.TextField(blank=True, null=True)
    calorie = models.IntegerField(blank=True, null=True)
    food_area = models.CharField(max_length=50, blank=True, null=True)
    food_state = models.CharField(max_length=50, blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    star_count = models.IntegerField(blank=True, null=True)
    ordered_count = models.IntegerField(blank=True, null=True)
    chef = models.ForeignKey(Chef, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'food'


class House(models.Model):
    id = models.BigIntegerField(primary_key=True)
    house_address = models.CharField(max_length=50, blank=True, null=True)
    house_call_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'house'


class OrderSheet(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cook_list = models.TextField()
    whole_price = models.IntegerField()
    address = models.CharField(max_length=255)
    time_order = models.DateTimeField()
    time_complete = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=5)
    payment_way = models.CharField(max_length=10, blank=True, null=True)
    user_request = models.TextField(blank=True, null=True)
    chef = models.ForeignKey(Chef, models.DO_NOTHING)
    deliverer = models.ForeignKey(Deliverer, models.DO_NOTHING)
    house = models.ForeignKey(House, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order_sheet'


class Review(models.Model):
    id = models.BigIntegerField(primary_key=True)
    text = models.TextField(blank=True, null=True)
    image_url_list = models.CharField(max_length=255, blank=True, null=True)
    stars = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'review'


class Schedule(models.Model):
    id = models.BigIntegerField(primary_key=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    food_limit = models.IntegerField(blank=True, null=True)
    food_count = models.IntegerField(blank=True, null=True)
    chef = models.ForeignKey(Chef, models.DO_NOTHING)
    food = models.ForeignKey(Food, models.DO_NOTHING)
    house = models.ForeignKey(House, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'schedule'


class User(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, primary_key=True)
    login_info = models.TextField(blank=True, null=True)
    log_csv = models.CharField(max_length=255, blank=True, null=True)
    address_list = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    discount = models.TextField(blank=True, null=True)
    postscript = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
