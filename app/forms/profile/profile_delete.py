# coding=UTF-8

from django import forms
from django.forms import widgets
from django.utils.translation import ugettext_lazy as _

from app.forms.widgets.bootstrap_choices import BootstrapRadioSelect


class ProfileDeleteForm(forms.Form):
    YES_NO = (
        (True, _(u'Yes')),
        (False, _(u'No')),
    )
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}

    a = _(u'In order to help us improving Cogofly, '
          u'and add new features, could you please precise us the reason?')
    reason_delete = forms.CharField(
        label=a, localize=True, required=False,
        widget=widgets.Textarea(attrs={
            'title': a, 'rows': 5, 'cols': 40, 'style': 'resize: vertical',
            'class': 'form-control',
            'groupno': 0}))

    a = _(u'By clicking "Yes" you agree to delete your account:')
    # 'i_agree' seul est en conflit avec 'i_agree' de ProfileDeactivateForm
    # -> le rendre unique via '_delete' :
    i_agree_delete = forms.TypedChoiceField(
        label=_(u'Still agree?'),
        required=False,
        coerce=lambda x: x == 'True',
        choices=YES_NO,
        widget=BootstrapRadioSelect({'groupno': 0}))
