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

#Plot dspmass with a 5 sigma mass cut on d0mass
plot_variable(t,"dspmass","d0mass<1.95365 && d0mass > 1.77065","From MC: D^{*+} Mass with 5#sigma D^{0} Mass Cut","M_{D^{*+}} (GeV/c^{2})",h1,frame,0.25,"/home/taylor/Research/plots/dspkstree/d0cutdspmass")
