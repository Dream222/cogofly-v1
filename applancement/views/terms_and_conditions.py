# coding=UTF-8
# Politique d'utilisation des données

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _


class TermsAndConditionsView(View):
    template_name = 'static/terms_and_conditions.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'tac_title': _(u'Cogofly - Terms and Conditions'),
            'tac_contact_us': _(
                u'If you require any more information or have any questions '
                u'about our Terms and Conditions, please feel free to contact '
                u'us by email by clicking '
                u'<a href="mailto:cogofly@gmail.com" target="_blank">'
                u'here '
                u'</a>'),
            'tac_introduction': _(u'Introduction'),
            'tac_introduction_1': _(
                u'These terms and conditions govern your use of this website;'
                u'by using this website, you accept these terms and conditions '
                u'in full and without reservation. If you disagree with these '
                u'terms and conditions or any part of these terms and '
                u'conditions, you must not use this website.'),
            'tac_introduction_2': _(
                u'You must be at least 18 [eighteen] years of age to use this '
                u'website. By using this website and by agreeing to these '
                u'terms and conditions, you warrant and represent that you are '
                u'at least 18 years of age.'),
            'tac_licence': _(u'License to use website'),
            'tac_licence_1': _(
                u'Unless otherwise stated,'
                u'<a href="/" target="_blank">www.cogofly.com</a>'
                u'and/or its licensors own the intellectual property rights '
                u'published on this website and materials used on '
                u'<a href="/" target="_blank">www.cogofly.com</a>.'
                u'Subject to the license below, all these intellectual '
                u'property rights are reserved.'),
            'tac_licence_2': _(
                u'You may view, download for caching purposes only,'
                u'and print pages, files or other content from the website '
                u'for your own personal use, subject to the restrictions set '
                u'out below and elsewhere in these terms and conditions.'
            ),
            'tac_licence_you_must_not': {
                'title': _(
                    u'You must not:'
                ),
                'tab': [
                    _(u'republish material from this website in neither '
                      u'print nor digital media or documents (including '
                      u'republication on another website);'),
                    _(u'sell, rent or sub-license material from the website;'),
                    _(u'show any material from the website in public;'),
                    _(u'reproduce, duplicate, copy or otherwise exploit '
                      u'material on this website for a commercial purpose;'),
                    _(u'edit or otherwise modify any material on the website;'),
                    _(u'redistribute material from this website - except '
                      u'for content specifically and expressly made available '
                      u'for redistribution; or'),
                    _(u'republish or reproduce any part of this website '
                      u'through the use of iframes or screenscrapers.'),
                ],
            },
            'tac_content_redistribution': _(
                u'Where content is specifically made available for '
                u'redistribution, it may only be redistributed within your '
                u'organisation.'),
            'tac_acceptable_use': {
                'title': _(u'Acceptable use'),
                'tab': [
                    _(u'You must not use this website in any way that causes, '
                      u'or may cause, damage to the website or impairment of '
                      u'the availability or accessibility of '
                      u'<a href="/" target="_blank">www.cogofly.com</a> '
                      u'or in any way which is unlawful, illegal, fraudulent '
                      u'or harmful, or in connection with any unlawful, '
                      u'illegal, fraudulent or harmful purpose or activity.'),
                    _(u'You must not use this website to copy, store, host, '
                      u'transmit, send, use, publish or distribute any '
                      u'material which consists of (or is linked to) any '
                      u'spyware, computer virus, Trojan horse, worm, keystroke '
                      u'logger, rootkit or other malicious computer software.'),
                    _(u'You must not conduct any systematic or automated '
                      u'data collection activities on or in relation to this '
                      u'website without <a href="/" target="_blank">'
                      u'www.cogofly.com\'s'
                      u'</a> express written consent. This includes:')
                ]
            },
            'tac_acceptable_this_includes_tab': [
                _(u'scraping'),
                _(u'data mining'),
                _(u'data extraction'),
                _(u'data harvesting'),
                _(u'"framing" (iframes)'),
                _(u'Article "Spinning"'),
            ],
            'tac_you_must_not_use_1':
                _(u'You must not use this website or any part of it to '
                  u'transmit or send unsolicited commercial communications.'),
            'tac_you_must_not_use_2':
                _(u'You must not use this website for any purposes related to '
                  u'marketing without the express written consent of '
                  u'<a href="/" target="_blank">www.cogofly.com</a>.'),
            'tac_restricted_access_title': _(u'Restricted access'),
            'tac_restricted_access_1':
                _(u'Access to certain areas of this '
                  u'website is restricted.'
                  u'<a href="/" target="_blank">www.cogofly.com</a> reserves '
                  u'the right to restrict access to certain areas of this '
                  u'website, or at our discretion, this entire website.'
                  u'<a href="/" target="_blank">www.cogofly.com</a> may change '
                  u'or modify this policy without notice.'),
            'tac_restricted_access_2':
                _(u'If <a href="/" target="_blank">www.cogofly.com</a>'
                  u'provides you with a user ID and password to enable you to '
                  u'access restricted areas of this website or other content '
                  u'or services, you must ensure that the user ID and password '
                  u'are kept confidential. You alone are responsible for your '
                  u'password and user ID security.'),
            'tac_restricted_access_3':
                _(u'<a href="/" target="_blank">www.cogofly.com</a> may '
                  u'disable your user ID and password at '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> sole '
                  u'discretion without notice or explanation.'),
            'tac_user_content': _(u'User content'),
            'tac_user_content_1':
                _(u'In these terms and conditions, "your user content"'
                  u'means material (including without limitation text, images,'
                  u'audio material, video material and audio-visual material) '
                  u'that you submit to this website, for whatever purpose.'),
            'tac_user_content_2':
                _(u'You grant to '
                  u'<a href="/" target="_blank">www.cogofly.com</a> a '
                  u'worldwide, irrevocable, non-exclusive, royalty-free '
                  u'license to use, reproduce, adapt, publish, translate and '
                  u'distribute your user content in any existing or future '
                  u'media.  You also grant to '
                  u'<a href="/" target="_blank">www.cogofly.com</a> the right '
                  u'to sub-license these rights, and the right to bring an '
                  u'action for infringement of these rights.'),
            'tac_user_content_3':
                _(u'Your user content must not be illegal or unlawful, must '
                  u'not infringe any third party\'s legal rights, and must not '
                  u'be capable of giving rise to legal action whether against '
                  u'you or '
                  u'<a href="/" target="_blank">www.cogofly.com</a> or a third '
                  u'party (in each case under any applicable law).'),
            'tac_user_content_4':
                _(u'You must not submit any user content to the website that '
                  u'is or has ever been the subject of any threatened or '
                  u'actual legal proceedings or other similar complaint.'),
            'tac_user_content_5':
                _(u'<a href="/" target="_blank">www.cogofly.com</a> reserves '
                  u'the right to edit or remove any material submitted to this '
                  u'website, or stored on the servers of '
                  u'<a href="/" target="_blank">www.cogofly.com</a>, or hosted '
                  u'or published upon this website.'),
            'tac_user_content_6':
                _(u'<a href="/" target="_blank">www.cogofly.com\'s</a> rights '
                  u'under these terms and conditions in relation to user '
                  u'content,'
                  u'<a href="/" target="_blank">www.cogofly.com</a> does not '
                  u'undertake to monitor the submission of such content to, or '
                  u'the publication of such content on, this website.'),
            'tac_no_warranties_title': _(u'No warranties'),
            'tac_no_warranties_1':
                _(u'This website is provided "as is" without any '
                  u'representations or warranties, express or implied.'
                  u'<a href="/" target="_blank">www.cogofly.com</a> makes no '
                  u'representations or warranties in relation to this website '
                  u'or the information and materials provided on this '
                  u'website.'),
            'tac_no_warranties_2':
                _(u'Without prejudice to the generality of the foregoing '
                  u'paragraph, <a href="/" target="_blank">www.cogofly.com</a>'
                  u' does not warrant that:'),
            'tac_no_warranties_2_1':
                _(u'this website will be constantly available, or available '
                  u'at all; or'),
            'tac_no_warranties_2_2':
                _(u'the information on this website is complete, true, '
                  u'accurate or non-misleading.'),
            'tac_no_warranties_3':
                _(u'Nothing on this website constitutes, or is meant to '
                  u'constitute, advice of any kind. If you require advice in '
                  u'relation to any legal, financial or medical matter you '
                  u'should consult an appropriate professional.'),
            'tac_liability_title': _(u'Limitations of liability'),
            'tac_liability_1':
                _(u'<a href="/" target="_blank">www.cogofly.com</a> will not '
                  u'be liable to you (whether under the law of contact, the '
                  u'law of torts or otherwise) in relation to the contents of, '
                  u'or use of, or otherwise in connection with, this website:'),
            'tac_liability_1_1':
                _(u'to the extent that the website is provided free-of-charge,'
                  u'for any direct loss;'),
            'tac_liability_1_2':
                _(u'for any indirect, special or consequential loss; or'),
            'tac_liability_1_3':
                _(u'for any business losses, loss of revenue, income, profits '
                  u'or anticipated savings, loss of contracts or business '
                  u'relationships, loss of reputation or goodwill, or loss or '
                  u'corruption of information or data.'),
            'tac_liability_2':
                _(u'These limitations of liability apply even if '
                  u'<a href="/" target="_blank">www.cogofly.com</a> has been '
                  u'expressly advised of the potential loss.'),
            'tac_exceptions_title': _(u'Exceptions'),
            'tac_exceptions_1':
                _(u'Nothing in this website disclaimer will exclude or limit '
                  u'any warranty implied by law that it would be unlawful to '
                  u'exclude or limit; and nothing in this website disclaimer '
                  u'will exclude or limit the liability of Cogofly in respect '
                  u'of any:'),
            'tac_exceptions_1_1':
                _(u'death or personal injury caused by the negligence of '
                  u'<a href="/" target="_blank">www.cogofly.com</a> or its '
                  u'agents, employees or shareholders/owners;'),
            'tac_exceptions_1_2':
                _(u'fraud or fraudulent misrepresentation on the part of '
                  u'<a href="/" target="_blank">www.cogofly.com</a>; or'),
            'tac_exceptions_1_3':
                _(u'matter which it would be illegal or unlawful for '
                  u'<a href="/" target="_blank">www.cogofly.com</a> to exclude '
                  u'or limit, or to attempt or purport to exclude or limit, '
                  u'its liability.'),
            'tac_reasonableness_title': _(u'Reasonableness'),
            'tac_reasonableness_1':
                _(u'By using this website, you agree that the exclusions and '
                  u'limitations of liability set out in this website '
                  u'disclaimer are reasonable.'),
            'tac_reasonableness_2':
                _(u'If you do not think they are reasonable, you must not use '
                  u'this website.'),
            'tac_other_parties_title': _(u'Other parties'),
            'tac_other_parties_1':
                _(u'You accept that, as a limited liability entity,'
                  u'<a href="/" target="_blank">www.cogofly.com</a> has an '
                  u'interest in limiting the personal liability of its '
                  u'officers and employees. You agree that you will not bring '
                  u'any claim personally against '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> '
                  u'officers or employees in respect of any losses you suffer '
                  u'in connection with the website.'),
            'tac_other_parties_2':
                _(u'Without prejudice to the foregoing paragraph, you agree '
                  u'that the limitations of warranties and liability set out '
                  u'in this website disclaimer will protect '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> '
                  u'officers, employees, agents, subsidiaries, successors, '
                  u'assigns and sub-contractors as well as '
                  u'<a href="/" target="_blank">www.cogofly.com</a>.'),
            'tac_unenforceable_provisions_title':
                _(u'Unenforceable provisions'),
            'tac_unenforceable_provisions_1':
                _(u'If any provision of this website disclaimer is, or is '
                  u'found to be, unenforceable under applicable law, that will '
                  u'not affect the enforceability of the other provisions of '
                  u'this website disclaimer.'),
            'tac_indemnity_title': _(u'Indemnity'),
            'tac_indemnity_1':
                _(u'You hereby indemnify '
                  u'<a href="/" target="_blank">www.cogofly.com</a> and '
                  u'undertake to keep '
                  u'<a href="/" target="_blank">www.cogofly.com</a>'
                  u'indemnified against any losses, damages, costs, '
                  u'liabilities and expenses (including without limitation '
                  u'legal expenses and any amounts paid by '
                  u'<a href="/" target="_blank">www.cogofly.com</a> to a third '
                  u'party in settlement of a claim or dispute on the advice of '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a>'
                  u'legal advisers) incurred or suffered by '
                  u'<a href="/" target="_blank">www.cogofly.com</a> arising '
                  u'out of any breach by you of any provision of these terms '
                  u'and conditions, or arising out of any claim that you have '
                  u'breached any provision of these terms and conditions.'),
            'tac_breaches_title': _(u'Breaches of these terms and conditions'),
            'tac_breaches_1':
                _(u'Without prejudice to '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> other '
                  u'rights under these terms and conditions, if you breach '
                  u'these terms and conditions in any way, '
                  u'<a href="/" target="_blank">www.cogofly.com</a> may take '
                  u'such action as '
                  u'<a href="/" target="_blank">www.cogofly.com</a> deems '
                  u'appropriate to deal with the breach, including suspending '
                  u'your access to the website, prohibiting you from accessing '
                  u'the website, blocking computers using your IP address from '
                  u'accessing the website, contacting your internet service '
                  u'provider to request that they block your access to the '
                  u'website and/or bringing court proceedings against you.'),
            'tac_variation_title': _(u'Variation'),
            'tac_variation_1':
                _(u'<a href="/" target="_blank">www.cogofly.com</a> may revise '
                  u'these terms and conditions from time-to-time. Revised '
                  u'terms and conditions will apply to the use of this website '
                  u'from the date of the publication of the revised terms and '
                  u'conditions on this website. Please check this page '
                  u'regularly to ensure you are familiar with the current '
                  u'version.'),
            'tac_assignment_title': _(u'Assignment'),
            'tac_assignment_1':
                _(u'<a href="/" target="_blank">www.cogofly.com</a> may '
                  u'transfer, sub-contract or otherwise deal with '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> rights '
                  u'and/or obligations under these terms and conditions '
                  u'without notifying you or obtaining your consent.'),
            'tac_assignment_2':
                _(u'You may not transfer, sub-contract or otherwise deal with '
                  u'your rights and/or obligations under these terms and '
                  u'conditions.'),
            'tac_severability_title': _(u'Severability'),
            'tac_severability_1':
                _(u'If a provision of these terms and conditions is determined '
                  u'by any court or other competent authority to be unlawful '
                  u'and/or unenforceable, the other provisions will continue '
                  u'in effect. If any unlawful and/or unenforceable provision '
                  u'would be lawful or enforceable if part of it were deleted, '
                  u'that part will be deemed to be deleted, and the rest of '
                  u'the provision will continue in effect.'),
            'tac_entire_agreement_title': _(u'Entire agreement'),
            'tac_entire_agreement_1':
                _(u'These terms and conditions, together with '
                  u'<a href="/" target="_blank">www.cogofly.com\'s</a> Privacy '
                  u'Policy constitute the entire agreement between you and '
                  u'<a href="/" target="_blank">www.cogofly.com</a> in '
                  u'relation to your use of this website, and supersede all '
                  u'previous agreements in respect of your use of this '
                  u'website.'),
            'tac_law_and_juridiction_title': _(u'Law and jurisdiction'),
            'tac_law_and_juridiction_1':
                _(u'These terms and conditions will be governed by and '
                  u'construed in accordance with the laws of Marseille '
                  u'(France), and any disputes relating to these terms and '
                  u'conditions will be subject to the exclusive jurisdiction '
                  u'of the courts of '
                  u'Marseille (France).'),
            'tac_information_technology':
                _(u'Information Technology must respect human identity, '
                  u'human rights, people’s private lives and freedom'),
            'tac_registered_CNIL':
                _(u'We are registered at the CNIL under file no. 1822236'),
        })
