def filtering(self):
#DECLARING ALL THE SCREENOUTS
    #AGE QUOTA
    if self.player.age > 2004: # screen out under 18 year olds
        self.player.screenout = 1

    if self.player.age < 1943: # screen out older than 79
        self.player.screenout = 1


#DECLARING ALL THE QUOTA REACHED
#GENDER
    # if self.player.gender == 1 and self.group.gender_group_male >= 534:
    #         self.player.quota = 1
    if self.player.gender == 1 and self.group.gender_group_male >= 1:
        self.player.quota = 1

    if self.player.gender == 2 and self.group.gender_group_female >= 516:
            self.player.quota = 1
#AGEGROUPS
    if 1993 <= self.player.age <= 2004 and self.group.age_1 >= 182:
            #18-29: somebody born between 1993 and 2004 (inclusive of 1993 and 2004)
            self.player.quota = 1

    if 1983 <= self.player.age < 1993 and self.group.age_2 >= 182: 
            #30-39: somebody born between 1983 and 1992 (inclusive of 1983 and 1992)
            self.player.quota = 1
            
    if 1973 <= self.player.age < 1983 and self.group.age_3 >= 167:
            #40-49:somebody born between 1973 and 1982 (inclusive of 1973 and 1982)
            self.player.quota = 1

    if 1963 <= self.player.age < 1973 and self.group.age_4 >= 216:
            #50-59: somebody born between 1963 and 1972 (inclusive of 1963 and 1972)
            self.player.quota = 1

    if 1953 <= self.player.age < 1963 and self.group.age_5 >= 182:
            #60-69: somebody born between 1953 and 1962 (inclusive of 1953 and 1962)
            self.player.quota = 1

    if 1943 <= self.player.age < 1953 and self.group.age_6 >= 122:
            #70-79: somebody born between 1943 and 1952 inclusive of 1943 and 1952)
            self.player.quota = 1


#FEDERALSTATES    
    if self.player.federalstate == 1 and self.group.fd_1 >= 37: 
            #Schlewsweig-Holstein
            self.player.quota = 1

    if self.player.federalstate == 2 and self.group.fd_2 >= 23:
            #Hamburg
            self.player.quota = 1

    if self.player.federalstate == 3 and self.group.fd_3 >= 100:
            #Niedersachsen
            self.player.quota = 1

    if self.player.federalstate == 4 and self.group.fd_4 >= 9:
            #Bremen
            self.player.quota = 1

    if self.player.federalstate == 5 and self.group.fd_5 >= 226:
            #Nordrein-Westfalen
            self.player.quota = 1
    
    if self.player.federalstate == 6 and self.group.fd_6 >= 79:
            #Hessen
            self.player.quota = 1

    if self.player.federalstate == 7 and self.group.fd_7 >= 51:
            #Rheinland-Pfalz
            self.player.quota = 1

    if self.player.federalstate == 8 and self.group.fd_8 >= 139:
            #Baden-Württemberg
            self.player.quota = 1
    
    if self.player.federalstate == 9 and self.group.fd_9 >= 165:
            #Bayern
            self.player.quota = 1

    if self.player.federalstate == 10 and self.group.fd_10 >= 13:
            #Saarland
            self.player.quota = 1
    
    if self.player.federalstate == 11 and self.group.fd_11 >= 46:
            #Berlin
            self.player.quota = 1

    if self.player.federalstate == 12 and self.group.fd_12 >= 32:
            #Brandenburg
            self.player.quota = 1

    if self.player.federalstate == 13 and self.group.fd_13 >= 21:
            #Mecklenburg Vorpommern
            self.player.quota = 1

    if self.player.federalstate == 14 and self.group.fd_14 >= 53:
            #Sachsen
            self.player.quota = 1
    
    if self.player.federalstate == 15 and self.group.fd_15 >= 28:
            #Sachsen-Anhalt
            self.player.quota = 1

    if self.player.federalstate == 16 and self.group.fd_16 >= 28:
            #Thüringen
            self.player.quota = 1


def counting(self):
 #COUNTING UP THE QUOTAS
    if self.player.quota == 0: #self.player.screenout == 0 and

    #GENDER
        if self.player.gender == 1:  # MALE
            self.group.gender_group_male += 1

        if self.player.gender == 2:  # FEMALE
            self.group.gender_group_female += 1

    #AGE GROUPS
        if 1993 <= self.player.age <= 2004: # ages 18 - 29
            self.group.age_1 += 1

        if 1983 <= self.player.age < 1993: # ages 30- 39
            self.group.age_2 += 1
        
        if 1973 <= self.player.age < 1983: # ages 40- 49
            self.group.age_3 += 1
        
        if 1963 <= self.player.age < 1973: # ages 50- 59
            self.group.age_4 += 1
        
        if 1953 <= self.player.age < 1963: # ages 60 -69
            self.group.age_5 += 1

        if 1943 <= self.player.age < 1953: # ages 70 -79
            self.group.age_6 += 1

    # FEDERAL STATE QUOTA

        if self.player.federalstate == 1:  # Schleswig-Holstein
            self.group.fd_1 += 1
        
        if self.player.federalstate == 2:  # Hamburg
            self.group.fd_2 += 1

        if self.player.federalstate == 3:  # Niedersachen
            self.group.fd_3 += 1
        
        if self.player.federalstate == 4:  # Bremen
            self.group.fd_4 += 1

        if self.player.federalstate == 5:  # Nordrein-Westfalen
            self.group.fd_5 += 1

        if self.player.federalstate == 6:  # Hessen
            self.group.fd_6 += 1
        
        if self.player.federalstate == 7:  # Rheinland-Pfalz
            self.group.fd_7 += 1
        
        if self.player.federalstate == 8:  # Baden-Württemberg
            self.group.fd_8 += 1
        
        if self.player.federalstate == 9:  # Bayern
            self.group.fd_9 += 1
        
        if self.player.federalstate == 10:  # Saarland
            self.group.fd_10 += 1
        
        if self.player.federalstate == 11:  # Berlin
            self.group.fd_11 += 1
        
        if self.player.federalstate == 12:  # Brandenburg
            self.group.fd_12 += 1
        
        if self.player.federalstate == 13:  # Mecklenburg-Vorpommern
            self.group.fd_13 += 1

        if self.player.federalstate == 14:  # Sachsen
            self.group.fd_14 += 1

        if self.player.federalstate == 15:  # Sachsen-Anhalt 
            self.group.fd_15 += 1
       
        if self.player.federalstate == 16:  # Thüringen
            self.group.fd_16 += 1     