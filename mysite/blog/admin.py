from django.contrib import admin
from blog.models import Category, Post

class CategoryInline(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'published_date')
    inlines = [CategoryInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)
