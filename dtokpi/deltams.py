from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")

f = TFile("/home/tkimmel/Research/root/kssignalmfrecon_noCuts.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon_pizCuts.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")

#f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")

#t = f.Get("dsrecontree")
t = f.Get("dstree")

deltam = RooRealVar("deltam","deltam",0.138,0.154)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)


#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ks_noCuts")
plot_variable2histos(t,"deltam","whomi==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ks_noCuts_TM_ksSignal")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ks_pizCuts")
#plot_variable2histos(t,"deltam","whomi==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ks_pizCuts_TM")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ks")
#plot_variable2histos(t,"deltam","whomi==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC Using K_{S}^{0} 4-Momentum","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ks_TM")

#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_noCuts")
#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_noCuts_TM_ksSignal")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_pizCuts")
#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_pizCuts_TM")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon")
#plot_variable2histos(t,"deltam","abs(dsflag)==1","Truth Matched","","Total","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0}_{S} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.55,0.55,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_TM")
