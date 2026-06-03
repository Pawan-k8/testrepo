#DefineString = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
#code for finding text repeatation
class textFinder:
    #constructor
    def __init__ (self,text):
        formatText = text.replace(',','').replace('.','').replace('!','').replace('?','')
        self.fmtText = formatText.lower()
    #method 1
    def overallFreq(self): #defining method 
        wordlist = self.fmtText.split(' ') #spliting the string into wordlist
        freqMp={} #creation of empty dict
        for word in wordlist: #search for all words inside wordlist
            freqMp[word] = wordlist.count(word) #count of all words inside wordlist
        return freqMp #storing the updated wordlist into dictionary

    #method 2
    def particularFreq(self,word):
        particularFreq = self.overallFreq()
        if word in particularFreq:
            return (particularFreq[word])
        else:
            return 0


#########################
#calling function
#initial call
calling = textFinder(DefineString)
#first call (overall word count)
calling.overallFreq()
#2nd call (particular word count)
word = "et"
calling.particularFreq(word)
