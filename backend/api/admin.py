from api import models as api_models
from django.contrib import admin

# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['full_name', 'username', 'email']
#     list_display = ['username', 'email']


# class ProfileAdmin(admin.ModelAdmin):
#     search_fields = ['user']
#     list_display = ['thumbnail', 'user', 'full_name']


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["title"]


# class PostAdmin(admin.ModelAdmin):
#     list_display = ["title", "user", "category", "view"]


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ["post", "name", "email", "comment"]


# class BookmarkAdmin(admin.ModelAdmin):
#     list_display = ["user", "post"]


# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ["user", "post", "type", "seen",]

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(api_models.User)
admin.site.register(api_models.Profile)
admin.site.register(api_models.Category, CategoryAdmin)
admin.site.register(api_models.Post, PostAdmin)
admin.site.register(api_models.Comment)
admin.site.register(api_models.Notification)
admin.site.register(api_models.Bookmark)
