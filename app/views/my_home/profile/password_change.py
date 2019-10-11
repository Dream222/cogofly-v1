# coding=UTF-8
from django.contrib import auth
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import generic

from app.forms.profile.profile_password import ProfilePasswordForm
from app.models.personne import Personne
from app.views.common import LoginRequiredMixin


class ChangePasswordView(LoginRequiredMixin, generic.FormView):
    template_name = 'my_home/profile/base.html'
    form_class = ProfilePasswordForm
    success_url = reverse_lazy('my_home_profile_edit')

    def get(self, request, *args, **kwargs):
        retour = super(ChangePasswordView, self).get(request, *args, **kwargs)
        # (!) il ne calcule la vue que si nécessaire !
        # -> forcer à le faire *AVANT* de supprimer le message :
        retour.render()
        if self.request.session.get('message', None):
            del self.request.session['message']
        return retour

    def get_object(self, queryset=None):
        try:
            return Personne.objects.get(user=self.request.user)
        except Personne.DoesNotExist:
            return None

    def form_valid(self, form):
        p = self.get_object()
        old = form.cleaned_data.get('old_password', u'')
        new1 = form.cleaned_data.get('new_password1', u'')
        new2 = form.cleaned_data.get('new_password2', u'')
        error = None
        if old != u'':
            if new1 == u'':
                error = _(u'New password missing')
            if new2 == u'':
                error = _(u'New password missing')
            if new1 != new2:
                error = _(u"The new password is not the same twice")
        elif not p.reset_password:
            error = _(u"The old password is missing")

        # si aucune erreur, reste à vérifier que l'ancien mot de passe est bon :
        if not error and not p.reset_password:
            if not p.user.check_password(old):
                error = _(u'Bad password')

        if not error:
            # ouf ! enfin on peut reset le mot de passe :
            p.reset_password = None
            p.save()
            p.user.set_password(new1)
            p.user.save()

            # Tricher ! Normalement, un reset password = déconnexion.
            # Comme c'est débile, je reconnecte automatiquement ici via mon
            # système d'authentification qui ne nécessite pas de mot de passe :
            user = auth.authenticate(username=p.user.username,
                                     secure=u'_.|._')
            if user is None:
                user = auth.authenticate(email=p.user.email,
                                         secure=u'_.|._')
            if user is not None:
                auth.login(self.request, user)
            self.request.session['message'] = [
                _(u"Account updated"),
                _(u"Your password has been changed."),
                _(u"Click here to hide this message")]
        else:
            self.request.session['message'] = [
                _(u"Your password has not been changed:"),
                error, _(u"Please try again"),
                _(u"Click here to hide this message")]
        return super(ChangePasswordView, self).form_valid(form)
