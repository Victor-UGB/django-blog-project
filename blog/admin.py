from django.contrib import admin
from .models import Post
from .models import auth_User

# Register your models here.
admin.site.register(Post)
admin.site.register(auth_User)