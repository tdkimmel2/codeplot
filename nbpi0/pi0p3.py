from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/systematics/pi0Systematics.root","READ")
t = f.Get("pi0tree")

#pizP = RooRealVar("pizP","pizP",0,5)
pizP = RooRealVar("pizP","pizP",3.125,5)

nBins = 100
lb = pizP.getMin()
rb = pizP.getMax()
frame = pizP.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#plot_variable(t,"pizP","","#pi^{0} 3-Momentum Magnitude: From #pi^{0} Systematics MC","|#vect{p}_{#pi^{0}}",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/nbpi0/Systematics/pizP")
#plot_variable(t,"pizP","nb>0.832 && bcsflag==1","#pi^{0} 3-Momentum Magnitude: From #pi^{0} Systematics MC","|#vect{p}_{#pi^{0}}",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/nbpi0/Systematics/pizP_withCuts")

plot_variable2histos(t,"pizP","pizP>3.125 && whomi==1","Truth Matched #pi^{0}'s","pizP>3.125","All #pi^{0}'s","#pi^{0} 3-Momentum Magnitude: From #pi^{0} Systematics MC","|#vec{p}_{#pi^{0}}|",h1,h2,frame,0.5,0.65,"/home/tkimmel/Research/plots/nbpi0/Systematics/pizPG3.125")
