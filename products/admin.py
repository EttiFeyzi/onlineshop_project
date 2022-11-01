from django.contrib import admin

from .models import Product, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'status',]

    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class CommenttAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active',]

