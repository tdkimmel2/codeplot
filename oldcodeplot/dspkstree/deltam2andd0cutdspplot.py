from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dspkstree")

dspmass = RooRealVar("dspmass","dspmass",1.9,2.1)
nBins = 100
lb = dspmass.getMin()
rb = dspmass.getMax()
frame = dspmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#Plot dspmass with a 5 sigma mass cut on deltam2
plot_variablewith2cutsandtrue(t,"dspmass","whoru","deltam2>0.528 && deltam2<0.5986","d0mass<1.95365 && d0mass > 1.77065","5#sigma Cut on #DeltaM^{2} and M_{D^{0}}","From MC: D^{*+} Mass with 5#sigma #DeltaM^{2}_{D^{*+}D^{0}} and M_{D^{0}} Cuts","M_{D^{*+}} (GeV/c^{2})",h1,h2,frame,0.15,"/home/taylor/Research/plots/dspkstree/deltam2andd0cutdspmass")
