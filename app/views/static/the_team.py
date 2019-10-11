# coding=UTF-8
# Page statique : "À propos"

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _


class TheTeamView(View):
    template_name = 'static/the_team.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'the_team_title': _(u'Cogofly - The team'),
            'the_team_who_are_we': _(u'Who are we?'),
            'the_team_stories': [_(
                u'<strong>COGOFLY</strong> was founded by Mr. Franck '
                u'Lagathu, born on 21 June 1973 in Marseille, France.'
            ), _(
                u'Commercial Support Manager at Airbus Helicopters, and '
                u'former Sales Manager in the Estate Agents sector, the '
                u'launch of this new site marks the start, in parallel, of '
                u'a new and passionate adventure. Whilst I have a great '
                u'team supporting me, as the main player it is important '
                u'to talk about my own diverse experiences in order to '
                u'explain how the idea of launching such a concept came '
                u'about.'
            ), _(
                u'The first page written, or rather "scribbled", during '
                u'the summer of 2006 highlighted the need for a concept '
                u'which would later become part of the '
                u'<strong>COGOFLY</strong> adventure. It was indeed the '
                u'result of a simple observation: <strong>There are far '
                u'too many people who travel alone!</strong>'
            ), _(
                u'At the time, with this worldwide phenomenon in mind, my '
                u'site was leaning towards a name that I would later deem '
                u'to be overly "pessimistic": <strong>Never Alone!</strong>'
            ), _(
                u'The fact that I was based in Munich for 4 years, along '
                u'with other commitments, meant that I had to put the '
                u'project on the backburner for a while. However I NEVER '
                u'forgot about it...in fact quite the contrary! I was '
                u'constantly writing down different ideas and closely '
                u'following the global market. It was clear to me that the '
                u'entire world was concerned and I felt I had to do '
                u'something to address this universal issue.'
            ), _(
                u'Always there for my family and friends, this desire to '
                u'always help people out encouraged me to launch a website '
                u'which could respond to this requirement in every way. '
                u'The testimonies that can be found on this site only '
                u'serve to reinforce this temperament which is fully '
                u'recognized and appreciated by my entourage; a '
                u'temperament which, quite naturally, resulted in a '
                u'connection between this site and my destiny.'
            ), _(
                u'Back from Germany in 2010, after a multitude of fruitful '
                u'and enriching encounters, I was able to restart work on '
                u'my ideas which had by now reached a dozen pages. The 5 '
                u'years following my return home only served to strengthen '
                u'the courage of my convictions, and several useful pages '
                u'were added in order to further the project and work '
                u'towards something more concrete.'
            ), _(
                u'2015 has been a crucial year in that I have had the '
                u'chance to meet a number of people within the sector, '
                u'along with web service providers, and have thus learned '
                u'a great deal from being in their presence. These '
                u'contacts, located via a list given to me by Marseille’s '
                u'Chamber of Commerce and Industry (CCI), through their '
                u'respective remarks and feedback regarding my concept, '
                u'have only served to strengthen my desire to proceed with '
                u'the launch of this new social network on an '
                u'international scale.'
            ), _(
                u'The support of this institution helped me to realize '
                u'that a number of additional skills were required, such '
                u'as legal, financial and HR-related aspects...as is the '
                u'case for any newfound company. Thanks to them, I was '
                u'able to obtain all of the contacts required in order to '
                u'set me on the right path...'
            ), _(
                u'All of these encounters resulted in me finding another '
                u'name, more internationally orientated, which expressed '
                u'the idea of taking off...<strong>Take Off Mate '
                u'(TOM)</strong> was therefore brought to the table. At '
                u'this point I have to say a big thank you to several of '
                u'my work colleagues who took the time to motivate me and '
                u'give me their opinions in order to ratify each key step '
                u'of my project.'
            ), _(
                u'It was with this name that I was able to present it to '
                u'the Masters students at the University of Aix-Marseille '
                u'at Luminy, more precisely to the <strong>Junior '
                u'Aix-Marseille company (JAM), presided by Mr Florian '
                u'DOUAY</strong> who, with the support of two other '
                u'contributors, came up with a 43-page technical '
                u'specification. It was therefore only normal to choose '
                u'this establishment, and the choice was made even more '
                u'quickly due to the fact that the students’ were '
                u'instantly motivated, willing and full of ideas; fully in '
                u'line with the ethics of this site.'
            ), _(
                u'As I turned the pages of the technical specification, it '
                u'seemed to suit me more and more, and I felt the need to '
                u'make the adequate changes in order to add the finishing '
                u'touches. The changes carried out helped to form the '
                u'foundations of this site.'
            ), _(
                u'Once the new 50-page version approved, my attention then '
                u'turned towards <strong>HQF Development, and its '
                u'representative Sir Olivier PONS</strong>, who convinced '
                u'me to finally take the plunge with this '
                u'international-scale project. His reactivity, honest '
                u'approach throughout our different exchanges, passion and '
                u'a general feel-good factor that I got from him, led '
                u'quite naturally to <strong>the signing of a development '
                u'contract on 5 October 2015.</strong>'
            ), _(
                u'As indicated in the "About COGOFLY" section, '
                u'<strong>COGOFLY</strong> was therefore created one week '
                u'before the signing of the said contract, and the brand '
                u'was then deployed on a global scale.'
            ), _(
                u'<strong>My goal is to make this new social network the '
                u'reference in terms of co-trips: "The LinkedIn/Facebook" '
                u'of the Tourism industry. This new community will then '
                u'have access to a reliable and intuitive site, and be '
                u'able to meet up in total confidence and share common '
                u'projects and goals.</strong>'
            ), _(
                u'The conclusion of all this, and this adage came to me '
                u'quite naturally, is that:'
            ), _(
                u'<h1>Alone, we think...Together, we get away!</h1>'
            )]
        })
