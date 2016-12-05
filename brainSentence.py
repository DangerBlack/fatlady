class BrainSentence:

    names = ['silvia','claudia','elf','alessandra','gaia','elena','sunti','giulia','morg','momo','filippo','diana','lorenzo','daffo']
    verbs = {
                "i'm":"saluta",
                'am':'saluta',
                'is':'saluta',
                'who are you':"introduci",
                'happy new year':"newyear",
                'what are you':"painting",
                'are you death':"no",
                'fuck':"lose",
                'tell me the riddle':"riddle",
                'twelve':"correct",
            }

    action = {
            "saluta":["salutaNAME.mp3","none"],
            "introduci":["introduci.mp3","happy"], #I'm Amaros Black from the glorius Black family, I'm a famous painter in my time, and now I'm just hanging around. Hoping not to have an hanghover...
            "newyear":["happynewyear.mp3","happy"],
            "painting":["painting.mp3","none"],#I'm just painting a naked lady, but it's hard sometimes remembering her face
            "no":["no.mp3","none"],
            "lose":["givepoint.mp3","angry"],
            "riddle":["riddle.mp3","none"],
            "correct":["correct.mp3","happy"]

    }

    emotion = ['none','happy','angry'];

    def __init__(self, sentence):
        self.sentence = sentence


    #Return a list of two [AUDIO_FILE_NAME,SPEAKING_EMOTION]
    #using the AUDIO_FILE_NAME you can reproduce those file
    #using the emotion you can better chose the correct scene
    def deduce(self):
        selected_verb = ''
        selected_name = ''
        selected_action = ''
        for v in self.verbs.keys():
            if(v in self.sentence):
                hasName = False
                for n in self.names:
                    if(n in self.sentence):
                        hasName=True
                        selected_verb = self.verbs[v]
                        selected_name = n
                        #print 'trovato['+v+','+n+']: '+self.verbs[v]+" -> "+n
                if(not hasName):
                    #print 'trovato['+v+']: '+self.verbs[v]
                    selected_verb = self.verbs[v]
        if("NAME" in self.action[selected_verb][0]):
            selected_action=[self.action[selected_verb][0].replace("NAME",selected_name),self.action[selected_verb][1]]
        else:
            selected_action=self.action[selected_verb]
        return selected_action

bs = BrainSentence('who are you')
print(bs.deduce())
bs = BrainSentence("hi i'm claudia")
print(bs.deduce())
bs = BrainSentence("hi i am claudia")
print(bs.deduce())
