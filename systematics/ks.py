from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#t = f.Get("dstree")
#t = f.Get("dsrecontree")
t = f.Get("dslrecontree")

kpP = RooRealVar("kpP","kpP",0,3.5)
nBins = 100
rb = kpP.getMax()
lb = kpP.getMin()
frame = kpP.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

# KS
#plot_variable3histos(t,"kpP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Neutral Kaon's 3-Momentum Using the 4-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{K^{0}_{S}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/kpPS_dstree_TM")

#plot_variable(t,"kpP","","Magnitude of the Neutral Kaon's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{K^{0}_{S}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/kpPS")
#plot_variable3histos(t,"kpP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Neutral Kaon's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{K^{0}_{S}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/kpPS_TM")

# KL
#plot_variable(t,"kpP","","Magnitude of the Neutral Kaon's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{K^{0}_{L}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/kpPL")
plot_variable3histos(t,"kpP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Neutral Kaon's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{K^{0}_{L}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/kpPL_TM")
