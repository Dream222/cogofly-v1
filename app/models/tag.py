# coding=UTF-8
import urllib2

import ftfy
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from app.models.generic import BaseTranslatableModel, BaseModel, Langue
from urllib import urlencode
import json as simplejson


class BaseTag(BaseTranslatableModel):
    TYPE_ENTREPRISE = u'0'
    TYPE_PROFESSION = u'1'
    TYPE_LANGUE = u'2'
    TYPE_GOOGLEMAPS = u'3'
    TYPE_PERMIS = u'4'
    TYPE_DIPLOME = u'5'
    TYPE_CENTRE_DINTERET = u'6'
    TYPE_HOBBY = u'7'
    TAB_TYPES = {
        TYPE_ENTREPRISE: _(u'Company'),
        TYPE_PROFESSION: _(u'Job'),
        TYPE_LANGUE: _(u'Language'),
        TYPE_GOOGLEMAPS: _(u'Google maps'),
        TYPE_PERMIS: _(u'Driving licences'),
        TYPE_DIPLOME: _(u'Diploma'),
        TYPE_CENTRE_DINTERET: _(u'Point of interest'),
        TYPE_HOBBY: _(u'Hobby'),
    }
    type_tag = models.CharField(max_length=1,
                                choices=[(a, b) for a, b in
                                         list(TAB_TYPES.items())],
                                default=TYPE_ENTREPRISE)

    class Meta(BaseModel.Meta):
        abstract = True


@python_2_unicode_compatible
class TagWithValue(BaseTag):
    description = models.CharField(max_length=200, default=u'', null=True,
                                   blank=True)
    value = models.CharField(max_length=200, default=u'', null=True,
                             blank=True)

    def __str__(self):
        return u'{} - {} : {} -> {}'.format(
            self.id, self.langue.locale, self.description, self.value)

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Tag with an associated value")
        verbose_name_plural = _(u"Tags with an associated value")


@python_2_unicode_compatible
class Tag(BaseTag):
    description = models.CharField(max_length=200, default=u'', null=True,
                                   blank=True)

    def __str__(self):
        return self.description

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Tag")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOUVELLE RÉECRITURE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOUVELLE RÉECRITURE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOUVELLE RÉECRITURE
@python_2_unicode_compatible
class TagBase(BaseModel):
    TYPE_MATIERE = 1
    TYPE_ACTIVITE = 2
    TYPE_HOBBY = 3
    TYPE_PERMIS = 4
    TYPE_PERSONNALITE = 5
    TYPE_LANGUE = 6
    TYPE_GOOGLE_MAP = 7
    TAB_TYPES = {
        TYPE_MATIERE: _(u'Subjects'),
        TYPE_ACTIVITE: _(u'Activity sectors'),
        TYPE_HOBBY: _(u'Hobbies'),
        TYPE_PERMIS: _(u'Driving licences'),
        TYPE_PERSONNALITE: _(u'Personality'),
        TYPE_LANGUE: _(u'Language'),
        TYPE_GOOGLE_MAP: _(u'Google maps'),
    }
    type_tag = models.IntegerField(choices=[(a, b) for a, b in
                                            list(TAB_TYPES.items())],
                                   null=True, blank=True,
                                   default=None)
    poids = models.IntegerField(default=None, blank=True, null=True,
                                help_text=_(u"Used for ordering"),)
    description = models.CharField(max_length=200, default=u'', null=True,
                                   blank=True)

    def __str__(self):
        return u'({}) - {}'.format(
            TagBase.TAB_TYPES[self.type_tag] if self.type_tag else u'?',
            self.description)

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Referent tag")
        verbose_name_plural = _(u"Referent tags")


@python_2_unicode_compatible
class TagTraduit(BaseModel):
    tag = models.ForeignKey(TagBase, default=None, blank=True, null=True,
                            help_text=_(u"It's the master tag"),
                            related_name='tag')
    langue = models.ForeignKey(Langue, default=None, blank=True, null=True)
    value = models.CharField(max_length=200, default=u'', null=True,
                             blank=True)

    def __str__(self):
        return u'{} - {} ({}) -> {}'.format(
            self.id,
            str(self.tag) if self.tag else u'(?)',
            self.langue.locale if self.langue else u'(?)',
            self.value)

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Tag translated from a referent tag")
        verbose_name_plural = _(u"Tags translated")


