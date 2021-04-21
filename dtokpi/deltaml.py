from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
#f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
t = f.Get("dslrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.155)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.65,0.65,"/home/tkimmel/Research/plots/alldtokpi/klRecon_TM")

# Full Stream
#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From All Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.65,0.65,"/home/tkimmel/Research/plots/fullStream/klRecon_TM")
plot_variable3histos(t,"deltam","","Total","abs(dsflag)==1","Signal","abs(dsflag)!=1","Background","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Full Stream of Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.55,0.45,"/home/tkimmel/Research/plots/fullStream/klRecon_TM")
#plot_variable(t,"deltam","abs(dsflag)==1","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K^{0}_{L} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/klSignalMC/klRecon_TM")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From K^{0}_{S} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/ksSignalMC/klRecon")
