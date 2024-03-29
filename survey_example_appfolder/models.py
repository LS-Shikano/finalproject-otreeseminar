from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random


author = " "
doc = " "

class Constants(BaseConstants):
    name_in_url = 'survey-example'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    def creating_session(self):
        '''we are declaring the group assignment here'''
        for p in self.get_players():
            # social movement
            p.sm_group_assignment = random.Random().randint(1, 3)

            # ballot
            p.ba_group_assignment = random.Random().randint(0, 3)
            p.ba_ideology_assignment = random.Random().randint(0, 1)

            # charisma
            p.ch_group_assignment = random.Random().randint(1, 12)
            # group 1: casual/happy/easy
            # group 2: casual/happy/medium
            # group 3: casual/happy/hard
            # group 4: casual/neutral/easy
            # group 5: casual/neutral/medium
            # group 6: casual/neutral/hard
            # group 7: business/happy/easy
            # group 8: business/happy/medium
            # group 9: business/happy/hard
            # group 10: business/neutral/easy
            # group 11: business/neutral/medium
            # group 12: business/neutral/hard




class Group(BaseGroup):
    counter = models.IntegerField(initial=0)
    #gender groups
    gender_group_male = models.IntegerField(initial = 0)
    gender_group_female = models.IntegerField(initial = 0)
   
    #federalstate groups
    fd_1 = models.IntegerField(initial = 0)
    fd_2 = models.IntegerField(initial = 0)
    fd_3  = models.IntegerField(initial = 0)
    fd_4 = models.IntegerField(initial = 0)
    fd_5 = models.IntegerField(initial = 0)
    fd_6 = models.IntegerField(initial = 0)
    fd_7 = models.IntegerField(initial = 0)
    fd_8 = models.IntegerField(initial = 0)
    fd_9 = models.IntegerField(initial = 0)
    fd_10 = models.IntegerField(initial = 0)
    fd_11 = models.IntegerField(initial = 0)
    fd_12 = models.IntegerField(initial = 0)
    fd_13 = models.IntegerField(initial = 0)
    fd_14 = models.IntegerField(initial = 0)
    fd_15 = models.IntegerField(initial = 0)
    fd_16 = models.IntegerField(initial = 0)

    #age groups
    age_1 = models.IntegerField(initial = 0)
    age_2 = models.IntegerField(initial = 0)
    age_3 = models.IntegerField(initial = 0)
    age_4 = models.IntegerField(initial = 0)
    age_5 = models.IntegerField(initial = 0)
    age_6 = models.IntegerField(initial = 0)


class Player(BasePlayer):
    #META DATA
    device_type = models.IntegerField(initial = -999)
    operating_system = models.IntegerField(initial = -999)
    screen_width = models.IntegerField(initial = -999)
    screen_height = models.IntegerField(initial = -999)
    screenout = models.IntegerField(initial=0)
    quota = models.IntegerField(initial=0)
    age = models.IntegerField(initial = -999)
    gender = models.IntegerField(initial=-999)
    federalstate = models.IntegerField(initial=-999)

#General Pages
    time_welcome = models.StringField(initial=-999)
    time_quotapage = models.StringField(initial=-999)
    time_endpage = models.StringField(initial=-999)


