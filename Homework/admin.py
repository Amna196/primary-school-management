from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Homework, User, Student # Import your custom User model

admin.site.register(Homework)
admin.site.register(Student)
# Register your custom User model
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass # You can customize the admin view for your User model here. If you don't have any specific customization, you can leave it as is.
