from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/partialMC.root","READ")
t = f.Get("dsrecontree")
#t = f.Get("dslrecontree")

kpP = RooRealVar("kpP","kpP",0,4)
nBins = 75
lb = kpP.getMin()
rb = kpP.getMax()
frame = kpP.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

plot_variable2histos(t,"kpP","abs(dsflag)==1","Truth Matched","","Total","|#vec{p}_{K_{S}^{0}}| D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{K_{S}^{0}}| (GeV/c)",h1,h2,frame,0.55,0.65,"/home/tkimmel/Research/plots/alldtokpi/kpPS")
#plot_variable2histos(t,"kpP","abs(dsflag)==1","Truth Matched","","Total","|#vec{p}_{K_{L}^{0}}| D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{K_{L}^{0}}| (GeV/c)",h1,h2,frame,0.55,0.65,"/home/tkimmel/Research/plots/alldtokpi/kpPL")
