from otree.api import Currency as c, currency_range, safe_json
from ._builtin import Page, WaitPage
from .models import Constants, Player
from  survey_example_appfolder.HelperFunctions import filtering, counting

#General Welcome and Quota Page
class Welcome(Page):
    form_model = Player
    form_fields = ['time_welcome', 'device_type', 'operating_system', 'screen_width', 'screen_height']

class QuotaPage(Page):
    form_model = Player
    form_fields = ['age', 'gender', 'federalstate', 'time_quotapage']
    def before_next_page(self):
        filtering(self)


#Social Movement Pages
class SmWelcome(Page):
    form_model = Player
    form_fields = ['sm_time_welcome'] 

class SmTreatmentPage(Page):
    form_model = Player
    form_fields = ['sm_time_treatmentpage', 'sm_participation']
    def vars_for_template(self):
        return {'sm_group_assignment': safe_json(self.player.sm_group_assignment),
                'device_type': safe_json(self.player.device_type)}

class SmParticipationPage(Page):
    form_model = Player
    form_fields=['sm_time_participationpage', 'sm_topic_relevance', 'sm_familiar_people', 'sm_booked', 'sm_transportation', 'sm_reach', 'sm_crowd', 
    'sm_polarization', 'sm_riots', 'sm_participation_else']

class SmPoliticalPage(Page):
    form_model = Player
    form_fields=['sm_time_politicalpage', 'sm_missing_knowledge', 'sm_own_knowledge', 'sm_general_knowledge',
    'sm_future', 'sm_unsure', 'sm_olddays']

class SmDemonstrationPage(Page):
    form_model = Player
    form_fields=['sm_time_demonstrationpage', 'sm_demonstration_change', 'sm_demonstration_democracy', 'sm_demonstration_views',
    'sm_politicians', 'sm_influence', 'sm_interests']

class SmEndPage(Page):
    form_model = Player
    form_fields=['sm_time_endpage']



# Ballot pages
class BaWelcome(Page):
    form_model = Player

    def before_next_page(self):
        self.group.counter += 1


# ballot as a table

class Ballot1(Page):
    form_model = Player
    form_fields = ['ba_ballot1']

    def vars_for_template(self):
        return {'ba_group_assignment': safe_json(self.player.ba_group_assignment)}


# ballot as a picture

class Ballot2(Page):
    form_model = Player
    form_fields = ['ba_ballot_pic1']

    def vars_for_template(self):
        return {'ba_group_assignment': safe_json(self.player.ba_group_assignment)}


# group 0 will get ideology1 page before ballot

class BaIdeology1(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos', 'ba_opinion1', 'ba_opinion2', 'ba_opinion3',
                   'ba_opinion4', 'ba_opinion5', 'ba_women1', 'ba_women2', 'ba_women3', 'ba_women4', 'ba_women5',
                   'ba_women6', 'ba_women7', 'ba_women8', 'ba_women9', 'ba_women10', 'ba_men1', 'ba_men2', 'ba_men3',
                   'ba_women4', 'ba_women5', 'ba_men6', 'ba_men7', 'ba_men8', 'ba_men9', 'ba_men10']

    def is_displayed(self):
        return self.player.ba_ideology_assignment == 0


# group 1 will get ideology2 page after ballot

class BaIdeology2(Page):
    form_model = Player
    form_fields = ['ba_positioning', 'ba_party_pos', 'ba_opinion1', 'ba_opinion2', 'ba_opinion3',
                   'ba_opinion4', 'ba_opinion5', 'ba_women1', 'ba_women2', 'ba_women3', 'ba_women4', 'ba_women5',
                   'ba_women6', 'ba_women7', 'ba_women8', 'ba_women9', 'ba_women10', 'ba_men1', 'ba_men2', 'ba_men3',
                   'ba_men4', 'ba_men5', 'ba_men6', 'ba_men7', 'ba_men8', 'ba_men9', 'ba_men10']

    def is_displayed(self):
        return self.player.ba_ideology_assignment == 1

class BaEndPage(Page):
    form_model = Player




# Charisma Pages
class ChIntro(Page):
    form_model = Player


class ChPictureAudio(Page):
    form_model = Player
    form_fields = ["ch_time_image_audio", "ch_im", "ch_audio", "ch_browserType"]
    def vars_for_template(self):
        return {'ch_group_assignment': self.player.ch_group_assignment}

class ChCheckRede(Page):
    form_model = Player
    form_fields = ["ch_time_check_rede" ,"ch_check_question", "reasonDescription"]

class ChSurvey_Charisma(Page):

    def vars_for_template(self):
        return{"ch_check_question": self.player.ch_check_question}

    # if participant didn't listen to speech, they won't get the questionnaire
    def is_displayed(self):
        return self.player.ch_check_question != 4 and self.player.ch_check_question != 5

    form_model = Player
    form_fields = ["ch_Q1", "ch_Q2", "ch_Q3", "ch_Q4", "ch_Q5", "ch_Q6", "ch_Q7", "ch_Q8", "ch_Q9", "ch_Q10", "ch_Q11",
                   "ch_Q12", "ch_time_survey_charisma"]

class ChSurvey_Charisma2(Page):

    def vars_for_template(self):
        return{"ch_check_question": self.player.ch_check_question}

    # if participant didn't listen to speech, they won't get the questionnaire
    def is_displayed(self):
        return self.player.ch_check_question != 4 and self.player.ch_check_question != 5

    form_model = Player
    form_fields = ["ch_Q1", "ch_Q2", "ch_Q3", "ch_Q4", "ch_Q5", "ch_Q6", "ch_Q7", "ch_Q8", "ch_Q9", "ch_Q10", "ch_Q11",
                   "ch_Q12", "ch_time_survey_charisma2"]


class ChEndPage(Page):
    form_model = Player
    form_fields = ["ch_end_of_survey"]


# control variables
class CvDemoPage(Page):
    form_model = Player
    form_fields = ['party_preference1', 'party_preference2', 'party_preference3', 'party_preference4',
                   'party_preference5', 'party_preference6', 'eligibility', 'participation']

class CvDemoPage2(Page):
    form_model = Player
    form_fields = ['demonstration_participation_allowed', 'demonstration_participation_notallowed',
                   'demonstration_participation_online', 'social_media']

class CvDemoPage3(Page):
    form_model = Player
    form_fields = ['household_income', 'general_education', 'ba_location', 'ba_immigration1',
                   'ba_immigration2', 'ba_immigration3']

    

#General EndPage
class EndPage(Page):
    form_model = Player
    form_fields=['time_endpage']
    def before_next_page(self): 
        counting(self)

class RedirectPage(Page):
    form_model = Player
    form_fields=[] #no time as it would not get recorded as the link is replaced (nothing written to database)
    def vars_for_template(self):
        return {"participant_label": safe_json(self.participant.label)}

page_sequence = [
                #general pages
                Welcome,
                QuotaPage,
                
                #Ballot Pages
                BaWelcome,
                BaIdeology1,
                Ballot2,
                BaIdeology2,
                BaEndPage,

                #Social MovementPages
                SmWelcome,
                SmTreatmentPage,
                SmParticipationPage,
                SmPoliticalPage,
                SmDemonstrationPage,
                SmEndPage,


                # Charisma Pages
                ChIntro,
                ChPictureAudio,
                ChCheckRede,
                ChSurvey_Charisma,
                ChSurvey_Charisma2,
                ChEndPage,

                # control variables
                CvDemoPage,
                CvDemoPage2,
                CvDemoPage3,

                #General EndPage
                EndPage,
                RedirectPage]