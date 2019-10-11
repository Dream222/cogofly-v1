# coding=UTF-8
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_markdown.models import MarkdownField

from app.models.generic import BaseModel


@python_2_unicode_compatible
class Publicite(BaseModel):

    PUBLICITE_VOYAGES_DROITE = 1
    PUBLICITE_VOYAGES_GAUCHE = 2
    PUBLICITE_MY_PROFILE_GAUCHE = 3
    PUBLICITE_MY_PROFILE_DROITE = 4
    PUBLICITE_FIL_ACTUALITE_GAUCHE = 5
    PUBLICITE_FIL_ACTUALITE_DROITE = 6

    TAB_PUBLICITE = {
        PUBLICITE_VOYAGES_DROITE: _(u'Ads travels right'),
        PUBLICITE_VOYAGES_GAUCHE: _(u'Ads travels left'),
        PUBLICITE_MY_PROFILE_GAUCHE: _(u'Ads my profile left'),
        PUBLICITE_MY_PROFILE_DROITE: _(u'Ads my profile right'),
        PUBLICITE_FIL_ACTUALITE_GAUCHE: _(u'Ads news left'),
        PUBLICITE_FIL_ACTUALITE_DROITE: _(u'Ads news right'),
    }

    position = models.IntegerField(
        choices=[(a, b) for a, b in list(TAB_PUBLICITE.items())],
        default=None, null=True, blank=True,
        help_text=_(u"Where this ads goes"),
        verbose_name=_(u"Where this ads goes"), )

    label = models.CharField(default=None, null=True, blank=True,
                             max_length=200,
                             help_text=_(u"A recall of what this ads "
                                         u"contains (language independant)"),
                             verbose_name=_(u'Label'),)
    date_publication = models.DateTimeField(default=datetime.datetime.now,
                                            null=True, blank=True,
                                            verbose_name=_(u'Publication date'))
    ordre_si_top = models.IntegerField(
        null=True, blank=True, default=None,
        help_text=_(u'Priority: the lowest the higher '
                    u'("1" is <b>before</b> "2" and so on...).'),
        verbose_name=_(u'How this ad appears'))

    def __str__(self):
        if not self.label:
            return u''
        return (self.label[:95] + '...') if len(self.label) > 90 else self.label

    class Meta(BaseModel.Meta):
        ordering = ['date_v_debut']
        verbose_name = _(u'Ad')
        verbose_name_plural = _(u'Ads')


@python_2_unicode_compatible
class PubliciteTraduit(BaseModel):
    publicite = models.ForeignKey(Publicite, default=None, null=True,
                                  blank=True, on_delete=models.CASCADE)
    locale = models.CharField(default=None, null=True, blank=True,
                              max_length=2,
                              help_text=_(u"Ads locale (en, fr, ...)"),
                              verbose_name=_(u"Ads locale"),)
    title = models.CharField(default=None, null=True, blank=True,
                             max_length=200,
                             help_text=_(u"Ads title"),
                             verbose_name=_(u'Title'),)
    content = MarkdownField(default=None, null=True, blank=True,
                            help_text=_(u"Ads content"),
                            verbose_name=_(u'Content'),)

    def description(self):
        a = u'{} / {} - {}'.format(
            self.locale if self.locale else _(u'no locale'),
            self.title if self.locale else _(u'no title'),
            self.content if self.content else _(u'no content yet'),)
        return (a[:95] + '...') if len(a) > 90 else a

    def __str__(self):
        return self.description().strip()

    class Meta(BaseModel.Meta):
        ordering = ['date_v_debut']
        verbose_name = _(u'Ads-translated content')
        verbose_name_plural = _(u'Ads-translated')
