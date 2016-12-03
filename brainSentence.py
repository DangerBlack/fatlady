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
            "saluta":["Hello [], nice to meet you, I'm Amros Black named as the raven.","none"],
            "introduci":["introduci","happy"], #I'm Amaros Black from the glorius Black family, I'm a famous painter in my time, and now I'm just hanging around. Hoping not to have an hanghover...
            "newyear":["happy new year","happy"],
            "painting":["I'm painting a naked lady","none"],#I'm just painting a naked lady, but it's hard sometimes remembering her face
            "no":["Absolutely no","none"],
            "lose":["Any prefect around I wanna slipt 10 point to this ugly guy","angry"],
            "riddle":["How many uses of dragon blood did DUmbledore discover?","none"],
            "correct":["you are right! good boy","happy"]

    }

    emotion = ['none','happy','angry'];

    def __init__(self, sentence):
        self.sentence = sentence

    def deduce(self):
        for v in self.verbs.keys():
            if(v in self.sentence):
                hasName = False
                for n in self.names:
                    if(n in self.sentence):
                        hasName=True
                        print 'trovato['+v+','+n+']: '+self.verbs[v]+" -> "+n
                if(not hasName):
                    print 'trovato['+v+']: '+self.verbs[v]

bs = BrainSentence('who are you')
bs.deduce()
bs = BrainSentence("hi i'm danger")
bs.deduce()
bs = BrainSentence("hi i am danger")
bs.deduce()
