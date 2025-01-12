from django.contrib import admin
from .models import Room, Message
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
#
# from .forms import UserUpdateForm, SignUpForm
# from .models import CustomUser
#
#
# class CustomUserAdmin(UserAdmin):
#     add_form = SignUpForm
#     form = UserUpdateForm
#     model = CustomUser
#     list_display = ['email', 'username',]
#
#
# admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(Message)
admin.site.register(Room)