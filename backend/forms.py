from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Attractions, Restaurants, Apartments, About_PageTitle, About_PresentationText, About_TeamTitle, About_MemberOne, About_MemberTwo, About_MemberThree

class PostAttraction(forms.ModelForm):

    class Meta:
        model = Attractions
        fields = ('title', 'text',)

class PostRestaurant(forms.ModelForm):

    class Meta:
        model = Restaurants
        fields = ('title', 'text',)

class PostApartment(forms.ModelForm):

    class Meta:
        model = Apartments
        fields = ('title', 'text',)

class PostAboutTitle(forms.ModelForm):

    class Meta:
        model = About_PageTitle
        fields = ('title',)

class PostAboutPresentation(forms.ModelForm):

    class Meta:
        model = About_PresentationText
        fields = ('title', 'text',)

class PostAboutTeamTitle(forms.ModelForm):

    class Meta:
        model = About_TeamTitle
        fields = ('title',)

class PostAboutMemberOne(forms.ModelForm):

    class Meta:
        model = About_MemberOne
        fields = ('title', 'text',)

class PostAboutMemberTwo(forms.ModelForm):

    class Meta:
        model = About_MemberTwo
        fields = ('title', 'text',)

class PostAboutMemberThree(forms.ModelForm):

    class Meta:
        model = About_MemberThree
        fields = ('title', 'text',)

# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class PostAlgoRight(forms.ModelForm):

#     class Meta:
#         model = Algoright
#         fields = ('title', 'text',)

# backend forms to create (at least)
#BackHomeL, BackHomeR, BackAlgL, BackAlgR