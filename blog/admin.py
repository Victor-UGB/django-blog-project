from django.contrib import admin
from .models import Post
from .models import auth_User, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(auth_User)
admin.site.register(Comment)