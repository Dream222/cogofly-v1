# coding=UTF-8
import uuid

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.translation import ugettext as _
from django.views import generic

from app.forms.profile.profile_desactivate import ProfileDesactivateForm
from app.models.personne import Personne
from app.views.common import LoginRequiredMixin


class AccountDesactivateView(LoginRequiredMixin, generic.FormView):
    template_name = 'my_home/profile/base.html'
    form_class = ProfileDesactivateForm
    success_url = reverse_lazy('my_home_profile_edit')

    def get(self, request, *args, **kwargs):
        retour = super(AccountDesactivateView, self).get(request, *args,
                                                         **kwargs)
        # (!) il ne calcule la vue que si nécessaire !
        # -> forcer à le faire *AVANT* de supprimer le message :
        retour.render()
        if self.request.session.get('message', None):
            del self.request.session['message']
        return retour

    def get_object(self, queryset=None):
        p = Personne.objects.filter(
            user__pk__exact=self.request.user.pk
        ).all()
        return p[0] if len(p) else None

    def form_valid(self, form):
        # (!!) User est une clé étrangère = pas mis à jour automatiquement :
        i_agree_desactivate = form.cleaned_data.get('i_agree_desactivate')
        if i_agree_desactivate:
            self.request.session['message'] = [
                _(u'Account desactivated'),
                _(u'You have just deactivated your account and '
                  u'you will no longer be visible on this site.'),
                _(u'Please be advised that it can be reactivated at any '
                  u'time via the link that we have sent to the '
                  u'email address that you used when signing up. '),
                _(u'You can also reactivate your account via '
                  u'other social networks.'),
                _(u'Please feel free to come back in the near future '
                  u'and check out any new features which, we hope, '
                  u'will persuade you to share the adventure with us again.'),
                _(u'We would like to take this opportunity to thank you '
                  u'for using Cogofly and hope to see you again very soon.'),
                _(u'Click here to hide this message')]
            p = self.get_object()
            u = User.objects.get(pk=p.user.pk)
            p.est_active = False
            p.save()
            if 'development' not in self.request.META['HTTP_HOST']:
                site_web = u"{}://{}".format(
                    self.request.scheme, self.request.META['HTTP_HOST']
                )
                rand_str = str(uuid.uuid4())
                p.reactivate_code = rand_str
                p.save()
                EmailMessage(
                    subject=_(u'Account desactivated'),
                    body=u'{}\n{}\n{}\n{}\n{}\n{}{}\n{}'.format(
                        _(u'You have just deactivated your account and '
                          u'you will no longer be visible on this site.'),
                        _(u'We would like to take this opportunity to thank '
                          u'you for using Cogofly and hope to see '
                          u'you again very soon.'),
                        _(u'Please feel free to come back in the near future '
                          u'and check out any new features which, we hope, '
                          u'will persuade you to share the adventure '
                          u'with us again.'),
                        _(u'If you wish to reactivate it'),
                        _(u"click on the following link:"),
                        site_web,
                        reverse('my_home_profile_account_reactivate',
                                kwargs={'rand_str': rand_str}),
                        _(u'Thank you!'),
                    ),
                    from_email=u'register@cogofly.com',
                    to=[u.email],
                    # bcc=[u'cogofly+register@gmail.com'],
                    ).send()

        else:
            self.request.session['message'] = (
                _(u'No action!'),
                _(u'If you want to desactivate your account,'
                  u'please check "Yes".'))
        return super(AccountDesactivateView, self).form_valid(form)
#
