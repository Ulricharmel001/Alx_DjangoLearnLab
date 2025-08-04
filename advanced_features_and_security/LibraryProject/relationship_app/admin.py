# from django.contrib import admin

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# from .models import Library, Book  , Author, Librarian, UserProfile


# admin.site.register(Library)  # Register Library
# # admin.site.register(Book)     # Register Book
# admin.site.register(Author)
# admin.site.register(Librarian)
# admin.site.register(UserProfile)
# admin.site.register(CustomUser)

# class BookAdmin(admin.ModelAdmin):
#     list_display =('title', 'author')
#     fields = ('title', 'author', 'publication_year')
    
# admin.site.register(Book)



# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = UserAdmin.fieldsets + (
#         ('Additional Info', {'fields': ('role', 'date_of_birth', 'profile_photo')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         ('Additional Info', {'fields': ('role', 'date_of_birth', 'profile_photo')}),
#     )
#     list_display = ['username', 'email', 'role', 'is_staff']

# admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )


