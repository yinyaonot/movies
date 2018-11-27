
from django.contrib.auth.models import AbstractUser
from django.db import models


class CateLog(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_cate_log'


class Decade(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_decade'


class Film(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cata_log_name = models.CharField(max_length=255)
    cata_log = models.ForeignKey(CateLog, models.DO_NOTHING, blank=True, null=True)
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc = models.ForeignKey('Loc', models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.ForeignKey('Decade', models.DO_NOTHING, db_column='on_decade', blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class = models.ForeignKey('SubClass', models.DO_NOTHING, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_film'


class Level(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_level'


class Loc(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_loc'


class Raty(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    en_time = models.CharField(max_length=255, blank=True, null=True)
    film = models.ForeignKey(Film, models.DO_NOTHING, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_raty'


class Res(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    episodes = models.IntegerField()
    is_use = models.IntegerField()
    link = models.TextField(blank=True, null=True)
    link_type = models.CharField(max_length=255, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    film = models.ForeignKey(Film, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_res'


class SubClass(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    catalog = models.ForeignKey(CateLog, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_subclass'


class Type(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    is_use = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    subclass = models.ForeignKey(SubClass, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_type'





class VipCode(models.Model):
    id = models.CharField(primary_key=True, max_length=225)
    code = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    expire_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 't_vipcode'