@python_2_unicode_compatible
class TagGoogleMaps(TagBase):
    place_id = models.CharField(max_length=100, default=u'', null=True,
                                blank=True)

    lat = models.DecimalField(default=None, null=True, blank=True,
                              max_digits=19, decimal_places=10)

    lng = models.DecimalField(default=None, null=True, blank=True,
                              max_digits=19, decimal_places=10)

    # https://developers.google.com/maps/documentation/
    # geocoding/intro?hl=fr#Results
    # viewport contient la fenêtre d'affichage recommandée pour
    # l'affichage du résultat renvoyé, spécifié sous la forme de deux valeurs
    # latitude,longitude définissant les angles southwest et northeast de
    # la zone de délimitation de la fenêtre d'affichage.
    # La fenêtre d'affichage est généralement utilisée pour encadrer un
    # résultat présenté à l'utilisateur.
    viewport_northeast_lat = models.DecimalField(default=None, null=True,
                                                 blank=True,
                                                 max_digits=19,
                                                 decimal_places=10)
    viewport_northeast_lng = models.DecimalField(default=None, null=True,
                                                 blank=True,
                                                 max_digits=19,
                                                 decimal_places=10)
    viewport_southwest_lat = models.DecimalField(default=None, null=True,
                                                 blank=True,
                                                 max_digits=19,
                                                 decimal_places=10)
    viewport_southwest_lng = models.DecimalField(default=None, null=True,
                                                 blank=True,
                                                 max_digits=19,
                                                 decimal_places=10)

    def __str__(self):
        return _(u'{} (lat: {}, lng: {})').format(
            self.description,
            self.lat if self.lat else u'?', self.lng if self.lng else u'?')

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Tag google maps referent")
        verbose_name_plural = _(u"Tags google maps referents")


class GoogleException(Exception):
    pass


