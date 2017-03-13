from django.contrib import admin
from .models import User
from django import forms
# Register your models here.


class RegisterationForm( forms.ModelForm):
    password1 = forms.CharField(label='PassWord', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =('username', 'email', 'date_of_birth')

    def clean_password2(self):
        password1 = self.clean_data.get("password1")
        password2 = self.clean_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self,  commit=True):
        user = super(UserCreationForm, self).save(commit=Fales)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('usernme', 'email', 'password', 'date_of_birth', 'is_active', ''is_admin)
    
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
    list_display = ('username', 'email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', )}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldset is not a standard ModelAdmin attribute.
    # UserAdmin ovverrides get_fieldsets to use this attribute when creatung a user.
    add_fieldsets = (
            (None, {
                    'classes': ('wide',),
                    'fields': ('username', 'date_of')
                
                }
            
            )
