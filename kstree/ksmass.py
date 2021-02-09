from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/allmfreconKstree.root","READ")
f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")

t = f.Get("kstree")

ksmass = RooRealVar("ksmass","ksmass",0.490,0.506)
#nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = ksmass.getMin()
rb = ksmass.getMax()
frame = ksmass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#####################KSSignal MC##########################
plot_variable(t,"ksmass","","K_{S}^{0} Mass: From K_{S}^{0} Signal MC","M_{K_{S}^{0}} (GeV/c^{2})",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/kstree/ksmass_ksSig")

#####################Generic MC##########################
#plot_variable(t,"ksmass","","K_{S}^{0} Mass: From All Generic MC","M_{K_{S}^{0}} (GeV/c^{2})",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/kstree/ksmass")
