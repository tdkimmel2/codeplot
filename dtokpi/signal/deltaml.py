from ROOT import *
import sys
#sys.path.append('/home/tkimmel/Research/codeplot/functions/')
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
f = TFile("/home/taylor/Research/root/signalmfrecon.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

#plot_variable(t,"deltam","mcflag==-1","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0}_{L} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/signal/signaldeltamlklsignal")
#plot_variable(t,"deltam","mcflag==-2","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0}_{S} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/taylor/Research/plots/signal/signaldeltamlkssignal")
plot_variable(t,"deltam","mcflag==-3","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/taylor/Research/plots/signal/signaldeltamlk0signal")
#plot_variable3histos(rb,lb,t,"deltam","mcflag==-1","K^{0}_{L} Signal MC","mcflag==-2","K^{0}_{S}","mcflag==-3","K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.65,0.65,"/home/taylor/Research/plots/signal/signaldeltaml")
#plot_variable3histos(rb,lb,t,"deltam","mcflag==-1 && nb>0.54 && dnb>0.68","K^{0}_{L} Signal MC","mcflag==-2 && nb>0.54 && dnb>0.68","K^{0}_{S}","mcflag==-3 && nb>0.54 && dnb>0.68","K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.65,0.65,"/home/taylor/Research/plots/signal/signaldeltaml5468nbcuts")
