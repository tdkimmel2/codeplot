from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#t = f.Get("dsrecontree")
t = f.Get("dslrecontree")

pip = RooRealVar("pip","pip",0,1)
nBins = 100
rb = pip.getMax()
lb = pip.getMin()
frame = pip.frame()

"""
kspipP = RooRealVar("kspipP","kspipP",0,2)
kspipm = RooRealVar("kspipm","kspipm",0,2)
nBins = 100
rb = kspipP.getMax()
lb = kspipP.getMin()
frame = kspipP.frame()
"""

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

# KS
#plot_variable(t,"pip","","Magnitude of the Slow Charged Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/pipS")
#plot_variable3histos(t,"pip","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Slow Charged Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/pipS_TM")

#plot_variable(t,"kspipP","","Magnitude of the Positive Pion's 3-Momentum K_{S}^{0} -> #pi^{+} + #pi^{-}: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/kspipP")
#plot_variable3histos(t,"kspipP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Positive Pion's 3-Momentum K_{S}^{0} -> #pi^{+} + #pi^{-}: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/kspipPS_TM")
#plot_variable(t,"kspimP","","Magnitude of the Negative Pion's 3-Momentum K_{S}^{0} -> #pi^{+} + #pi^{-}: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/kspimP")
#plot_variable3histos(t,"kspimP","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Negative Pion's 3-Momentum K_{S}^{0} -> #pi^{+} + #pi^{-}: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/kspimPS_TM")

# KL
plot_variable(t,"pip","","Magnitude of the Slow Charged Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,frame,0.6,0.6,"/home/tkimmel/Research/plots/systematics/pipL")
#plot_variable3histos(t,"pip","","All","abs(dsflag)==1","Truth Matched D*","abs(dsflag)!=1","Background","Magnitude of the Slow Charged Pion's 3-Momentum D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","|#vec{p}_{#pi^{#pm}}|",h1,h2,h3,frame,0.55,0.6,"/home/tkimmel/Research/plots/systematics/pipL_TM")
