# coding=UTF-8
# Page statique : "À propos"

from django.shortcuts import render
from django.views.generic import View
from django.utils.translation import ugettext as _


class PrivacyPolicyView(View):
    template_name = 'static/privacy_policy.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'privacy_policy_title': _(u'Cogofly - Privacy policy'),
            'privacy_policy_data_protection':
                _(u'Data protection is of the utmost importance to'
                  u'<strong>COGOFLY</strong> (right after '
                  u'"<strong>COGOFLY</strong>"). '
                  u'The Privacy Policy in place supplements the Terms and '
                  u'Conditions of the website www.<strong>COGOFLY</strong>.com '
                  u'(referred to hereafter as "the Website"), governing the '
                  u'relationship between the user and <strong>COGOFLY</strong'
                  u'>. This Privacy Policy applies to all services provided on '
                  u'the Website. The French version of this Privacy Policy '
                  u'shall prevail over any other version. The user can contact '
                  u'<strong>COGOFLY</strong> by the following email: <strong>'
                  u'COGOFLY</strong>@gmail.com. By registering on the Website, '
                  u'the user consents to this Privacy Policy.'),
            'privacy_policy_1_collection':
                _(u'1. Collection of personal data:'),
            'privacy_policy_1_collection_details':
                _(u'<strong>COGOFLY</strong> collects, processes, and uses '
                  u'personal data about the users in accordance with French '
                  u'and Europe laws and statutes on data protection. This '
                  u'collection has been declared to the CNIL under number '
                  u'1822236v0. <strong>COGOFLY</strong> uses personal data in '
                  u'the exclusive goal of providing the user with the services '
                  u'described on the Website and in the Terms and Conditions. <'
                  u'strong>COGOFLY</strong> will never transfer Personal Data '
                  u'to third parties without the user\'s consent. The user has '
                  u'a right of access, rectification and opposition on his/her '
                  u'personal data. To exercise those rights, the user shall '
                  u'contact <strong>COGOFLY</strong> by the contact email.'),
            'privacy_policy_2_registration':
                _(u'2. Registration:'),
            'privacy_policy_2_registration_details':
                _(u'In order to become a user of the Website, it is necessary '
                  u'to first create an account on the Website. To create an '
                  u'account, the user is required to provide the following '
                  u'mandatory contact information:'),
            'privacy_policy_2_registration_details_enum': [
                _(u'For a "solo" account: email, password or social network '
                  u'account such as Facebook, Twitter, Instagram, Pinterest, '
                  u'LinkedIn, Viadeo, Google +, family name, first name, '
                  u'country and city of residence, country and city of birth, '
                  u'gender, date of birth, at least one place the user wishes '
                  u'to visit.'),
                _(u'For a group account: same information as for a "solo" '
                  u'account, but concerning at least two users (except for the '
                  u'users who are already registered in the Website).'),
                _(u'For a couple account: same information as for a "solo" '
                  u'account, but concerning both users of the couple (except '
                  u'if the two users who are already registered in the'
                  u'Website).'),
                _(u'For a family account: same information as for a "solo" '
                  u'account, but concerning all the users of the Family ('
                  u'except for the users who are already registered in the '
                  u'Website).')],
            'privacy_policy_3_profile_information':
                _(u'3. Profile Information and contents:'),
            'privacy_policy_3_profile_information_details':
                _(u'Once registered, the user may provide other optional '
                  u'pieces of information (profession, diplomas, languages, '
                  u'hobbies, and so on...). The user can also publish or post '
                  u'different contents on the Website. These pieces of '
                  u'information are collected by <strong>COGOFLY</strong> to '
                  u'provide the user with better services and more '
                  u'confidence.'),
            'privacy_policy_4_users_contacts':
                _(u'4. Information about the user\'s contacts:'),
            'privacy_policy_4_users_contacts_details_1':
                _(u'If the user chooses to invite other people to join his '
                  u'entity, he/she shall enter the last name, first name, and '
                  u'email addresses of the invitees, or just their email '
                  u'address and potentially a phone number, depending on the '
                  u'data required by the invitation. This data is used only to '
                  u'send the invitation email and other reminders. <strong>'
                  u'COGOFLY</strong> stores this information to send the '
                  u'invitation email and to register a contact connexion if '
                  u'the user\'s invitation is accepted.'),
            'privacy_policy_4_users_contacts_details_2':
                _(u'All information entered or uploaded about contacts is '
                  u'considered personal data for the application of this '
                  u'Privacy Policy.'),
            'privacy_policy_5_cookies':
                _(u'5. Cookies:'),
            'privacy_policy_5_cookies_details_1':
                _(u'<strong>COGOFLY</strong> uses cookies to identify the user '
                  u'during the course of his/her session and to recognise him/'
                  u'her as a user when he/she returns to the Website using the '
                  u'same computer and web browser. A cookie is a file stored '
                  u'on the user\'s computer tied to information about the '
                  u'user. <strong>COGOFLY</strong> uses session ID cookies to '
                  u'confirm that the user is logged in. These cookies '
                  u'terminate once the user closes the browser. By default, '
                  u'<strong>COGOFLY</strong> uses persistent cookies that '
                  u'store the user\'s login ID (but not the password) to make '
                  u'it easier for the user to log in when he/she comes back to '
                  u'the Website. These cookies will then store part of the '
                  u'login data in encrypted form. The user can remove or block '
                  u'these cookies using the settings in the browser if he/she '
                  u'wants to disable this convenience feature. Unfortunately, '
                  u'if the browser settings do not allow cookies, the user '
                  u'shall systematically give his user name and password to '
                  u'log on.'),
            'privacy_policy_5_cookies_details_2':
                _(u'<strong>COGOFLY</strong> also receives the IP address of '
                  u'the user\'s computer, the computer operating system and '
                  u'type of web browser he/she is using, as well as the name '
                  u'of the user\'s ISP.'),
            'privacy_policy_5_cookies_details_3':
                _(u'This data is saved in a log file and will be stored by. '
                  u'The information is used in anonymous form to analyse '
                  u'overall trends to help <strong>COGOFLY</strong> improve '
                  u'its service, e.g., <strong>COGOFLY</strong> may analyse on '
                  u'which days, at which time and when the Website are '
                  u'particularly frequented. The linkage between the '
                  u'user\'s IP address and his/her personally identifiable '
                  u'information is never shared with any third party without '
                  u'the user\'s permission except when required by law. '
                  u'<strong>COGOFLY</strong> reserves the right to review the '
                  u'log files from the last known IP address of the user where '
                  u'<strong>COGOFLY</strong> has reasonable cause to believe '
                  u'that the user is using the Website in breach of the '
                  u'Terms and Conditions or the applicable legislation. '
                  u'In doing this, <strong>COGOFLY</strong> protects other '
                  u'users, the safety of its user\'s '
                  u'data, as well as the Website and the services. Like the '
                  u'information the user enters at registration or in his/her '
                  u'profile, cookie and associated log file data is used to '
                  u'customise the use of the Website and to help the user to '
                  u'not type his user name and password again. By using the '
                  u'Website and/or registering with the Website, the user '
                  u'fully accepts the use of the above mentioned cookies and '
                  u'log files.'),
            'privacy_policy_6_viewable_datas':
                _(u'6. Viewable data:'),
            'privacy_policy_6_viewable_datas_1':
                _(u'When the user registers in the Website, he/she may choose '
                  u'by whom his/her profile information are viewable. Three '
                  u'choices are then available: profile Information can be '
                  u'viewable either by everybody or solely by the user\'s '
                  u'contacts/friends or solely by the user\'s himself/herself. '
                  u'The user may modify his/her choice at any time in the '
                  u'settings menu. However, the profile picture will always be '
                  u'viewable by everybody. This picture will be blurred when '
                  u'the profiles research succeeds, <strong>COGOFLY</strong> '
                  u'wishing to be clearly different from a dating website. If '
                  u'the user makes no choice when registering, the following '
                  u'rules apply by default:'),
            'privacy_policy_6_viewable_datas_2':
                _(u'Viewable by everybody: family name, first name, country'
                  u'/city of residence, country/city of birth, gender, date of '
                  u'birth, scholarship/diplomas, schools/universities, former '
                  u'country/city of residence, languages, current profession, '
                  u'current employer, former employers, types of licences, '
                  u'zodiacal sign, what the User has already visited/done, '
                  u'what the user wishes to visit/do, interests, hobbies, self-'
                  u'description, smoker, number of children, statute.'),
            'privacy_policy_6_viewable_datas_3':
                _(u'Viewable solely by the user: email address.'),
            'privacy_policy_7_sharing_information':
                _(u'7. Sharing information with other users of <strong>COGOFLY'
                  u'</strong> or third parties:'),
            'privacy_policy_7_sharing_information_details_1':
                _(u'Profile information is only available to other users of <'
                  u'strong>COGOFLY</strong> depending on the user\'s chosen '
                  u'individual privacy settings. Neither third parties ('
                  u'meaning not registered users) nor searching engines (eg : '
                  u'Google, Bing, Yahoo, etc…) have access to the user\'s '
                  u'profile information, contents and personal data. The user '
                  u'acknowledges that no security measures are perfect and '
                  u'that the user\'s personal data may become publicly '
                  u'available, in case of a website hacking for example, '
                  u'despite the efforts of <strong>COGOFLY</strong> '
                  u'to maintain security of the Website. '
                  u'<strong>COGOFLY</strong> cannot control '
                  u'the actions of other users with whom the user may shares '
                  u'data and information. Therefore, <strong>COGOFLY</strong> '
                  u'does not guarantee that personal data will not be viewed '
                  u'by unauthorised persons. <strong>COGOFLY</strong> is not '
                  u'responsible for circumvention of any privacy settings or '
                  u'security measures contained on the Website.'),
            'privacy_policy_7_sharing_information_details_2':
                _(u'The user also acknowledges that, even after removal, '
                  u'copies of personal data may remain viewable in cached and '
                  u'archived pages.'),
            'privacy_policy_8_emails_and_notifications':
                _(u'8. Emails, and Notifications to users:'),
            'privacy_policy_8_emails_and_notifications_details':
                _(u'<strong>COGOFLY</strong> regularly sends out notification '
                  u'messages and emails to all users of '
                  u'<strong>COGOFLY</strong>. This communication aims at '
                  u'informing the user about new features or events related '
                  u'to the Website, to received emails, to added friends, '
                  u'to "likes", and so on…<strong>COGOFLY</strong> may '
                  u'present new users of <strong>COGOFLY</strong> to the user. '
                  u'It may also be the case that '
                  u'<strong>COGOFLY</strong> presents the user as a '
                  u'possible contact to other users of '
                  u'<strong>COGOFLY</strong>. Finally, '
                  u'<strong>COGOFLY</strong> may inform the user about other '
                  u'users of <strong>COGOFLY</strong> who have visited the user'
                  u'\'s profile or vice versa, i.e., the user may be one of '
                  u'those users with regard to another user of '
                  u'<strong>COGOFLY</strong> whose profile the user has '
                  u'visited. Generally, the user may opt out of such '
                  u'notifications through his/her individual personal '
                  u'settings, though <strong>COGOFLY</strong> reserves the '
                  u'right to send the user notices about his/her account.'),
            'privacy_policy_9_forwarding_information':
                _(u'9. Forwarding information to third parties:'),
            'privacy_policy_9_forwarding_information_details_1':
                _(u'<strong>COGOFLY</strong> does not forward the user\'s '
                  u'personal data, his/her contents, or other information to '
                  u'third parties without the user\'s consent, except where <'
                  u'strong>COGOFLY</strong> believes such sharing is either 1) '
                  u'necessary to use the Website or, 2) legally required or, 3'
                  u') permitted by the user. For example, <strong>COGOFLY</'
                  u'strong> may forward personal data to service providers, to '
                  u'its partners or sponsors, to help <strong>COGOFLY</strong> '
                  u'offer a better service, a better access to and a better '
                  u'use of the Website as a whole.'),
            'privacy_policy_9_forwarding_information_details_2':
                _(u'<strong>COGOFLY</strong> may be required to disclose '
                  u'personal data by legal requests, such as court orders, in '
                  u'compliance with applicable laws and regulations. '
                  u'Additionally, <strong>COGOFLY</strong> may share '
                  u'information when <strong>COGOFLY</strong> believes it is '
                  u'necessary to comply with the law, to protect the interests '
                  u'or property of <strong>COGOFLY</strong>, to prevent fraud '
                  u'or other illegal activity perpetrated through the Website '
                  u'or using the <strong>COGOFLY</strong> name, or to prevent '
                  u'imminent damage. This may include sharing information with '
                  u'other companies, lawyers, government agencies. By using '
                  u'the Website or registering in the Website, the user allows '
                  u'<strong>COGOFLY</strong> to process and use his/her '
                  u'personal data for advertising or marketing purposes of '
                  u'partners of <strong>COGOFLY</strong> via the Website. '
                  u'Particularly, Personal Data may be used in order to tailor '
                  u'the advertisement presented to the user to his/her '
                  u'specific interests.'),
            'privacy_policy_10_miscellaneous':
                _(u'10. Miscellaneous:'),
            'privacy_policy_10_miscellaneous_1':
                _(u'10.1. Under Age:'),
            'privacy_policy_10_miscellaneous_1_details':
                _(u'Minors are not eligible to use the Website and are '
                  u'therefore not allowed to register and submit any personal '
                  u'information to <strong>COGOFLY</strong>. Parents and legal '
                  u'guardians are responsible for the protection of their '
                  u'children\'s privacy.'),
            'privacy_policy_10_miscellaneous_2':
                _(u'10.2. Links:'),
            'privacy_policy_10_miscellaneous_2_details':
                _(u'The Website may contain links to other websites. <strong>'
                  u'COGOFLY</strong> is not responsible for the privacy '
                  u'practices of other websites. <strong>COGOFLY</strong> '
                  u'encourages the User to be aware when he/she leaves the '
                  u'Website to read the privacy statements of each and every '
                  u'website that collects personally identifiable information. '
                  u'This Privacy Policy applies solely to information '
                  u'collected by <strong>COGOFLY</strong>.'),
            'privacy_policy_11_changing_information':
                _(u'11. Changing or removing information:'),
            'privacy_policy_11_changing_information_details':
                _(u"The user may control most personal information via the "
                  u"profile editing tools of his/her profile on the Website. "
                  u"The user may modify or delete any of his/her profile "
                  u"information except the mandatory information required "
                  u"during the registration process at any time by logging "
                  u"into his/her account. Information will be updated "
                  u"immediately, subject to have saved it. Users who wish to "
                  u"deactivate their account with <strong>COGOFLY</strong> "
                  u"should act as mentioned in article Deactivation or "
                  u"deletion of an account of the Terms and Conditions. In "
                  u"this case, <strong>COGOFLY</strong> will remove the "
                  u"user's "
                  u"name and other personally identifiable information from "
                  u"publicly viewable data. However, <strong>COGOFLY</strong> "
                  u"may retain certain data contributed by the user if it may "
                  u"be necessary to prevent fraud or future abuse, or for "
                  u"legitimate business purposes, such as statistical analysis "
                  u"of non-personally-identifiable data, or if required by law"
                  u". All retained data will continue to be subject to the "
                  u"terms of the Privacy Policy that the user has previously "
                  u"agreed to. Where the user makes use of the communication "
                  u"features of the service to share information with other "
                  u"users of <strong>COGOFLY</strong>, however, (e.g., sending "
                  u"a personal message to another user of "
                  u"<strong>COGOFLY</strong>) the user generally cannot remove "
                  u"such communications."),
            'privacy_policy_12_litigation':
                _(u'12. Litigation:'),
            'privacy_policy_12_litigation_details':
                _(u'Any dispute arising from the use of the Website is subject '
                  u'to this Privacy Policy and to the Terms and Conditions, '
                  u'including limitation of liability.'),
            'privacy_policy_13_modification':
                _(u'13. Modification of Privacy Policy:'),
            'privacy_policy_13_modification_details':
                _(u'<strong>COGOFLY</strong> reserves the right to amend this '
                  u'Privacy Policy at any time. <strong>COGOFLY</strong> shall '
                  u'give due notice of any amendments of this Privacy Policy '
                  u'to the user via the user\'s email address or by placing a '
                  u'notice in the user\'s personal inbox on the Website.'),
        })
