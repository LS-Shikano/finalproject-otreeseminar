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
            p.sm_group_assignment = random.Random().randint(1, 3)


class Group(BaseGroup):
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
    # screenout = models.IntegerField(initial=0)
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
    #SmWelcome
    sm_time_welcome = models.StringField(initial=-999)
    #SmTreatmentPage
    sm_time_treatmentpage = models.StringField(initial=-999)
    sm_participation = models.IntegerField(initial=-999)
    #SmParticipationPage
    sm_time_participationpage = models.StringField(initial=-999)
    sm_topic_relevance = models.IntegerField(initial = -999)
    sm_familiar_people = models.IntegerField(initial=-999)
    sm_booked = models.IntegerField(initial=-999)
    sm_transportation = models.IntegerField(initial = -999)
    sm_reach = models.IntegerField(initial=-999)
    sm_crowd = models.IntegerField(initial=-999)
    sm_polarization = models.IntegerField(initial=-999)
    sm_riots = models.IntegerField(initial=-999)
    sm_participation_else = models.StringField(blank=True) #voluntary
    #SmPoliticalPage
    sm_time_politicalpage = models.StringField(initial=-999)
    sm_missing_knowledge = models.IntegerField(initial=-999)
    sm_own_knowledge = models.IntegerField(initial=-999)
    sm_general_knowledge = models.IntegerField(initial=-999)
    sm_future = models.IntegerField(initial=-999)
    sm_unsure = models.IntegerField(initial=-999)
    sm_olddays = models.IntegerField(initial=-999)
    #SmDemonstrationPage
    sm_time_demonstrationpage = models.StringField(initial=-999)
    sm_demonstration_change = models.IntegerField(initial=-999)
    sm_demonstration_democracy = models.IntegerField(initial=-999)
    sm_demonstration_views = models.IntegerField(initial=-999)
    sm_politicians = models.IntegerField(initial=-999)
    sm_influence = models.IntegerField(initial=-999)
    sm_interests = models.IntegerField(initial=-999)
    #EndPage
    sm_time_endpage = models.StringField(initial=-999)