# Social Movement (sm) variables
    #general variables
    sm_group_assignment = models.IntegerField(initial=-999)
    #SmTreatmentPage
    sm_time_treatmentpage = models.StringField(initial=-999)
    sm_participation = models.IntegerField(initial=-999, blank=True)
    def sm_participation_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie das Pflichtfeld."
    #SmParticipationPage
    sm_time_participationpage = models.StringField(initial=-999)
    sm_topic_relevance = models.IntegerField(initial = -999, blank=True)
    def sm_topic_relevance_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_familiar_people = models.IntegerField(initial=-999, blank=True)
    def sm_familiar_people_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_booked = models.IntegerField(initial=-999, blank=True)
    def sm_booked_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_transportation = models.IntegerField(initial = -999, blank=True)
    def sm_transportation_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_reach = models.IntegerField(initial=-999, blank=True)
    def sm_reach_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_number = models.IntegerField(initial=-999, blank=True)
    def sm_number_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_crowd = models.IntegerField(initial=-999, blank=True)
    def sm_crowd_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_polarization = models.IntegerField(initial=-999, blank=True)
    def sm_polarization_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_riots = models.IntegerField(initial=-999, blank=True)
    def sm_riots_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_participation_else = models.StringField(blank=True) #voluntary
    #SmPoliticalPage
    sm_time_politicalpage = models.StringField(initial=-999)
    sm_missing_knowledge = models.IntegerField(initial=-999, blank=True)
    def sm_rmissing_knowledge_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_own_knowledge = models.IntegerField(initial=-999, blank=True)
    def sm_own_knowledge_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_general_knowledge = models.IntegerField(initial=-999, blank=True)
    def sm_general_knowledge_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_future = models.IntegerField(initial=-999, blank=True)
    def sm_future_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_unsure = models.IntegerField(initial=-999, blank=True)
    def sm_unsure_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_olddays = models.IntegerField(initial=-999, blank=True)
    def sm_olddays_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    #SmDemonstrationPage
    sm_time_demonstrationpage = models.StringField(initial=-999)
    sm_demonstration_change = models.IntegerField(initial=-999, blank=True)
    def sm_demonstration_change_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_demonstration_democracy = models.IntegerField(initial=-999, blank=True)
    def sm_demonstration_democracy_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_demonstration_views = models.IntegerField(initial=-999, blank=True)
    def sm_demonstration_views_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_politicians = models.IntegerField(initial=-999, blank=True)
    def sm_politicians_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_influence = models.IntegerField(initial=-999, blank=True)
    def sm_influence_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    sm_interests = models.IntegerField(initial=-999, blank=True)
    def sm_interests_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."


    # Ballot variables
    ba_party = models.IntegerField()
    ba_party_else = models.StringField(initial = -999, blank = True) #voluntary
    ba_group_assignment = models.IntegerField()
    ba_ideology_assignment = models.IntegerField()
    ba_ballot1 = models.IntegerField(initial=-999)
    ba_ballot_pic1 = models.IntegerField(initial=-999)
    ba_positioning = models.IntegerField(initial=-999)
    ba_party_pos = models.IntegerField(initial=-999, blank = True) #voluntary
    ba_opinion1 = models.IntegerField(initial=-999)
    ba_opinion2 = models.IntegerField(initial=-999)
    ba_opinion3 = models.IntegerField(initial=-999)
    ba_opinion4 = models.IntegerField(initial=-999)
    ba_opinion5 = models.IntegerField(initial=-999)
    ba_women1 = models.IntegerField(initial=-999)
    ba_women2 = models.IntegerField(initial=-999)
    ba_women3 = models.IntegerField(initial=-999)
    ba_women4 = models.IntegerField(initial=-999)
    ba_women5 = models.IntegerField(initial=-999)
    ba_women6 = models.IntegerField(initial=-999)
    ba_women7 = models.IntegerField(initial=-999)
    ba_women8 = models.IntegerField(initial=-999)
    ba_women9 = models.IntegerField(initial=-999)
    ba_women10 = models.IntegerField(initial=-999)
    ba_men1 = models.IntegerField(initial=-999)
    ba_men2 = models.IntegerField(initial=-999)
    ba_men3 = models.IntegerField(initial=-999)
    ba_men4 = models.IntegerField(initial=-999)
    ba_men5 = models.IntegerField(initial=-999)
    ba_men6 = models.IntegerField(initial=-999)
    ba_men7 = models.IntegerField(initial=-999)
    ba_men8 = models.IntegerField(initial=-999)
    ba_men9 = models.IntegerField(initial=-999)
    ba_men10 = models.IntegerField(initial=-999)


    # Charisma (Ch) variables
    ch_group_assignment = models.IntegerField()

    # image/audi page
    ch_time_image_audio = models.StringField(initial='-999')
    ch_im = models.StringField(initial='-999')
    ch_audio = models.StringField(initial='-999')
    ch_browserType = models.StringField(initial='-999')

    # check speech
    ch_time_check_rede = models.StringField(initial='-999')
    ch_check_question = models.IntegerField(blank=True, initial='-999')
    reasonDescription = models.StringField(blank=True, label="")

    # error handling for the content questions, participants have to give an answer
    def ch_check_question_error_message(player, value):
        if value not in [1, 2, 3, 4, 5]:
            return "Bitte beantworten Sie die Frage"

    # survey charisma page
    ch_time_survey_charisma = models.StringField(initial='-999')
    ch_time_survey_charisma2 = models.StringField(initial='-999')
    ch_Q1 = models.IntegerField(blank=True, initial='-999')
    ch_Q2 = models.IntegerField(blank=True, initial='-999')
    ch_Q3 = models.IntegerField(blank=True, initial='-999')
    ch_Q4 = models.IntegerField(blank=True, initial='-999')
    ch_Q5 = models.IntegerField(blank=True, initial='-999')
    ch_Q6 = models.IntegerField(blank=True, initial='-999')
    ch_Q7 = models.IntegerField(blank=True, initial='-999')
    ch_Q8 = models.IntegerField(blank=True, initial='-999')
    ch_Q9 = models.IntegerField(blank=True, initial='-999')
    ch_Q10 = models.IntegerField(blank=True, initial='-999')
    ch_Q11 = models.IntegerField(blank=True, initial='-999')
    ch_Q12 = models.IntegerField(blank=True, initial='-999')

    # end page
    ch_end_of_survey = models.StringField(initial='-999')


    # control variables
    therm_spd = models.IntegerField(initial=-999, blank=True)
    def therm_spd_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_cdu = models.IntegerField(initial=-999, blank=True)
    def therm_cdu_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_csu = models.IntegerField(initial=-999, blank=True)
    def therm_csu_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_gruene = models.IntegerField(initial=-999, blank=True)
    def therm_gruene_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_fdp = models.IntegerField(initial=-999, blank=True)
    def therm_fdp_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_afd = models.IntegerField(initial=-999, blank=True)
    def therm_afd_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    therm_linke = models.IntegerField(initial=-999, blank=True)
    def therm_linke_error_message(player, value):
        if value not in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    household_income = models.IntegerField(blank=True)
    def household_income_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -888, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    general_education = models.IntegerField(initial=-999, blank=True)
    def general_education_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, 6, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    ba_location = models.IntegerField(initial=-999, blank=True)
    def ba_location_error_message(player, value):
        if value not in [1, 2, 3, 4, 5, -888]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    ba_immigration1 = models.StringField(blank=True)
    ba_immigration2 = models.StringField(blank=True)
    ba_immigration3 = models.StringField(blank=True)
    eligibility = models.IntegerField(initial=-999, blank=True)
    def eligibility_error_message(player, value):
        if value not in [1, 2, -888, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    participation = models.IntegerField(initial=-999, blank=True)
    def participation_error_message(player, value):
        if value not in [1, 2, -888, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    demonstration_participation_allowed = models.IntegerField(blank=True)
    def demonstration_participation_allowed_error_message(player, value):
        if value not in [1, 2, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    demonstration_participation_notallowed = models.IntegerField(blank=True)
    def demonstration_participation_notallowed_error_message(player, value):
        if value not in [1, 2, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    demonstration_participation_online = models.IntegerField(blank=True)
    def demonstration_participation_online_error_message(player, value):
        if value not in [1, 2, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."
    social_media = models.IntegerField(blank=True)
    def social_media_online_error_message(player, value):
        if value not in [1, 2, -999]:
            return "Bitte beantworten Sie alle Pflichtfelder."