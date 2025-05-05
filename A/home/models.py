from django.db import models
from accounts.models import User


class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='دسته بندی زیر مجموعه', related_name='scategories', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(verbose_name='اسلاگ', allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نگارنده', related_name='posts')
    category = models.ManyToManyField(Category, related_name='posts')
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ', allow_unicode=True)
    body = models.TextField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')

    def __str__(self):
        return f'{self.title}'




class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', verbose_name='عکس پست')
    name = models.CharField(max_length=150, verbose_name='نام')
    file = models.ImageField(upload_to='', verbose_name='فایل')
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='مقاله', related_name='comments')

    user_name = models.CharField(verbose_name='نویسنده', max_length=100)
    user_email = models.EmailField( verbose_name=' ایمیل نویسنده')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_reply = models.BooleanField(default=False)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)


    def __str__(self):
        return f'{self.user}'
