# coding=UTF-8

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.timezone import make_aware
from django.views import generic
from django.utils.datetime_safe import datetime as django_datetime

from app.forms.profile.profile_delete import ProfileDeleteForm
from app.models.personne import Personne
from app.views.common import LoginRequiredMixin, CommonView


class AccountDeleteView(LoginRequiredMixin, generic.FormView):
    template_name = 'my_home/profile/base.html'
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('my_home_profile_edit')

    def get_context_data(self, **kwargs):
        # 'contact_id' = param de l'URL => dans kwargs => faire suivre kwargs :
        common = CommonView(self, **kwargs)
        context = super(AccountDeleteView, self).get_context_data(**kwargs)
        context['common'] = common.infos
        if self.request.session.get('message', None):
            context['message'] = self.request.session['message']
            del self.request.session['message']
        return context

    def get_object(self, queryset=None):
        p = Personne.objects.filter(
            user__pk__exact=self.request.user.pk
        ).all()
        return p[0] if len(p) else None

    def form_valid(self, form):
        # (!!) User est une clé étrangère = pas mis à jour automatiquement :
        i_agree_delete = form.cleaned_data.get('i_agree_delete')
        if i_agree_delete:
            self.request.session['message'] = [
                _(u'Account deleted'),
                _(u'You have just deleted your account.'),
                _(u'Please feel free to come back in the near future '
                  u'and check out any new features which, we hope, '
                  u'will persuade you to share the adventure with us again.'),
                _(u'We would like to take this opportunity to thank you '
                  u'for using Cogofly and hope to see you again very soon.'),
                _(u'Click here to hide this message')]
            p = self.get_object()
            u = User.objects.get(pk=p.user.pk)
            p.est_active = False
            p.est_detruit = make_aware(django_datetime.now())
            reason_delete = form.cleaned_data.get('reason_delete')
            p.reason_delete = reason_delete if reason_delete else None
            p.save()
            if 'development' not in self.request.META['HTTP_HOST']:
                EmailMessage(
                    subject=_(u'Account deleted'),
                    body=u'{}\n{}\n{}\n{}'.format(
                        _(u'You have just deleted your account.'),
                        _(u'We would like to take this opportunity to thank '
                          u'you for using Cogofly and hope to see '
                          u'you again very soon.'),
                        _(u'Please feel free to come back in the near future '
                          u'and check out any new features which, we hope, '
                          u'will persuade you to share the adventure '
                          u'with us again.'),
                        _(u'Thank you!'),
                    ),
                    from_email=u'register@cogofly.com',
                    to=[u.email],
                    bcc=[]).send()
                EmailMessage(
                    subject=_(u'Account deleted'),
                    body=u'{}\n{}'.format(
                        _(u'{} (email: {}) '
                          u'has just deleted his/her account.').format(
                            p.full_name(), u.email
                        ),
                        _(u'The reason for deletion is: {}').format(
                            reason_delete if reason_delete
                            else _(u'not precised')
                        ),
                    ),
                    from_email=u'contact@cogofly.com',
                    # to=[u'cogofly+support@gmail.com'],
                    bcc=[]).send()

            p.user.last_name = u'DELETE_{}'.format(
                p.user.last_name if p.user.last_name else u''
            )
            p.user.first_name = u'DELETE_{}'.format(
                p.user.first_name if p.user.first_name else u''
            )
            p.user.email = u'DELETE_{}'.format(
                p.user.email if p.user.email else u''
            )
            p.save()

        else:
            self.request.session['message'] = (
                _(u'No action!'),
                _(u'If you want to delete your account,'
                  u'please check "Yes".'))
        return super(AccountDeleteView, self).form_valid(form)
#
