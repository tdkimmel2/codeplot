from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/bmcdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

#plot_variable3histos(rb,lb,t,"deltam","whomi>3","Tight TM","whomi>0","Loose TM","","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.3,"/home/taylor/Research/plots/dtokpi/tmks")
plot_variable3histos(rb,lb,t,"deltam","whomi>3","Tight TM","whomi>0","Loose TM","","Total","Truth Matched #DeltaM_{D^{*+}D^{0}}  D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From Mixed MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.7,0.5,"/home/taylor/Research/plots/dtokpibmc/tmks")
