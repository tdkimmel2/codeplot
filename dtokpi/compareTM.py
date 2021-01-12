from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")

t = f.Get("dsrecontree")
t2 = f.Get("dstree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

# K0S Signal MC
#plot_variable2trees(t2,t2,"deltam","abs(dsflag)==1","Modified Truth Matching","whomi==1","Standard Truth Matching","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/ksSignalMC/directTMCompareKSSig")
# All Generic MC
plot_variable2trees(t2,t2,"deltam","abs(dsflag)==1","Modified Truth Matching","whomi==1","Standard Truth Matching","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/alldtokpi/directTMCompareAllMC")

#plot_variable2trees(t,t2,"deltam","abs(dsflag)==1","Modified Truth Matching","whomi==1","Standard Truth Matching","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.55,"/home/tkimmel/Research/plots/ksSignalMC/compareTM")
