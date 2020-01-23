from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/taylor/Research/root/signalmfrecon.root","READ")
f = TFile("/home/taylor/Research/root/tmpizk0signalmfrecon.root","READ")
t = f.Get("dsprecontree")

pi0p3 = RooRealVar("pi0p3", "pi0p3",0,3)
pi0p3cms = RooRealVar("pi0p3cms", "pi0p3cms",0,4)
gm1e = RooRealVar("gm1e", "gm1e",0,2)
gm2e = RooRealVar("gm2e", "gm2e",0,2)
gm1e925 = RooRealVar("gm1e925", "gm1e925",0,1)
gm2e925 = RooRealVar("gm2e925", "gm2e925",0,1)
ediff = RooRealVar("ediff", "ediff",0,1.5)
gm1eerror = RooRealVar("gm1eerror", "gm1eerror",0,0.002)
gm2eerror = RooRealVar("gm2eerror", "gm2eerror",0,0.002)
gm1p3 = RooRealVar("gm1p3", "gm1p3",0,2)
gm2p3 = RooRealVar("gm2p3", "gm2p3",0,2)
gm1p3cms = RooRealVar("gm1p3cms", "gm1p3cms",0,2.5)
gm2p3cms = RooRealVar("gm2p3cms", "gm2p3cms",0,2.5)
gmthetacms = RooRealVar("gmthetacms", "gmthetacms",0,3.14)
mfchi2 = RooRealVar("mfchi2", "mfchi2",0,50)
nBins = 100

variables =[pi0p3,pi0p3cms,gm1e,gm2e,gm1e925,gm2e925,ediff,gm1eerror,gm2eerror,gm1p3,gm2p3,gm1p3cms,gm2p3cms,gmthetacms,mfchi2]
variablesstr =['pi0p3','pi0p3cms','gm1e','gm2e','gm1e925','gm2e925','ediff','gm1eerror','gm2eerror','gm1p3','gm2p3','gm1p3cms','gm2p3cms','gmthetacms','mfchi2']
#print(len(variables))
i = 0
for x in range(len(variables)-1):
    #print variables[x]
    for y in range(x+1,len(variables)-1):
        i = 1
        #print(cor)
        if i%2==0:
            graph = TH2F("h2","h2",nBins,variables[x].getMin(),variables[x].getMax(),nBins,variables[y].getMin(),variables[y].getMax())
        else:
            graph2 = TH2F("h2","h2",nBins,variables[x].getMin(),variables[x].getMax(),nBins,variables[y].getMin(),variables[y].getMax())
        #print(str(variables[x]))
        t.Draw("%s:%s>>graph"%(variablesstr[x],variablesstr[y]))
        cor = graph.GetCorrelationFactor()
        #print(variablesstr[x]+" "+variablesstr[y])
        #print(cor)
        if cor>0.9:
            print(variablesstr[x]+" "+variablesstr[y])
            print(cor)
        if i%2==0:
            del graph
        else:
            del graph2
        i += 1


#plot_2d(t,"coskpiz","cosdpipcm","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/tmklbothanglesplottest")
