# coding=UTF-8

from django import forms
from django.utils.translation import ugettext_lazy as _

from app.forms.generic.fields.checkbox_input_bootstrap import \
    CheckboxInputBootstrap


class TestimonyForm(forms.Form):
    e = {'required': _(u'This field is required'),
         'invalid': _(u'This field contains invalid data')}

    a = _(u'Your testimonies and positive feedback are '
          u'paramount in helping Cogofly go that extra mile...'
          u'They will also motivate new members to join this new community '
          u'of Cogoflyers! '
          u'<br/><br/>'
          u'These same testimonies will appear on '
          u'your contacts\' news feed and will be available to view '
          u'at any time via the link "Testimonies" below')
    testimony = forms.CharField(
        label=a, max_length=20000,
        widget=forms.Textarea(attrs={
            'title': a,
            'size': 25,
            'type': 'textarea', 'rows': '8',
            'class': 'form-control'}),
        error_messages=e)

    a = _(u"Check if you agree to add your name, and your photo profile, "
          u"inside the testimony")
    testimony_show_name = forms.BooleanField(
        label=a, required=True,
        widget=CheckboxInputBootstrap(attrs={
            'title': a, }),
        error_messages=e)

