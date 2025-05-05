from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from . managers import UserManager


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    username = models.CharField(max_length=150, verbose_name='نام کاربری')
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن", unique=True)
    avatar = models.ImageField(upload_to='%Y/%m/%d', verbose_name='آواتار', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='کاربر کارمند')
    is_admin = models.BooleanField(default=False, verbose_name='کاربر ادمین')

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin

    @property
    def total_posts(self):
        return self.posts.count()
