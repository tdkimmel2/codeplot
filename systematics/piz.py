from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#t = f.Get("dsrecontree")
t = f.Get("dslrecontree")

pizpP = RooRealVar("pizpP","pizpP",0,5)
nBins = 100
rb = pizpP.getMax()
lb = pizpP.getMin()
frame = pizpP.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

# KS
#plot_variable(t,"pizpP","","Magnitude of the Neutral Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{0}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/pizpPS")
#plot_variable3histos(t,"pizpP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Neutral Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{0}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/pizpPS_TM")

# KL
#plot_variable(t,"pizpP","","Magnitude of the Neutral Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{0}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/pizpPL")
plot_variable3histos(t,"pizpP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Neutral Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{0}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/pizpPL_TM")
