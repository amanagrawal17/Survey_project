from django.contrib import admin
from surveyapp.models import *
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
# class UserModelAdmin(BaseUserAdmin):


#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ["id","email", "first_name","last_name" "is_admin"]
#     list_filter = ["is_admin"]
#     fieldsets = [
#         (None, {"fields": ["email", "password"]}),
#         ("Personal info", {"fields": ["first_name"]}),
#         ("Permissions", {"fields": ["is_admin"]}),
#     ]
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = [
#         (
#             None,
#             {
#                 "classes": ["wide"],
#                 "fields": ["email", "first_name", "password1", "password2"],
#             },
#         ),
#     ]
#     search_fields = ["email"]
#     ordering = ["email"]
#     filter_horizontal = []
# admin.site.register(User, UserModelAdmin)
# admin.site.unregister(User)
# Now register the new UserAdmin...


admin.site.register(User)
admin.site.register(Question_types)
admin.site.register(Questions)
admin.site.register(Response)
