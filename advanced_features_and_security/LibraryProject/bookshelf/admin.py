from django.contrib import admin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year', )

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'username'  )
    # add_fieldsets =(
    #     {

    #     }
    # )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)




    
