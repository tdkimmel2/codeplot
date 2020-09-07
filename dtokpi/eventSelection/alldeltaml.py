from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 100
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)

#plot_variable4histos(rb,lb,t,"deltam","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.15,0.73,"/home/tkimmel/Research/plots/alldtokpi/alldeltaml")
#plot_variable4histos(rb,lb,t,"deltam","mcflag==2 && nb>0.832","Charm MC","mcflag==3 && nb>0.832","Mixed MC","mcflag==4 && nb>0.832","Charged MC","mcflag==5 && nb>0.832","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.15,0.73,"/home/tkimmel/Research/plots/alldtokpi/alldeltaml_nb832")
plot_variable4histos(rb,lb,t,"deltam","mcflag==2 && abs(kpdiff)<0.1","Charm MC","mcflag==3 && abs(kpdiff)<0.1","Mixed MC","mcflag==4 && abs(kpdiff)<0.1","Charged MC","mcflag==5 && abs(kpdiff)<0.1","UDS MC","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,h2,h3,h4,frame,0.15,0.73,"/home/tkimmel/Research/plots/alldtokpi/alldeltaml_kpdiff1")
