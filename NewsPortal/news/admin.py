from django.contrib import admin
from .models import Post, Category
from .models import *
from modeltranslation.admin import TranslationAdmin




class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)

# Register your models here.
