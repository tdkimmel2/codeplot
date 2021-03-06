from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_pi0nb.root","READ")
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

#plot_variable4histos(rb,lb,t,"deltam","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.2,0.7,"/home/tkimmel/Research/plots/alldtokpi/alldeltams")
#plot_variable4histos(rb,lb,t,"deltam","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.65,0.6,"/home/taylor/Research/plots/alldtokpi/alldeltams")
#plot_variable4histos(rb,lb,t,"deltam","mcflag==2 && abs(kpdiff)<0.1","Charm MC","mcflag==3 && abs(kpdiff)<0.1","Mixed MC","mcflag==4 && abs(kpdiff)<0.1","Charged MC","mcflag==5 && abs(kpdiff)<0.1","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.15,0.73,"/home/tkimmel/Research/plots/alldtokpi/alldeltams_kpdiff1")
plot_variable4histos(rb,lb,t,"deltam","mcflag==2 && whomi>0","Charm MC","mcflag==3 && whomi>0","Mixed MC","mcflag==4 && whomi>0","Charged MC","mcflag==5 && whomi>0","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.65,0.73,"/home/tkimmel/Research/plots/alldtokpi/alldeltams_whomi0")
