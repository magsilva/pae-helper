class ConjuntoInteiros:
    def __init__(self, *initlist):
        self.CIlist = []
        for element in initlist:
            if (type(element) == type(0)):
                self.add(element)
            elif (type(element.CIlist) == type([])):
                for element2 in element.CIlist:
                    self.add(element2)
 
    def add(self, newitem):
        if (type(newitem) == type(0)):
            dontadd = 0
            for element in self.CIlist:
                if (newitem == element):
                    dontadd = 1
            if (dontadd == 0):
                self.CIlist = self.CIlist + [newitem]
        else:
            print 'Erro >> Inteiro esperado'
        
    def rem(self, remitem):
        if (type(remitem) == type(0)):
            self.CIlist.remove(remitem)
 
    def __str__(self):
        return "CI=" + str(self.CIlist)
            
def CIuni(CI1, CI2):
    CIRet = ConjuntoInteiros(CI1, CI2)
    return CIRet
 
def CIsub(CI1, CI2):
    CIRet = ConjuntoInteiros(CI1)
    for element in CI1.CIlist:
        for element2 in CI2.CIlist:
            if (element == element2):
                CIRet.rem(element)
    return CIRet
 
def CIint(CI1, CI2):
    CIRet = ConjuntoInteiros()
    for element in CI1.CIlist:
        for element2 in CI2.CIlist:
            if (element == element2):
                CIRet.add(element)
    return CIRetclass Tag:
    def __init__ (self):
        self.tag = ""
        
    def settag(self, incometag):
        self.tag = incometag
 
class Palavra:
    def __init__ (self):
        self.palavra = ""
        
    def setword(self, word):
        self.palavra = word
 
class Frase:
    def __init__ (self):
        self.frase = []
        self.taglist = []
        self.wordcount = 0
        self.tagcount = 0
        self.badtagcount = 0
       
    def addword (self, word):
        self.frase.append(word)
        self.wordcount+= 1
    def addtag (self, tag):
        self.frase.append(tag)
        self.taglist.append(tag)
        self.tagcount+= 1
        self.wordcount+= 1
    def addbadtag (self, badtag):
        self.frase.append(badtag)
        self.badtagcount+= 1
        self.wordcount+= 1
 
    def getwordcount (self):
        return self.wordcount
    def gettagcount (self):
        return self.tagcount
    def getbadtagcount (self):
        return self.badtagcount
 
def readfileout(filename, outputfile):
    fp = open(filename, 'r')
    ofp = open(outputfile, 'w')
 
    linecounter = 1
    lin = fp.readline()
    while (lin != ""):            
        fr = Frase()
        worditself = Palavra()
        atag = Tag()
 
        word = ""
        wordlist = lin.split()
        wn = len(wordlist)
        wcount = wn
        while (wn):
            word = wordlist[wcount - wn]
            if (word[0] == '<') and (word[len(word)-1] == '>'):
                atag.settag(word)
                fr.addtag(word)
            elif (word[0] == '<') and (word[len(word)-1] != '>'):
                worditself.setword(word)
                fr.addbadtag(word)
            else:
                worditself.setword(word)
                fr.addword(word)
            wn -= 1
        ofp.write ("linha %d - " % linecounter)
        ofp.write (" %d palavras - " % fr.getwordcount())
        ofp.write ("%d tags (" % fr.gettagcount())
        
        n = fr.gettagcount()
        while (n):
            ofp.write ("%s" % fr.taglist[fr.gettagcount()-n])
            if (n > 1):
                ofp.write (", ")
            n-= 1
        ofp.write (") - %d tags-problema\n" % fr.getbadtagcount())
 
        linecounter = linecounter + 1
        lin = fp.readline()
 
        del fr
        del worditself
 
    fp.close()
    ofp.close()

# ERRO 2 23

