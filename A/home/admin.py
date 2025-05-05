from django.contrib import admin
from . models import Post, Category,PostImage, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug':('title',)}

class PostImageAdmin(admin.TabularInline):
    model = PostImage
    raw_id_fields = ['post']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('auther', )
    model = Post
    inlines = [PostImageAdmin]
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'reply_comment')