@python_2_unicode_compatible
class TagGoogleMapsTraduit(BaseModel):
    tag_google_maps = models.ForeignKey(
        TagGoogleMaps, default=None, blank=True, null=True,
        help_text=_(u"Position de référence"),
        related_name='tag_google_maps')
    langue = models.ForeignKey(Langue, default=None, blank=True, null=True)
    # formatted_address selon les langues :
    # 'en' : "Beijing, Beijing, China", 'fr' : "P\u00e9kin, P\u00e9kin, Chine"
    formatted_address = models.CharField(max_length=200, default=u'', null=True,
                                         blank=True)

    # GMAPS_URL = 'http://maps.google.com/maps/api/geocode/json'
    # (!) url d'auto complete pour avoir des SUGGESTIONS google :
    # GMAPS_URL = u'https://' \
    #             u'maps.googleapis.com/maps/api/place/autocomplete/json'
    # (!) url pour chercher des places existantes :
    GMAPS_URL = 'https://maps.googleapis.com/maps/' \
                'api/place/textsearch/json'

    @staticmethod
    def make_cache_via_google_maps(text, locale):
        # Deux exemples pour mémo, à supprimer quand code fini :
        #
        # geocode(self, {                      geocode(self, {
        #     'input': u'Beijing, China',          'input': u'Pékin, Chine',
        #     'language': u'en',                   'language': u'fr',
        # })                                   })
        geo_args = {
            'input': text,
            'language': locale,
            # clé cogofly, compte cogofly@gmail.com, projet cogofly :
            # clé *Serveur* ne fonctionne pas :
            # 'key': u'AIzaSyC-05bQU8KfMuvr23-VmqROV_OKGizhdiM'
            # clé *Client* fonctionne :
            'key': u'AIzaSyCc0zrgx2mk-YPqzUvvpv4anNNWbMMk9EQ'

        }
        # Tout convertir en unicode
        str_geo_args = {}
        for k, v in geo_args.iteritems():
            str_geo_args[k] = ftfy.fix_encoding(unicode(v)).encode('utf-8')

        url = TagGoogleMapsTraduit.GMAPS_URL + '?' + urlencode(str_geo_args)
        print url
        request = urllib2.Request(url, headers={
            # "Referer": "http://www.cogofly.com/",
            "Referer": "http://cogofly.com",
            "userIp": "62.210.178.49"
        })
        print request
        handle = urllib2.urlopen(request).read()
        result = simplejson.loads(handle)
        print('src')
        print(geo_args)
        print('result')
        print(simplejson.dumps(result, indent=4))

        print(u"result['status'] -> {}".format(result['status']))
        # "OK"               indique qu'aucune erreur n'est survenue, que
        #                    l'adresse a été analysée et qu'au moins un
        #                    géocode a été trouvé.
        # "ZERO_RESULTS"     indique que le géocode a réussi mais n'a renvoyé
        #                    aucun résultat. Cela peut se produire si le
        #                    géocodeur a reçu un paramètre address inexistant.
        # "OVER_QUERY_LIMIT" indique que vous avez dépassé votre quota.
        # "REQUEST_DENIED"   indique que votre requête a été rejetée.
        # "INVALID_REQUEST"  indique généralement qu'il manque un élément
        #                    (address, components ou latlng) de la requête.
        # "UNKNOWN_ERROR"    indique que la requête n'a pas pu être traitée
        #                    en raison d'une erreur de serveur.
        #                    Si vous essayez à nouveau, la requête pourrait
        #                    aboutir.
        if result['status'] == "REQUEST_DENIED":
            # RAF : envoyer un mail
            raise Exception(_(u"We have a technical error. "
                              u"Please try again."))

        # Si même google trouve pas on arrête tout :
        if not len(result['results']):
            raise GoogleException(_(u"Google didn't find a town/country "
                                    u"with this name"))

        # 1 - aller chercher si on l'a en base :
        tag = None
        formatted_address = None
        for place in result['results']:
            try:
                tag = TagGoogleMaps.objects.get(
                    place_id__exact=place['place_id'])
                formatted_address = place.get('formatted_address')
            except TagGoogleMaps.DoesNotExist:
                pass
        if tag is None:
            # Prendre le premier résultat qui est souvent le bon
            place = result['results'][0]
            formatted_address = place.get('formatted_address')
            description = place.get('name', _(u'No name from google maps'))
            # Pas trouvé en base, créer position référence = TagGoogleMaps
            if not place.get('geometry'):  # devrait jamais arriver :
                raise GoogleException(_(u"Google didn't provide a location for "
                                        u"this town/country with this name"))

            def _g(tab, args):
                print tab, args
                if tab.get(args[0]) is None:
                    return None
                if len(args) > 1:
                    return _g(tab[args[0]], args[1:])
                return tab.get(args[0])
            g = place['geometry']
            tag = TagGoogleMaps.objects.create(
                type_tag=TagBase.TYPE_GOOGLE_MAP,
                description=description,
                place_id=place['place_id'],
                lat=_g(g, ['location', 'lat']),
                lng=_g(g, ['location', 'lng']),
                viewport_northeast_lat=_g(g, ['viewport', 'northeast', 'lat']),
                viewport_northeast_lng=_g(g, ['viewport', 'northeast', 'lng']),
                viewport_southwest_lat=_g(g, ['viewport', 'southwest', 'lat']),
                viewport_southwest_lng=_g(g, ['viewport', 'southwest', 'lng']),
            )
            tag.save()

        # arrivé ici, tag vaut forcément quelque chose
        # Si on a appelé cette fonction en cours, c'est que TagGoogleMapsTraduit
        # n'avait pas renvoyé d'enregistrement
        # -> le créer et le renvoyer
        tt = TagGoogleMapsTraduit.objects.create(
            tag_google_maps=tag,
            langue=Langue.objects.get(locale__exact=locale),
            # formatted_address selon les langues :
            # 'en' : "Beijing, Beijing, China",
            # 'fr' : "P\u00e9kin, P\u00e9kin, Chine"
            formatted_address=formatted_address)
        tt.save()
        if text != formatted_address:
            # Le texte entré par l'utilisateur n'est pas le même que le retour
            # google, enregistrer les deux :
            tt = TagGoogleMapsTraduit.objects.create(
                tag_google_maps=tag,
                langue=Langue.objects.get(locale__exact=locale),
                formatted_address=text)
            tt.save()
        return tt
        # Infos que je n'ai pas gardé en cache (inutiles ici)
        # "results": [
        #     {
        #         "name": "Paris",
        #         "reference": "Cn... blabla on s'en fout...bpn8",
        #         "types": [
        #             "locality",
        #             "political"
        #         ],
        #         "icon": "url image d'une pin pour pointer"
        #     }
        # ]

    def __str__(self):
        return u'{} - {} ({}) -> {}'.format(
            self.id,
            str(self.tag_google_maps) if self.tag_google_maps else u'(?)',
            self.langue.locale if self.langue else u'(?)',
            self.formatted_address)

    class Meta(BaseTranslatableModel.Meta):
        verbose_name = _(u"Tag google maps of a place in a language")
        verbose_name_plural = _(u"Tags google maps of a place in a language")
