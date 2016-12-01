class BrainSentence:

    names = ['danger','giulia','elena','elf','momo','diana','claudia']
    verbs = {
                "i'm":"saluta",
                'am':'saluta',
                'is':'saluta',
                'who are you':'intoduci'
            }
    action = {
        0:[0,1,3,10],
        1:[0,3],
        2:[0,3],
        3:[0,1,2,3],
        10:[0,11],
        11:[12,13],
        12:[10],
        13:[14],
        14:[15],
        15:[12,13]
    }
    eventNode = [1,2]

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
