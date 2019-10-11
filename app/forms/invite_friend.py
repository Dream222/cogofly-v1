# coding=UTF-8

from django import forms
from django.utils.translation import ugettext_lazy as _


class InviteFriendForm(forms.Form):
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}
    a = _(u'First name:')
    prenom = forms.CharField(
        label=a, max_length=100, required=False,
        widget=forms.TextInput(attrs={'title': a,
                                      'placeholder': _(u'his/her first name'),
                                      'class': 'form-control'}
                               ),
        error_messages=e)

    a = _(u'Last name:')
    nom = forms.CharField(
        label=a, max_length=100, required=False,
        widget=forms.TextInput(attrs={'title': a,
                                      'placeholder': _(u'his/her last name'),
                                      'class': 'form-control'}),
        error_messages=e)

    a = _(u'Email:')
    email = forms.EmailField(
        label=a, max_length=200,
        widget=forms.TextInput(attrs={'title': a, 'size': 30, 'type': 'email',
                                      'placeholder': _(u'mail@exemple.org'),
                                      'class': 'form-control'}),
        error_messages=e)

    a = _(u'Personal message (optional):')
    message = forms.CharField(
        label=a, max_length=1000,
        widget=forms.Textarea(attrs={
            'title': a, 'size': 30,
            'type': 'textarea', 'rows': '9',
            'class': 'form-control'}),
        error_messages=e)


