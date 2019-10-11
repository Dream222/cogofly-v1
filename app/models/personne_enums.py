# coding=UTF-8

from django.utils.translation import ugettext_lazy as _


class PersonneEnums(object):

    VISIBILITE_TOUT_LE_MONDE = 1
    VISIBILITE_MES_AMIS = 2
    VISIBILITE_QUE_MOI = 3
    TAB_VISIBILITE = {
        VISIBILITE_TOUT_LE_MONDE: _(u"Everyone can see those informations"),
        VISIBILITE_MES_AMIS: _(u"Only my friends can see those informations"),
        VISIBILITE_QUE_MOI: _(u"Only me can see those informations"),
    }

    AGE_ENTRE_18_ET_25 = 1
    AGE_ENTRE_26_ET_35 = 2
    AGE_ENTRE_36_ET_45 = 3
    AGE_ENTRE_46_ET_55 = 4
    AGE_ENTRE_56_ET_PLUS = 5
    TAB_AGE = {
        AGE_ENTRE_18_ET_25: _(u"Between 18 and 25"),
        AGE_ENTRE_26_ET_35: _(u"Between 26 and 35"),
        AGE_ENTRE_36_ET_45: _(u"Between 36 and 45"),
        AGE_ENTRE_46_ET_55: _(u"Between 46 and 55"),
        AGE_ENTRE_56_ET_PLUS: _(u"56 and more"),
    }
    TAB_AGE_ECART = {
        AGE_ENTRE_18_ET_25:   {'min': 18, 'max': 25},
        AGE_ENTRE_26_ET_35:   {'min': 26, 'max': 35},
        AGE_ENTRE_36_ET_45:   {'min': 36, 'max': 45},
        AGE_ENTRE_46_ET_55:   {'min': 46, 'max': 55},
        AGE_ENTRE_56_ET_PLUS: {'min': 56, 'max': -1},
    }

    INVITATION_REFUS_NON = 1
    INVITATION_REFUS_NON_MERCI = 2
    INVITATION_REFUS_UNE_AUTRE_FOIS = 3
    INVITATION_REFUS_PAS_INTERESSE_JE = 4
    INVITATION_REFUS_PAS_INTERESSE_NOUS = 5
    INVITATION_REFUS_PAS_INTERESSE_MAINTENANT_JE = 6
    INVITATION_REFUS_PAS_INTERESSE_MAINTENANT_NOUS = 7
    INVITATION_REFUS_VOYAGE_PAS_JE = 8
    INVITATION_REFUS_VOYAGE_PAS_NOUS = 9
    INVITATION_REFUS_DEPLACE_PAS_JE = 10
    INVITATION_REFUS_DEPLACE_PAS_NOUS = 11
    INVITATION_REFUS_SOUHAITE_RESTER_SEUL_JE = 12
    INVITATION_REFUS_SOUHAITE_RESTER_SEUL_NOUS = 13
    INVITATION_REFUS_AUCUN_PROJET_VOYAGE_EN_COMMUN_NOUS = 14
    INVITATION_REFUS_AUCUN_PROJET_SORTIE_EN_COMMUN_NOUS = 15
    INVITATION_REFUS_AUCUN_PROJET_ACTIVITE_EN_COMMUN_NOUS = 16
    INVITATION_REFUS_PARLE_PAS_VOTRE_LANGUE_JE = 17
    INVITATION_REFUS_PARLE_PAS_VOTRE_LANGUE_NOUS = 18
    INVITATION_REFUS_PARLE_PAS_ANGLAIS_JE = 19
    INVITATION_REFUS_PARLE_PAS_ANGLAIS_NOUS = 20
    INVITATION_REFUS_UTILISER_MES_CONTACTS_JE = 21
    INVITATION_REFUS_UTILISER_MES_CONTACTS_NOUS = 22
    INVITATION_REFUS_CONTACTER_UNE_AUTRE_PERSONNE_JE = 23
    INVITATION_REFUS_CONTACTER_UNE_AUTRE_PERSONNE_NOUS = 24
    INVITATION_REFUS_CONTACTER_MESSAGE_JE = 25
    INVITATION_REFUS_CONTACTER_MESSAGE_NOUS = 26

    TAB_INVITATION = {
        INVITATION_REFUS_NON:
            _(u"No"),
        INVITATION_REFUS_NON_MERCI:
            _(u"No thank you"),
        INVITATION_REFUS_UNE_AUTRE_FOIS:
            _(u"Maybe another time"),
        INVITATION_REFUS_PAS_INTERESSE_JE:
            _(u"I am quite simply not interested"),
        INVITATION_REFUS_PAS_INTERESSE_NOUS:
            _(u"We are quite simply not interested"),
        INVITATION_REFUS_PAS_INTERESSE_MAINTENANT_JE:
            _(u"I am not interested for now"),
        INVITATION_REFUS_PAS_INTERESSE_MAINTENANT_NOUS:
            _(u"We are not interested for now"),
        INVITATION_REFUS_VOYAGE_PAS_JE:
            _(u"I don’t travel"),
        INVITATION_REFUS_VOYAGE_PAS_NOUS:
            _(u"We don’t travel"),
        INVITATION_REFUS_DEPLACE_PAS_JE:
            _(u"I don’t travel around"),
        INVITATION_REFUS_DEPLACE_PAS_NOUS:
            _(u"We don’t travel around"),
        INVITATION_REFUS_SOUHAITE_RESTER_SEUL_JE:
            _(u"I prefer to remain alone"),
        INVITATION_REFUS_SOUHAITE_RESTER_SEUL_NOUS:
            _(u"We prefer to remain alone"),
        INVITATION_REFUS_AUCUN_PROJET_VOYAGE_EN_COMMUN_NOUS:
            _(u"We have no travel plans in common"),
        INVITATION_REFUS_AUCUN_PROJET_SORTIE_EN_COMMUN_NOUS:
            _(u"We have no ideas in common for trips out"),
        INVITATION_REFUS_AUCUN_PROJET_ACTIVITE_EN_COMMUN_NOUS:
            _(u"We have nothing in common in terms of activities"),
        INVITATION_REFUS_PARLE_PAS_VOTRE_LANGUE_JE:
            _(u"I don’t speak your language"),
        INVITATION_REFUS_PARLE_PAS_VOTRE_LANGUE_NOUS:
            _(u"We don’t speak your language"),
        INVITATION_REFUS_PARLE_PAS_ANGLAIS_JE:
            _(u"I don’t speak English"),
        INVITATION_REFUS_PARLE_PAS_ANGLAIS_NOUS:
            _(u"We don’t speak English"),
        INVITATION_REFUS_UTILISER_MES_CONTACTS_JE:
            _(u"I invite you to use my contacts"),
        INVITATION_REFUS_UTILISER_MES_CONTACTS_NOUS:
            _(u"We invite you to get in touch with our contacts"),
        INVITATION_REFUS_CONTACTER_UNE_AUTRE_PERSONNE_JE:
            _(u"I invite you to contact another contact"),
        INVITATION_REFUS_CONTACTER_UNE_AUTRE_PERSONNE_NOUS:
            _(u"We invite you to contact another person"),
        INVITATION_REFUS_CONTACTER_MESSAGE_JE:
            _(u"I invite you to contact me by private message"),
        INVITATION_REFUS_CONTACTER_MESSAGE_NOUS:
            _(u"We invite you to contact us by private message"),
    }

    RELATION_AMI = 0
    RELATION_CONNAISSANCE = 1
    RELATION_INVITATION_EN_COURS = 2
    RELATION_INVITATION_REFUSEE = 3
    RELATION_PARENT_ENFANT = 4
    RELATION_ENFANT_PARENT = 5
    RELATION_MARI_FEMME = 6
    RELATION_FEMME_MARI = 7
    RELATION_PROFESSEUR_ELEVE = 8
    RELATION_ELEVE_PROFESSEUR = 9
    RELATION_RETIREE = 10

    TAB_RELATIONS = {
        RELATION_AMI: _(u'friend'),
        RELATION_CONNAISSANCE: _(u'relationship'),
        RELATION_INVITATION_REFUSEE: _(u"invitation refused"),
        RELATION_INVITATION_EN_COURS: _(u'sent an invitation'),
        RELATION_PARENT_ENFANT: _(u'parent / child'),
        RELATION_ENFANT_PARENT: _(u'child / parent'),
        RELATION_MARI_FEMME: _(u'husband / wife'),
        RELATION_FEMME_MARI: _(u'wife / husband'),
        RELATION_PROFESSEUR_ELEVE: _(u'teacher / student'),
        RELATION_ELEVE_PROFESSEUR: _(u'student / teacher'),
        RELATION_RETIREE: _(u'remover / removed'),
    }
    TAB_RELATIONS_REVERSE = {
        RELATION_AMI: _(u'friend'),
        RELATION_CONNAISSANCE: _(u'relationship'),
        RELATION_INVITATION_REFUSEE: _(u"refused invitation"),
        RELATION_INVITATION_EN_COURS: _(u'received invitation'),
        RELATION_PARENT_ENFANT: _(u'child / parent'),
        RELATION_ENFANT_PARENT: _(u'parent / child'),
        RELATION_MARI_FEMME: _(u'wife / husband'),
        RELATION_FEMME_MARI: _(u'husband / wife'),
        RELATION_PROFESSEUR_ELEVE: _(u'student / teacher'),
        RELATION_ELEVE_PROFESSEUR: _(u'teacher / student'),
        RELATION_RETIREE: _(u'removed / remover'),
    }

    TAB_RELATIONS_YOU = {
        RELATION_AMI: _(u'You are friend with {}'),
        RELATION_CONNAISSANCE: _(u'{} is one of your friend'),
        RELATION_INVITATION_REFUSEE: _(u"{} declined your invitation"),
        RELATION_INVITATION_EN_COURS: _(u"Invitation sent to {}"),
        RELATION_PARENT_ENFANT: _(u'You are the parent of {}'),
        RELATION_ENFANT_PARENT: _(u'You are the child of {}'),
        RELATION_MARI_FEMME: _(u'You are the husband of {}'),
        RELATION_FEMME_MARI: _(u'You are the wife of {}'),
        RELATION_PROFESSEUR_ELEVE: _(u'You are the teacher of {}'),
        RELATION_ELEVE_PROFESSEUR: _(u'You are the student of {}'),
        RELATION_RETIREE: _(u'You have removed this relation'),
    }
    TAB_RELATIONS_REVERSE_YOU = {
        RELATION_AMI: _(u'You are friend with {}'),
        RELATION_CONNAISSANCE: _(u'{} is one of your friend'),
        RELATION_INVITATION_REFUSEE: _(u"You declined {}'s invitation"),
        RELATION_INVITATION_EN_COURS: _(u'You received an invitation from {}'),
        RELATION_PARENT_ENFANT: _(u'You are the child of {}'),
        RELATION_ENFANT_PARENT: _(u'You are the parent of {}'),
        RELATION_MARI_FEMME: _(u'You are the wife of {}'),
        RELATION_FEMME_MARI: _(u'You are the husband of {}'),
        RELATION_PROFESSEUR_ELEVE: _(u'You are the student of {}'),
        RELATION_ELEVE_PROFESSEUR: _(u'You are the teacher of {}'),
        RELATION_RETIREE: _(u'{} has removed the relation with you'),
    }

    TAB_RELATIONS_YOU_SHORT = {
        RELATION_AMI: _(u'You are a friend'),
        RELATION_CONNAISSANCE: _(u'He/she is one of your friend'),
        RELATION_INVITATION_REFUSEE: _(u"He/she declined your invitation"),
        RELATION_INVITATION_EN_COURS: _(u"Invitation sent"),
        RELATION_PARENT_ENFANT: _(u'You are a parent'),
        RELATION_ENFANT_PARENT: _(u'You are the child'),
        RELATION_MARI_FEMME: _(u'You are the husband'),
        RELATION_FEMME_MARI: _(u'You are the wife'),
        RELATION_PROFESSEUR_ELEVE: _(u'You are the teacher'),
        RELATION_ELEVE_PROFESSEUR: _(u'You are the student'),
        RELATION_RETIREE: _(u'You removed this relation'),
    }
    TAB_RELATIONS_REVERSE_YOU_SHORT = {
        RELATION_AMI: _(u'You are a friend'),
        RELATION_CONNAISSANCE: _(u'He/she is one of your friend'),
        RELATION_INVITATION_REFUSEE: _(u"You declined the invitation"),
        RELATION_INVITATION_EN_COURS: _(u'You received an invitation'),
        RELATION_PARENT_ENFANT: _(u'You are the child'),
        RELATION_ENFANT_PARENT: _(u'You are the parent'),
        RELATION_MARI_FEMME: _(u'You are the wife'),
        RELATION_FEMME_MARI: _(u'You are the husband'),
        RELATION_PROFESSEUR_ELEVE: _(u'You are a student'),
        RELATION_ELEVE_PROFESSEUR: _(u'You are a teacher'),
        RELATION_RETIREE: _(u'He/she has removed the relation'),
    }

    NEWSLETTER_CONFIGURATION_EVERY_DAY = 1
    NEWSLETTER_CONFIGURATION_EVERY_WEEK = 2
    NEWSLETTER_CONFIGURATION_EVERY_MONTH = 3
    NEWSLETTER_CONFIGURATION_NEVER = 4

    TAB_NEWSLETTER_CONFIGURATION = {
        NEWSLETTER_CONFIGURATION_EVERY_DAY: _(u'Every day'),
        NEWSLETTER_CONFIGURATION_EVERY_WEEK: _(u'Every week'),
        NEWSLETTER_CONFIGURATION_EVERY_MONTH: _(u'Every month'),
        NEWSLETTER_CONFIGURATION_NEVER: _(u'Never send newsletter'), }
    """
    Franck m'a donné toute une liste pour les choix, qui s'est agrandie dans
    le temps, je l'ai donc déplacée ici parce que sinon le code n'est
    plus maintenable :
    """

    ZODIAC_CUSTOM_CAPRICORN = 0
    ZODIAC_CUSTOM_AQUARIUS = 1
    ZODIAC_CUSTOM_PISCES = 2
    ZODIAC_CUSTOM_ARIES = 3
    ZODIAC_CUSTOM_TAURUS = 4
    ZODIAC_CUSTOM_GEMINI = 5
    ZODIAC_CUSTOM_CANCER = 6
    ZODIAC_CUSTOM_LEO = 7
    ZODIAC_CUSTOM_VIRGO = 8
    ZODIAC_CUSTOM_LIBRA = 9
    ZODIAC_CUSTOM_SCORPIO = 10
    ZODIAC_CUSTOM_SAGITTARIUS = 11
    ZODIAC_CUSTOM_NOT_PRECISED = 12

    TAB_CUSTOM_ZODIAC_SIGN = {
        ZODIAC_CUSTOM_NOT_PRECISED: _(u'Not precised'),
        ZODIAC_CUSTOM_CAPRICORN: _(u'Capricorn'),
        ZODIAC_CUSTOM_AQUARIUS: _(u'Aquarius'),
        ZODIAC_CUSTOM_PISCES: _(u'Pisces'),
        ZODIAC_CUSTOM_ARIES: _(u'Aries'),
        ZODIAC_CUSTOM_TAURUS: _(u'Taurus'),
        ZODIAC_CUSTOM_GEMINI: _(u'Gemini'),
        ZODIAC_CUSTOM_CANCER: _(u'Cancer'),
        ZODIAC_CUSTOM_LEO: _(u'Leo'),
        ZODIAC_CUSTOM_VIRGO: _(u'Virgo'),
        ZODIAC_CUSTOM_LIBRA: _(u'Libra'),
        ZODIAC_CUSTOM_SCORPIO: _(u'Scorpio'),
        ZODIAC_CUSTOM_SAGITTARIUS: _(u'Sagittarius'), }

    SEXE_HOMME = 1
    SEXE_FEMME = 2
    TAB_SEXE = {SEXE_HOMME: _(u'Male'),
                SEXE_FEMME: _(u'Female'), }

    EST_NON_FUMEUR = 0
    EST_FUMEUR = 1
    EST_FUMEUR_OCCASIONNEL = 2
    EST_FUMEUR_NOT_PRECISED = 3
    TAB_EST_FUMEUR = {EST_FUMEUR_NOT_PRECISED: _(u'Not precised'),
                      EST_NON_FUMEUR: _(u'Non-smoker'),
                      EST_FUMEUR: _(u'Smoker'),
                      EST_FUMEUR_OCCASIONNEL: _(u'Social smoker'), }

    STATUT_SOLO = 0
    # STATUT_GROUPE = 1
    # STATUT_COUPLE = 2
    # STATUT_FAMILY = 3
    TAB_STATUT = {STATUT_SOLO: _(u'Solo'),
                  # STATUT_GROUPE: _(u'Group'),
                  # STATUT_COUPLE: _(u'Couple'),
                  # STATUT_FAMILY: _(u'Family'),
                  }

    NIVEAU_ETUDE_PETITE_ENFANCE = 0
    NIVEAU_ETUDE_PRIMAIRE = 1
    NIVEAU_ETUDE_SECONDAIRE_1ER_CYCLE = 2
    NIVEAU_ETUDE_SECONDAIRE_2ND_CYCLE = 3
    NIVEAU_ETUDE_POST_SECONDAIRE = 4
    NIVEAU_ETUDE_SUPERIEUR_CYCLE_COURT = 5
    NIVEAU_ETUDE_SUPERIEUR_LICENCE = 6
    NIVEAU_ETUDE_MASTER = 7
    NIVEAU_ETUDE_DOCTORAT = 8
    NIVEAU_ETUDES_AUTRE = 9
    NIVEAU_ETUDES_NOT_PRECISED = 10
    TAB_NIVEAU_ETUDES = {
        NIVEAU_ETUDES_NOT_PRECISED: _(u'Not precised'),
        NIVEAU_ETUDE_PETITE_ENFANCE: _(
            u'Nursery school'),
        NIVEAU_ETUDE_PRIMAIRE: _(
            u'Primary education'),
        NIVEAU_ETUDE_SECONDAIRE_1ER_CYCLE: _(
            u'Lower secondary education'),
        NIVEAU_ETUDE_SECONDAIRE_2ND_CYCLE: _(
            u'Upper secondary education'),
        NIVEAU_ETUDE_POST_SECONDAIRE: _(
            u'Post-secondary non-tertiary education'),
        NIVEAU_ETUDE_SUPERIEUR_CYCLE_COURT: _(
            u'Short-cycle tertiary education'),
        NIVEAU_ETUDE_SUPERIEUR_LICENCE: _(
            u'Bachelor\'s Degree or equivalent level'),
        NIVEAU_ETUDE_MASTER: _(
            u'Master\'s Degree or equivalent level'),
        NIVEAU_ETUDE_DOCTORAT: _(
            u'Ph.D. or equivalent level'),
        NIVEAU_ETUDES_AUTRE: _(
            u'Other'), }

    PROFESSION_AGRICULTEUR = 0
    PROFESSION_ARTISAN = 1
    PROFESSION_ARTISTE = 2
    PROFESSION_CADRE = 3
    PROFESSION_CHAUFFEUR = 4
    PROFESSION_CHEF_D_ENTREPRISE = 5
    PROFESSION_CLERGE_RELIGIEUX = 6
    PROFESSION_COMMERCANT_ET_ASSIMILE = 7
    PROFESSION_CONTREMAITRE_AGENT_DE_MAITRISE = 8
    PROFESSION_DIRIGEANT = 9
    PROFESSION_EMPLOYE = 10
    PROFESSION_ETUDIANT = 11
    PROFESSION_FONCTIONNAIRE = 12
    PROFESSION_INGENIEUR = 13
    PROFESSION_INSTITUTEUR = 14
    PROFESSION_OUVRIER = 15
    PROFESSION_POLICIER_OU_MILITAIRE = 16
    PROFESSION_PROFESSEUR = 17
    PROFESSION_PROFESSION_LIBERALE = 18
    PROFESSION_RETRAITE = 19
    PROFESSION_SPORTIF = 20
    PROFESSION_TECHNICIEN = 21
    PROFESSION_NON_DIVULGUE = 22
    PROFESSION_SANS_EMPLOI = 23
    PROFESSION_AUTRE = 24
    PROFESSION_NOT_PRECISED = 25

    TAB_PROFESSION = {
        PROFESSION_NOT_PRECISED: _(u'Not precised'),
        PROFESSION_AGRICULTEUR: _(u'Farmer'),
        PROFESSION_ARTISAN: _(u'Craftsman'),
        PROFESSION_ARTISTE: _(u'Artist'),
        PROFESSION_CADRE: _(u'Manager'),
        PROFESSION_CHAUFFEUR: _(u'Driver'),
        PROFESSION_CHEF_D_ENTREPRISE: _(u'Chief Executive Officer'),
        PROFESSION_CLERGE_RELIGIEUX: _(u'Clergyman'),
        PROFESSION_COMMERCANT_ET_ASSIMILE: _(u'Independent retailer'),
        PROFESSION_CONTREMAITRE_AGENT_DE_MAITRISE: _(u'Foreman, supervisor'),
        PROFESSION_DIRIGEANT: _(u'Managing director'),
        PROFESSION_EMPLOYE: _(u'Employee'),
        PROFESSION_ETUDIANT: _(u'Student'),
        PROFESSION_FONCTIONNAIRE: _(u'Civil servant'),
        PROFESSION_INGENIEUR: _(u'Engineer'),
        PROFESSION_INSTITUTEUR: _(u'Primary schoolteacher'),
        PROFESSION_OUVRIER: _(u'Labourer'),
        PROFESSION_POLICIER_OU_MILITAIRE: _(u'Policeman or Soldier'),
        PROFESSION_PROFESSEUR: _(u'Teacher'),
        PROFESSION_PROFESSION_LIBERALE: _(u'Self-employed profession'),
        PROFESSION_RETRAITE: _(u'Pensioner'),
        PROFESSION_SPORTIF: _(u'Sportsman'),
        PROFESSION_TECHNICIEN: _(u'Technician'),
        PROFESSION_NON_DIVULGUE: _(u'Undisclosed'),
        PROFESSION_SANS_EMPLOI: _(u'Unemployed'),
        PROFESSION_AUTRE: _(u'Other'), }

    LANGUE_ALBANAIS = 0
    LANGUE_ALLEMAND = 1
    LANGUE_ANGLAIS = 2
    LANGUE_ARABE = 3
    LANGUE_ARMENIEN = 4
    LANGUE_BENGALI = 5
    LANGUE_CATALAN = 6
    LANGUE_CHINOIS = 7
    LANGUE_COREEN = 8
    LANGUE_CROATE = 9
    LANGUE_DANOIS = 10
    LANGUE_ESPAGNOL = 11
    LANGUE_FINNOIS = 12
    LANGUE_FRANCAIS = 13
    LANGUE_GREC = 14
    LANGUE_HONGROIS = 15
    LANGUE_ITALIEN = 16
    LANGUE_MALAIS = 17
    LANGUE_MONGOL = 18
    LANGUE_NEERLANDAIS = 19
    LANGUE_OCCITAN = 20
    LANGUE_PERSAN = 21
    LANGUE_PORTUGAIS = 22
    LANGUE_ROUMAIN = 23
    LANGUE_RUSSE = 24
    LANGUE_SERBE = 25
    LANGUE_SLOVAQUE = 26
    LANGUE_SLOVENE = 27
    LANGUE_SUEDOIS = 28
    LANGUE_TURC = 29
    LANGUE_AUTRE = 30
    TAB_LANGUE = {
        LANGUE_ALBANAIS: _(u'Albanian'),
        LANGUE_ALLEMAND: _(u'German'),
        LANGUE_ANGLAIS: _(u'English'),
        LANGUE_ARABE: _(u'Arabic'),
        LANGUE_ARMENIEN: _(u'Armenian'),
        LANGUE_BENGALI: _(u'Bengali'),
        LANGUE_CATALAN: _(u'Catalan'),
        LANGUE_CHINOIS: _(u'Chinese'),
        LANGUE_COREEN: _(u'Korean'),
        LANGUE_CROATE: _(u'Croatian'),
        LANGUE_DANOIS: _(u'Danish'),
        LANGUE_ESPAGNOL: _(u'Spanish'),
        LANGUE_FINNOIS: _(u'Finnish'),
        LANGUE_FRANCAIS: _(u'French'),
        LANGUE_GREC: _(u'Greek'),
        LANGUE_HONGROIS: _(u'Hungarian'),
        LANGUE_ITALIEN: _(u'Italian'),
        LANGUE_MALAIS: _(u'Malaysian'),
        LANGUE_MONGOL: _(u'Mongolian'),
        LANGUE_NEERLANDAIS: _(u'Dutch'),
        LANGUE_OCCITAN: _(u'Occitan'),
        LANGUE_PERSAN: _(u'Persian'),
        LANGUE_PORTUGAIS: _(u'Portuguese'),
        LANGUE_ROUMAIN: _(u'Romanian'),
        LANGUE_RUSSE: _(u'Russian'),
        LANGUE_SERBE: _(u'Serbian'),
        LANGUE_SLOVAQUE: _(u'Slovakian'),
        LANGUE_SLOVENE: _(u'Slovenian'),
        LANGUE_SUEDOIS: _(u'Swedish'),
        LANGUE_TURC: _(u'Turkish'),
        LANGUE_AUTRE: _(u'Other'),
    }

    HOW_DID_I_KNOW_COGOFLY_FACEBOOK = 1
    HOW_DID_I_KNOW_COGOFLY_GOOGLE = 2
    HOW_DID_I_KNOW_COGOFLY_GOOGLE_PLUS = 3
    HOW_DID_I_KNOW_COGOFLY_TWITTER = 4
    HOW_DID_I_KNOW_COGOFLY_FLYERS = 5
    HOW_DID_I_KNOW_COGOFLY_WORD_OF_MOUTH = 6
    HOW_DID_I_KNOW_COGOFLY_OTHER = 7

    TAB_HOW_DID_I_KNOW_COGOFLY = {
        HOW_DID_I_KNOW_COGOFLY_FACEBOOK: u'Facebook',
        HOW_DID_I_KNOW_COGOFLY_GOOGLE: u'Google',
        HOW_DID_I_KNOW_COGOFLY_GOOGLE_PLUS: u'Google Plus',
        HOW_DID_I_KNOW_COGOFLY_TWITTER: u'Twitter',
        HOW_DID_I_KNOW_COGOFLY_FLYERS: _(u'Flyers'),
        HOW_DID_I_KNOW_COGOFLY_WORD_OF_MOUTH: _(u'Word of mouth'),
        HOW_DID_I_KNOW_COGOFLY_OTHER: _(u'Other'),
    }
