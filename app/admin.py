from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# Register your models here.

from .models import User

class UserCreationForm( forms.ModelForm):
    password1 = forms.CharField(label='PassWord', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =('email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self,  commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')
    
    def clean_password(self):
        return self.initial['password']
 
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    ''' The fields to be used in displaying the User model.
        These override the definitions on the base UserAdmin
        the reference specific fields on the auth.User
    ''' 
    list_display = ( 'email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ( 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldset is not a standard ModelAdmin attribute.
    # UserAdmin ovverrides get_fieldsets to use this attribute when creatung a user.
    add_fieldsets = (
            (None, {
                    'classes': ('wide',),
                    'fields': ('email','date_of_birth', 'password1', 'password2')}
            ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

#Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model for admin.
admin.site.unregister(Group)
