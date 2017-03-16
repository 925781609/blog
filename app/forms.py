from django import forms 
from django.forms.extras.widgets import SelectDateWidget
from .models import User
BIRTH_YEAR_CHOICES=('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                           ('green', 'Green'),
                           ('black', 'Black'))

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)
    birth_year = forms.DateField( widget=SelectDateWidget() )
    #birth_year = forms.DateField( widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES) )
    favorite_colors = forms.MultipleChoiceField( required=False,
            widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your Email', max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    
    #def clean(self):
    #    user = self.authenticate_via_email()
    #    if not user:
    #        raise forms.ValidationErrror("Sorry, that login was invalid. Pls try again. ")
    #    else:
    #        self.user = user
    #    return self.cleaned_data


    #def authenticate_via_email(self):
    #    """
    #        Authenticate user using email.
    #        Returns user object if authenticated else None
    #    """
    #    email = self.cleaned_data['email']
    #    if email :
    #        try: 
    #            user = get_object_or_404(User, email=email)
    #            if user.check_password( self.cleaned_data['password']):
    #                return user
    #        except ObjectDoesNotExist:
    #            pass
    #    return None
