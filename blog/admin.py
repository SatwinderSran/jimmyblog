from django.contrib import admin
from .models import Post, Profile, Images, Comment, Contactus
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'created', 'updated')
    search_fields = ('author__username', 'title')
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','message')
    list_filter = ('name', 'email')
    search_fields = ('name', 'email')

admin.site.register(Comment)
admin.site.register(Contactus,MessageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Images, ImagesAdmin)
