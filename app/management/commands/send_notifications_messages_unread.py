# coding=UTF-8

import random
import time
from datetime import timedelta

import re

from BeautifulSoup import BeautifulSoup
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.utils import translation
from django.utils.formats import get_format
from django.utils.timezone import make_aware
from django.utils.translation import ugettext_lazy as _
from django.utils.datetime_safe import datetime as django_datetime

from app.models.personne import Personne
from app.views.common_mixins import ActivitesMixin, InvitationsMixin, \
    LikesMixin, MessagesNotReadAndNotNotifiedByMailMixin


class Command(ActivitesMixin, MessagesNotReadAndNotNotifiedByMailMixin,
              InvitationsMixin, LikesMixin, BaseCommand):
    help = 'Send mail to notify members if they have new messages'
    can_import_settings = True

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.requires_system_checks = True  # test bd bien synchro, entre autres
        self.output_transaction = True  # dump visuel de SQL

    def add_arguments(self, parser):
        parser.add_argument('--fake',
                            action='store_true',
                            dest='fake',
                            default=None,
                            help='Just fake and send to Olivier Pons')

    def send_notifications_messages_unread(self, personne, nb_mails_sent, fake):

        if personne.site_language is None:
            return
        if personne.site_web is None:
            return

        translation.activate(personne.site_language.locale)
        f = get_format('DATE_INPUT_FORMATS')[1]

        message = []
        html_message = []

        def append_m(msg, html_msg=None, with_newline=True, position=None):
            if position is not None:
                message.insert(position, msg)
                if with_newline:
                    message.insert(position + 1, u"\n")
                html_message.insert(position,
                                    msg if html_msg is None else html_msg)
                if with_newline:
                    html_message.insert(position + 1, u"\n")
            else:
                if msg != u'':
                    message.append(msg)
                if with_newline:
                    message.append(u"\n")
                html_message.append(msg if html_msg is None else html_msg)
                if with_newline:
                    html_message.append(u"\n")

        # chercher les nouveaux messages
        convs = self.messages_not_read_and_not_notified_by_mail(personne)
        if convs.count() == 0:
            return False
        print(str(personne))
        for conversation in convs:
            for conv_message in conversation.messages_unread_for(personne):
                src = conv_message.src
                if conv_message.message is not None:
                    cleantext = BeautifulSoup(conv_message.message).text
                    if len(cleantext) > 80:
                        cleantext = u'{} (...)'.format(cleantext[:80])
                    append_m(_(u'{} sent you a '
                               u'message:').format(src.full_name()))
                    append_m(u'    {}'.format(cleantext))

        # ------------------
        # there should be always something to send, but just in case:
        mail_is_sent = False
        if len(message) > 2:

            # ------------------
            # message d'invite pour se connecter :
            append_m(
                str(_(u'If you would like to find out more, '
                      u'please log in via the following link:')),
                with_newline=False)
            append_m(
                u"{}{}".format(personne.site_web, reverse('my_home_index'))
            )

            # ------------------
            # message pour modifier l'abonnement :
            append_m(
                str(_(u'If you no longer wish to receive '
                      u'the Cogoflyer dashboard, '
                      u'or any other notifications, '
                      u'please click here:')),
                with_newline=False)
            append_m(u"{}{}".format(
                personne.site_web, reverse('my_home_profile_edit'))
            )
            append_m(
                str(_(u"And don't forget to click on: 'Change my parameters'"))
            )
            # output for me, with removing all double "\n"
            print(re.sub(u'\n+', u'\n',
                         u"\n".join([personne.user.email, ] + message)))
            send_mail(
                subject=_(u"Cogofly's message!"),
                message=u"\n".join(message).encode('utf-8'),
                html_message=u"<br/>\n".join(html_message).encode('utf-8'),
                from_email=u'contact@cogofly.com',
                recipient_list=[personne.user.email, ])
            # dont bother Franck with my mail:
            if personne.pk != 585:
                # send a copy all the time:
                send_mail(
                    subject=u' '.join([u"Cogofly's messages : ",
                                       personne.user.email]).encode('utf-8'),
                    message=u"\n".join([personne.user.email, ] +
                                       message).encode('utf-8'),
                    html_message=u"<br/>\n".join([personne.user.email, ] +
                                                 html_message).encode('utf-8'),
                    from_email=u'contact@cogofly.com',
                    recipient_list=['lagathufranck@gmail.com',])
            mail_is_sent = True

            # (!) Only save if production mode and not fake:
            import cogofly.settings
            if not cogofly.settings.DEBUG and not fake:
                # ok, sent -> remember it in the database:
                d = make_aware(django_datetime.now())
                for conversation in convs:
                    for conv_message in conversation.messages_unread_for(
                            personne):
                        conv_message.dst_message_unread_notified = d
                        conv_message.save()

                a = random.randint(1, 5)
                print(u'Mail sent at {}'.format(d))
                print(u'Sleeping {} s...'.format(a))
                time.sleep(a)

        translation.deactivate()
        return mail_is_sent

    def handle(self, *args, **options):
        d = make_aware(django_datetime.now())
        fake = options.get('fake', False)
        personnes_to_check = Personne.objects.filter(
            Q(est_detruit__isnull=True,
              date_v_fin__isnull=True,
              est_active__exact=True)
            & (Q(id__exact=585) if fake else Q())
        )
        nb_mails_sent = 0
        for personne in personnes_to_check:
            if self.send_notifications_messages_unread(personne,
                                                       nb_mails_sent,
                                                       fake):
                nb_mails_sent += 1
        # (!) dont use self.stdout.write(), not available here, just print:
        print(u'Successfully sent notifications of messages unread')
