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
                #Charisma Pages
                
                #Social MovementPages
                SmWelcome,
                SmTreatmentPage,
                SmParticipationPage,
                SmPoliticalPage,
                SmDemonstrationPage,
                SmEndPage,
                #Ballot Pages

                #General EndPage
                EndPage,
                RedirectPage]