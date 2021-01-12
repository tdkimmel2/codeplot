from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/genericmfdtokpi.root","READ")

#t = f.Get("dsrecontree")
t = f.Get("dstree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
#deltam = RooRealVar("deltam","deltam",0.143653,0.147379) #Three sigma window for Ks
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#plot_variable2histos(t,"deltam","whomi==1","Truth Matched Candidates","","All Candidates","Truth Matched #DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi+: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.4,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ks_ds_tm2histos")
#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched Candidates","","All Candidates","Truth Matched #DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi+: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.4,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_ds_tm2histos")

###########################Generic MC#########################
plot_variable2histos(t,"deltam","bcsflag==1","Best #pi^{0} Candidate Selection","","All Candidates","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi+: From All Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.4,0.45,"/home/tkimmel/Research/plots/alldtokpi/ks_ds_bcs2histos")
