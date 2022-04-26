from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin



# Create your models here.

class Usermanager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('email must be required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be is_superuser=True')

        return self._create_user(email, password, **extra_fields)

class user(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.CharField(max_length=255, null=True,blank=True , unique=True)
    mobile = models.CharField(max_length=12, null=True,blank=True)
    alternate_mobile = models.CharField(max_length=12, null=True,blank=True)
    fname = models.CharField(max_length=255, null=True,blank=True)
    birthday = models.CharField(max_length=255, null=True,blank=True)
    laname = models.CharField(max_length=255, null=True,blank=True)
    age = models.CharField(max_length=10, null=True,blank=True)
    gender = models.CharField(max_length=20, null=True,blank=True)
    village = models.CharField(max_length=20, null=True,blank=True)
    district = models.CharField(max_length=20, null=True,blank=True)
    city = models.CharField(max_length=20, null=True,blank=True)
    password = models.CharField(max_length=255, null=True,blank=True)
    cpassword = models.CharField(max_length=255, null=True,blank=True)
    address1 = models.CharField(max_length=100, null=True,blank=True)
    permanent_address = models.CharField(max_length=100, null=True,blank=True)
    pin = models.CharField(max_length=100, null=True,blank=True)
    Aadhar = models.CharField(max_length=100, null=True,blank=True)
    Active = models.BooleanField(default=False, null=True,blank=True)
    qualification = models.CharField(max_length=100, null=True,blank=True)
    school = models.CharField(max_length=100, null=True,blank=True)
    passingyear = models.CharField(max_length=100, null=True,blank=True)
    marks = models.CharField(max_length=100, null=True,blank=True)
    grade = models.CharField(max_length=100, null=True,blank=True)
    course_detail = models.CharField(max_length=100, null=True,blank=True)
    updated_by = models.CharField(max_length=100, null=True,blank=True)
    Fees = models.CharField(max_length=100, null=True,blank=True)
    Fees_date = models.CharField(max_length=100, null=True,blank=True)
    Fees_amount = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    is_staff = models.BooleanField(default=False, )
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = Usermanager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser




class StudentInquiry(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    selectmodel = models.CharField(max_length=500,blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
