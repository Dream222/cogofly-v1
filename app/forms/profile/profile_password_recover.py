# coding=UTF-8

from django import forms
from django.utils.translation import ugettext_lazy as _

from app.forms.widgets.bootstrap_choices import BootstrapRadioSelect


class ProfilePasswordRecoverForm(forms.Form):
    YES_NO = (
        (True, _(u'Yes')),
        (False, _(u'No')),
    )
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}

    a = _(u'If you\'re not a robot, click "Yes" to get your password back:')
    i_agree = forms.TypedChoiceField(
        label=a, required=True,
        coerce=lambda x: x == 'True',
        choices=YES_NO,
        widget=BootstrapRadioSelect({'groupno': 0}))

    a = _(u'Enter your email to recover your password:')
    email = forms.EmailField(
        label=a, max_length=200, required=False,
        widget=forms.TextInput(attrs={'title': a, 'size': 30, 'type': 'email',
                                      'placeholder': _(u'mail@exemple.org'),
                                      'groupno': 0,
                                      'class': 'form-control'}),
        error_messages=e)
