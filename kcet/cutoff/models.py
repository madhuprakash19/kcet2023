from django.db import models

# Create your models here.
class EngGenRound1(models.Model):
    college = models.CharField(db_column='College', max_length=200)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100)  # Field name made lowercase.
    number_1g = models.IntegerField(db_column='1G')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1k = models.IntegerField(db_column='1K')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1r = models.IntegerField(db_column='1R')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ag = models.IntegerField(db_column='2AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ak = models.IntegerField(db_column='2AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ar = models.IntegerField(db_column='2AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bg = models.IntegerField(db_column='2BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bk = models.IntegerField(db_column='2BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2br = models.IntegerField(db_column='2BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ag = models.IntegerField(db_column='3AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ak = models.IntegerField(db_column='3AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ar = models.IntegerField(db_column='3AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bg = models.IntegerField(db_column='3BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bk = models.IntegerField(db_column='3BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3br = models.IntegerField(db_column='3BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    gm = models.IntegerField(db_column='GM')  # Field name made lowercase.
    gmk = models.IntegerField(db_column='GMK')  # Field name made lowercase.
    gmr = models.IntegerField(db_column='GMR')  # Field name made lowercase.
    scg = models.IntegerField(db_column='SCG')  # Field name made lowercase.
    sck = models.IntegerField(db_column='SCK')  # Field name made lowercase.
    scr = models.IntegerField(db_column='SCR')  # Field name made lowercase.
    stg = models.IntegerField(db_column='STG')  # Field name made lowercase.
    stk = models.IntegerField(db_column='STK')  # Field name made lowercase.
    str = models.IntegerField(db_column='STR')  # Field name made lowercase.


class EngGenRound2(models.Model):
    college = models.CharField(db_column='College', max_length=200)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100)  # Field name made lowercase.
    number_1g = models.IntegerField(db_column='1G')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1k = models.IntegerField(db_column='1K')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1r = models.IntegerField(db_column='1R')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ag = models.IntegerField(db_column='2AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ak = models.IntegerField(db_column='2AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ar = models.IntegerField(db_column='2AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bg = models.IntegerField(db_column='2BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bk = models.IntegerField(db_column='2BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2br = models.IntegerField(db_column='2BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ag = models.IntegerField(db_column='3AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ak = models.IntegerField(db_column='3AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ar = models.IntegerField(db_column='3AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bg = models.IntegerField(db_column='3BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bk = models.IntegerField(db_column='3BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3br = models.IntegerField(db_column='3BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    gm = models.IntegerField(db_column='GM')  # Field name made lowercase.
    gmk = models.IntegerField(db_column='GMK')  # Field name made lowercase.
    gmr = models.IntegerField(db_column='GMR')  # Field name made lowercase.
    scg = models.IntegerField(db_column='SCG')  # Field name made lowercase.
    sck = models.IntegerField(db_column='SCK')  # Field name made lowercase.
    scr = models.IntegerField(db_column='SCR')  # Field name made lowercase.
    stg = models.IntegerField(db_column='STG')  # Field name made lowercase.
    stk = models.IntegerField(db_column='STK')  # Field name made lowercase.
    str = models.IntegerField(db_column='STR')  # Field name made lowercase.


class EngGenRound3(models.Model):
    college = models.CharField(db_column='College', max_length=200)  # Field name made lowercase.
    branch = models.CharField(db_column='Branch', max_length=100)  # Field name made lowercase.
    number_1g = models.IntegerField(db_column='1G')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1k = models.IntegerField(db_column='1K')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_1r = models.IntegerField(db_column='1R')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ag = models.IntegerField(db_column='2AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ak = models.IntegerField(db_column='2AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2ar = models.IntegerField(db_column='2AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bg = models.IntegerField(db_column='2BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2bk = models.IntegerField(db_column='2BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_2br = models.IntegerField(db_column='2BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ag = models.IntegerField(db_column='3AG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ak = models.IntegerField(db_column='3AK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3ar = models.IntegerField(db_column='3AR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bg = models.IntegerField(db_column='3BG')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3bk = models.IntegerField(db_column='3BK')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3br = models.IntegerField(db_column='3BR')  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    gm = models.IntegerField(db_column='GM')  # Field name made lowercase.
    gmk = models.IntegerField(db_column='GMK')  # Field name made lowercase.
    gmr = models.IntegerField(db_column='GMR')  # Field name made lowercase.
    scg = models.IntegerField(db_column='SCG')  # Field name made lowercase.
    sck = models.IntegerField(db_column='SCK')  # Field name made lowercase.
    scr = models.IntegerField(db_column='SCR')  # Field name made lowercase.
    stg = models.IntegerField(db_column='STG')  # Field name made lowercase.
    stk = models.IntegerField(db_column='STK')  # Field name made lowercase.
    str = models.IntegerField(db_column='STR')  # Field name made lowercase.
