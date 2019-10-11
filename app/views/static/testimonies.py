# coding=UTF-8
# Page statique : "À propos"

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _

from app.models.personne import ActiviteTestimony
from app.views.common import CommonView


class TestimoniesView(View):
    template_name = 'static/testimonies.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'temoignages': ActiviteTestimony.objects.filter(
                validated_by_moderator=True,
                date_v_fin__exact=None),
            'testimonies_title': _(u'Cogofly - Testimonies'),
            'testimonies': [{
                'title': _(u'Olivier Foulon:'),
                'details': _(
                    u'"Having had the chance to work together with FRANCK on '
                    u'several projects, I have had the opportunity to '
                    u'accompany him on several business trips; he is the kind '
                    u'of guy you will never forget, always willing to provide '
                    u'assistance to all kinds of people. I believe it is part '
                    u'of his genetic profile to be on Earth, help people and '
                    u'make them happy, in both small and great ways. I believe '
                    u'his site is part of this process and constitutes a real '
                    u'inner part of his personality; almost as if it were the '
                    u'logical conclusion to a personal ambition dedicated to '
                    u'fulfilling everybody\'s needs and, more precisely, '
                    u'passion for travelling, and the embedded necessity for '
                    u'everybody to interchange.'
                )}, {
                'title': _(u'Michel Wauthier:'),
                'details': _(
                    u'"I have known Franck for quite a while now. He has a '
                    u'unique way of meeting people, striking up relationships, '
                    u'genuine and sincere ones, and is very loyal when it '
                    u'comes to friendship. Always on the move, dynamic, full '
                    u'of new ideas, with a real entrepreneurial spirit, he has '
                    u'shown courage and determination by putting everything he '
                    u'has into a project in which he wholeheartedly believes; '
                    u'a project with the goal of bringing people closer '
                    u'together, and getting them to meet up with each other. A '
                    u'project which, upon reflection, resembles him a great '
                    u'deal; and it is for this reason that it has to work. And '
                    u'not just for him, but for those whom it will help to '
                    u'"co-go-fly": new faces for new trips and places.'
                )}, {
                'title': _(u'Benjamin Mallows:'),
                'details': _(
                    u'"I\'ve known Franck for several years now and his will '
                    u'to succeed, drive and motivation are simply second '
                    u'to none. It\'s a real pleasure to work with people '
                    u'like Franck because you always have that peace of mind, '
                    u'safe in the knowledge that results are guaranteed. '
                    u'Franck is a loyal and trustworthy colleague and '
                    u'friend who, I have no doubt about it, has the '
                    u'profile and all the prerequisites to be the very best. '
                    u'His project is a fascinating one and I\'m very much '
                    u'looking forward to seeing all of his hard '
                    u'work pay off."'
                )}, {
                'title': _(u'Florent Portes:'),
                'details': _(
                    u'"Franck is the designer and creator of this website, he '
                    u'asked me to help him for the development, I was '
                    u'motivated by this idea to find a solution for all these '
                    u'people that don’t want to travel alone, indeed, times '
                    u'are difficult these days, for all, economic crisis, '
                    u'current situation, terrorism but the fact you can find '
                    u'hope despite all these bad things happening is first of '
                    u'all a noble idea and to take a stand in this world, and '
                    u'to see few persons motivated to develop this project, '
                    u'this is a really creative and innovative idea, to allow '
                    u'people that don’t know each other, to meet, travel and '
                    u'the more you get to know someone, the closer you feel to '
                    u'them, and these friendships will last, because love is '
                    u'stronger than all things, and we need to defend this '
                    u'love in this chaotic world today. '
                    u'Franck is a committed person, I have only known him for '
                    u'a few years but what struck me is his strength of '
                    u'conviction, close to stubbornness but to do good, and to '
                    u'seek quality, what struck me again is his motivation, he '
                    u'refuses to fail, I am motivated to work with him to see '
                    u'these qualities and concepts in him, his desire to '
                    u'succeed and to bring forth his vision, because it is '
                    u'with small and simple things that great things are '
                    u'achieved."'
                )}]
        })
