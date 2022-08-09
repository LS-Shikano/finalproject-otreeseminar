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
    sm_group_assignment = models.IntegerField(initial=-999, blank=True)
    #SmWelcome
    sm_time_welcome = models.StringField(initial=-999, blank=True)
    #SmTreatmentPage
    sm_time_treatmentpage = models.StringField(initial=-999, blank=True)
    sm_participation = models.IntegerField(initial=-999, blank=True)
    #SmParticipationPage
    sm_time_participationpage = models.StringField(initial=-999, blank=True)
    sm_topic_relevance = models.IntegerField(initial = -999, blank=True)
    sm_familiar_people = models.IntegerField(initial=-999, blank=True)
    sm_booked = models.IntegerField(initial=-999, blank=True)
    sm_transportation = models.IntegerField(initial = -999, blank=True)
    sm_reach = models.IntegerField(initial=-999, blank=True)
    sm_number = models.IntegerField(initial=-999, blank=True)
    sm_crowd = models.IntegerField(initial=-999, blank=True)
    sm_polarization = models.IntegerField(initial=-999, blank=True)
    sm_riots = models.IntegerField(initial=-999, blank=True)
    sm_participation_else = models.StringField(blank=True) #optional
    #SmPoliticalPage
    sm_time_politicalpage = models.StringField(initial=-999, blank=True)
    sm_missing_knowledge = models.IntegerField(initial=-999, blank=True)
    sm_own_knowledge = models.IntegerField(initial=-999, blank=True)
    sm_general_knowledge = models.IntegerField(initial=-999, blank=True)
    sm_future = models.IntegerField(initial=-999, blank=True)
    sm_unsure = models.IntegerField(initial=-999, blank=True)
    sm_olddays = models.IntegerField(initial=-999, blank=True)
    #SmDemonstrationPage
    sm_time_demonstrationpage = models.StringField(initial=-999, blank=True)
    sm_demonstration_change = models.IntegerField(initial=-999, blank=True)
    sm_demonstration_democracy = models.IntegerField(initial=-999, blank=True)
    sm_demonstration_views = models.IntegerField(initial=-999, blank=True)
    sm_politicians = models.IntegerField(initial=-999, blank=True)
    sm_influence = models.IntegerField(initial=-999, blank=True)
    sm_interests = models.IntegerField(initial=-999, blank=True)


    # Ballot variables
    ba_party = models.IntegerField(blank=True)
    ba_group_assignment = models.IntegerField(blank=True)
    ba_ideology_assignment = models.IntegerField(blank=True)
    ba_ballot1 = models.IntegerField(initial=-999, blank=True)
    ba_ballot_pic1 = models.IntegerField(initial=-999, blank=True)
    ba_positioning = models.IntegerField(initial=-999, blank=True)
    ba_party_pos = models.IntegerField(initial=-999, blank=True)
    ba_opinion1 = models.IntegerField(initial=-999, blank=True)
    ba_opinion2 = models.IntegerField(initial=-999, blank=True)
    ba_opinion3 = models.IntegerField(initial=-999, blank=True)
    ba_opinion4 = models.IntegerField(initial=-999, blank=True)
    ba_opinion5 = models.IntegerField(initial=-999, blank=True)
    ba_women1 = models.IntegerField(initial=-999, blank=True)
    ba_women2 = models.IntegerField(initial=-999, blank=True)
    ba_women3 = models.IntegerField(initial=-999, blank=True)
    ba_women4 = models.IntegerField(initial=-999, blank=True)
    ba_women5 = models.IntegerField(initial=-999, blank=True)
    ba_women6 = models.IntegerField(initial=-999, blank=True)
    ba_women7 = models.IntegerField(initial=-999, blank=True)
    ba_women8 = models.IntegerField(initial=-999, blank=True)
    ba_women9 = models.IntegerField(initial=-999, blank=True)
    ba_women10 = models.IntegerField(initial=-999, blank=True)
    ba_men1 = models.IntegerField(initial=-999, blank=True)
    ba_men2 = models.IntegerField(initial=-999, blank=True)
    ba_men3 = models.IntegerField(initial=-999, blank=True)
    ba_men4 = models.IntegerField(initial=-999, blank=True)
    ba_men5 = models.IntegerField(initial=-999, blank=True)
    ba_men6 = models.IntegerField(initial=-999, blank=True)
    ba_men7 = models.IntegerField(initial=-999, blank=True)
    ba_men8 = models.IntegerField(initial=-999, blank=True)
    ba_men9 = models.IntegerField(initial=-999, blank=True)
    ba_men10 = models.IntegerField(initial=-999, blank=True)


    # Charisma (Ch) variables
    ch_group_assignment = models.IntegerField()

    # image/audi page
    ch_time_image_audio = models.StringField(initial='-999', blank=True)
    ch_im = models.StringField(initial='-999', blank=True)
    ch_audio = models.StringField(initial='-999', blank=True)
    ch_browserType = models.StringField(initial='-999', blank=True)

    # check speech
    ch_time_check_rede = models.StringField(initial='-999', blank=True)
    ch_check_question = models.IntegerField(blank=True, initial='-999') #optional
    reasonDescription = models.StringField(blank=True, label="") #optional

    # error handling for the content questions, participants have to give an answer
    # def ch_check_question_error_message(player, value):
    #     if value not in [1, 2, 3, 4, 5]:
    #         return "Bitte beantworten Sie die Frage"

    # survey charisma page
    ch_time_survey_charisma = models.StringField(initial='-999', blank=True)
    ch_time_survey_charisma2 = models.StringField(initial='-999', blank=True)
    ch_Q1 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q2 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q3 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q4 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q5 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q6 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q7 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q8 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q9 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q10 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q11 = models.IntegerField(blank=True, initial='-999') #optional
    ch_Q12 = models.IntegerField(blank=True, initial='-999') #optional

    # end page
    ch_end_of_survey = models.StringField(initial='-999', blank=True)


    # control variables
    therm_spd = models.IntegerField(initial=-999, blank=True)
    therm_cdu = models.IntegerField(initial=-999, blank=True)
    therm_csu = models.IntegerField(initial=-999, blank=True)
    therm_gruene = models.IntegerField(initial=-999, blank=True)
    therm_fdp = models.IntegerField(initial=-999, blank=True)
    therm_afd = models.IntegerField(initial=-999, blank=True)
    therm_linke = models.IntegerField(initial=-999, blank=True)
    household_income = models.IntegerField(initial=-999, blank=True)
    general_education = models.IntegerField(initial=-999, blank=True)
    ba_location = models.IntegerField(initial=-999, blank=True)
    ba_immigration1 = models.StringField(blank=True) #optional
    ba_immigration2 = models.StringField(blank=True) #optional
    ba_immigration3 = models.StringField(blank=True) #optional
    eligibility = models.IntegerField(initial=-999, blank=True)
    participation = models.IntegerField(initial=-999, blank=True)
    demonstration_participation_allowed = models.IntegerField(initial=-999, blank=True)
    demonstration_participation_notallowed = models.IntegerField(initial=-999, blank=True)
    demonstration_participation_online = models.IntegerField(initial=-999, blank=True)
    social_media = models.IntegerField(initial=-999, blank=True)