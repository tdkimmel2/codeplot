from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/allmfdtokpi.root","READ")
t = f.Get("dsprecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)
h5 = TH1F("h5","h5",nBins,lb,rb)

plot_variable5histos(rb,lb,t,"deltam","mcflag==1 && whomi > 3","Inclusive MC","mcflag==2 && whomi > 3","Charm MC","mcflag==3 && whomi > 3","Mixed MC","mcflag==4 && whomi > 3","Charged MC","mcflag==5 && whomi > 3","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.65,0.6,"/home/tkimmel/Research/plots/alldtokpi/alltmdeltams")
#plot_variable5histos(rb,lb,t,"deltam","mcflag==1 && whomi > 3","Inclusive MC","mcflag==2 && whomi > 3","Charm MC","mcflag==3 && whomi > 3","Mixed MC","mcflag==4 && whomi > 3","Charged MC","mcflag==5 && whomi > 3","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,h5,frame,0.65,0.6,"/home/taylor/Research/plots/alldtokpi/alltmdeltams")
