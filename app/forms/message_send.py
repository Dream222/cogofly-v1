# coding=UTF-8
"""
Form pour envoyer un message.
(!) Lors de la construction on lui passe un id qui est caché :
     - soit Activite = pour faire suivre l'id de l'activité,
     - soit Conversation = pour faire suivre l'id de la conversation
"""

from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from app.forms.generic.form_hidden_field import HiddenFieldForm


class MessageSendForm(HiddenFieldForm):
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}

    # !! No label here, exceptional:
    a = _(u'Send a message:')
    message = forms.CharField(
        label='', localize=True, required=False,
        widget=widgets.Textarea(attrs={
            'title': a,
            'rows': 5,
            'cols': 40,
            'style': 'resize: vertical',
            'class': 'form-control'}))

