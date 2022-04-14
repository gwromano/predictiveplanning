from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    change_list_template='change_list_form.html'

    change_form_template = 'change_form.html'

    add_form_template='add_form.html'

    list_display = ('first_name','last_name','email','is_staff', 'is_active',)
    list_filter = ('first_name','email', 'is_staff', 'is_active',)

    search_fields = ('email','first_name','last_name','a1','a2','city','state','pincode')
    ordering = ('first_name',)

    add_fieldsets = (
        ('Personal Information', {
            # To create a section with name 'Personal Information' with mentioned fields
            'description': "",
            'classes': ('wide',),  # To make char fields and text fields of a specific size
            'fields': (('first_name','last_name'),'email','a1','a2','city','state','pincode','check',
                       'password1', 'password2',)}
        ),
        ('Permissions',{
            'description': "",
            'classes': ('wide', 'collapse'),
            'fields':( 'is_staff', 'is_active','date_joined')}),
    )


    def change_view(self, request, object_id, form_url='', extra_context=None):


        extra_context = {'title': 'Here you can type your new title for the User Change tab'}


        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )