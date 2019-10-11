# coding=UTF-8
# Page statique : "À propos"

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _


class ContactUsView(View):
    template_name = 'static/contact_us.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'contact_us_title': _(u'Cogofly - Contact us'),
            'contact_us_contact_us': _(
                u'If you require any more information or have any questions '
                u'about our Terms and Conditions, please feel free to contact '
                u'us by email by clicking '
                u'<a href="mailto:cogofly@gmail.com" target="_blank">'
                u'here '
                u'</a>'),
        })
