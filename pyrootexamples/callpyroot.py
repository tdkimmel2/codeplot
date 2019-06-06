from ROOT import *
from pyrootfunctions import *

f = TFile("/home/taylor/Research/root/dsprecon.root","READ")
t = f.Get("dspkstree")

dspmass = RooRealVar("dspmass","dspmass",1.81,2.21)
nBins = 100
lb = dspmass.getMin()
rb = dspmass.getMax()
frame = dspmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

#plot_particlemass(t,"dspmass","From MC: D^{*+} Mass","M_{D^{*+}} (GeV/c^{2})",h1,frame,"masstest")
#plot_trueparticlemass(t,"dspmass","whoru","From MC: True D^{*+} Mass","M_{D^{*+}} (GeV/c^{2})",h1,frame,"truetest")
plot_trueparticlemasswithbackground(t,"dspmass","whoru","From MC: True D^{*+} Mass","M_{D^{*+}} (GeV/c^{2})",h1,h2,h3,frame,0.75,"truetestwithbackground")
