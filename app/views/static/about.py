# coding=UTF-8
# Page statique : "À propos"

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _


class AboutView(View):
    template_name = 'static/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'about_title': _(u'About Cogofly'),
            'about_main_aim': _(
                u'The main aim of this page is to explain the Cogofly concept.'
                u'The brand Cogofly, name and logo, came to light thanks to '
                u'the human values that this concept wishes to get across and '
                u'maintain moving forward.'),
            'about_constat': _(
                u'This brand is the result of a worldwide issue: '
                u'<strong>There are far too many people who travel '
                u'alone!</strong>'),
            'about_concept_title': _(u'The concept:'),
            'about_concept_content_1': _(
                u'The idea came to light after several professional and '
                u'private trips I have been able to do over the years...'),
            'about_concept_content_2': _(
                u'<strong>This social network website is a worldwide concept'
                u' which will help to avoid travelling, spending a weekend, '
                u'make a business trip, do some rides (cultural, sport, '
                u'education, etc...), or just going on an outing, ALONE...'
                u'if someone just feel ALONE, as well and for any reasons, '
                u'this website is then the good one !</strong>'),
            'about_concept_content_3': _(
                u'This situation, unfortunately, doesn\'t have "borders"...'
                u'It can touch a person, a group of person, couples, families '
                u'and also all socio-professional categories. '),
            'about_concept_content_4': _(
                u'<strong>Cogofly\'s primary goal is to help people to avoid '
                u'travelling alone any more. The second one is simply to help '
                u'them to no longer be alone.</strong>'),
            'about_concept_content_5': _(
                u'It also naturally deals with the following notion:<strong>: "'
                u'Who has never felt like they\'re always well surrounded, '
                u'but ended up feeling rather alone ?</strong>'),
            'about_brand_title': _(u'The brand: name + logo'),
            'about_brand_content_1': _(
                u'It was of paramount importance to find a site name which '
                u'was both catchy and easy to remember for all members, plus '
                u'anyone else reading this page (verbally and visually).'),
            'about_brand_content_2': _(
                u'<strong>It was therefore absolutely necessary to '
                u'find:</strong>'),
            'about_brand_content_li_1': _(
                u'A short name, easy to pronounce and remember (Facebook, '
                u'Google, Twitter, Airbnb, Viadeo, etc...).'),
            'about_brand_content_li_2': _(
                u'A simple, clear and visual logo.'),

            'about_name_title': _(u'Name:'),
            'about_name_content_1': _(
                u'In order for this mission to succeed, it was important to '
                u'keep certain ideas and "basic" words in mind, such as:'),
            'about_name_content_2': _(
                u'Sharing: co-travelling, car-sharing...'),
            'about_name_content_3': _(
                u'Going out / Being on the move: trips, excursions, '
                u'days/nights out...'),
            'about_name_content_4': _(
                u'Travelling: going away, heading off, jetting off...'),
            'about_name_content_5': _(
                u'<strong>CO-GO-FLY</strong>: The name seemed so '
                u'<strong>OBVIOUS</strong>!'),
            'about_name_content_6': _(
                u'<strong>And so Cogofly was born, its domain name reserved '
                u'on Monday 28 September 2015 and its trademark protected '
                u'with INPI</strong>!'),


            'about_logo_title': _(u'Logo:'),
            'about_logo_content_1': _(
                u'<strong>In order to complete this mission, it was important '
                u'to highlight:</strong>'),
            'about_logo_content_li_1': _(
                u'The "Co" concept, which encapsulates the site\'s main '
                u'focus: Think "together", Think "Co" and Take Off!'),
            'about_logo_content_li_2': _(
                u'The infinity sign, ∞, which resembles Co...evoking the '
                u'infinite possibilities that the site will bring with its '
                u'official launch on 21/06/2016.'),
            'about_logo_content_li_3': _(
                u'The "smile" situated under the name, more precisely under '
                u'the "Gofly" part, and forming a loop around "Co".'),
            'about_logo_content_li_4': _(
                u'A "smile" which also evokes the idea of an open and '
                u'accessible world.'),
            'about_logo_content_li_5': _(
                u'The separation between the 2 semi-circles is intentional, '
                u'calling to mind the concept of Yin & Yang, and further '
                u'eliciting the need to travel together...'),
            'about_logo_content_li_6': _(
                u'A slightly tilted circle in order to express the idea '
                u'of movement'),
        })
