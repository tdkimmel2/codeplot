from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")

t = f.Get("dsrecontree")
t2 = f.Get("dstree")

deltam = RooRealVar("deltam","deltam",0.138,0.155)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

# K0L Signal MC
#plot_variable2trees(t,t2,"deltam","","Modified Reconstruction: ","","Standard Reconstruction: ","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.20,"/home/tkimmel/Research/plots/klSignalMC/compareRecon_pionDup")

# K0S Signal MC
#plot_variable2trees(t,t2,"deltam","","Modified Reconstruction: ","","Standard Reconstruction: ","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.49,0.6,"/home/tkimmel/Research/plots/ksSignalMC/compareRecon_ksSignal")
plot_variable2trees(t2,t2,"deltam","abs(dsflag)==1","Modified Truth Matching: ","whomi==1","Standard Truth Matching: ","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.49,0.55,"/home/tkimmel/Research/plots/ksSignalMC/directTMCompare_ksSignal")
#plot_variable2trees(t,t2,"deltam","abs(dsflag)==1","Modified Reconstruction and TM: ","whomi==1","Standard Reconstruction and TM: ","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.46,0.6,"/home/tkimmel/Research/plots/ksSignalMC/compareReconTM_pionDup")

# All Generic MC
#plot_variable2trees(t2,t2,"deltam","abs(dsflag)==1","Modified Truth Matching: ","whomi==1","Standard Truth Matching: ","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.49,0.55,"/home/tkimmel/Research/plots/alldtokpi/directTMCompare_allGeneric")
