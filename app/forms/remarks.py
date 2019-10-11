# coding=UTF-8

from django import forms
from django.utils.translation import ugettext_lazy as _


class RemarksForm(forms.Form):
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}

    a = _(u"Feel free to contact us with any remarks or suggestions "
          u"you may have, any problems you have encountered and any ways "
          u"in which you feel the site could be improved in order to "
          u"meet your expectations.")
    remarks = forms.CharField(
        label=a, max_length=20000,
        widget=forms.Textarea(attrs={
            'title': a, 'size': 25,
            'type': 'textarea', 'rows': '8',
            'class': 'form-control'}),
        error_messages=e)


