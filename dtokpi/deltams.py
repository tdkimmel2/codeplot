from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")

#t = f.Get("dsrecontree")
t = f.Get("dstree")

#deltam = RooRealVar("deltam","deltam",0.138,0.18)
deltam = RooRealVar("deltam","deltam",0.138,0.16)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#plot_variable(t,"deltam","chrgflag==1","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_dsp")
#plot_variable(t,"deltam","chrgflag==-1","#DeltaM_{D^{*-}D^{0}} D^{*-} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{-}: From K^{0} Signal MC","#DeltaM_{D^{*-}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_dsm")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_ds")

#plot_variable(t,"deltam","chrgflag==1","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_dsp")
#plot_variable(t,"deltam","chrgflag==-1","#DeltaM_{D^{*-}D^{0}} D^{*-} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{-}: From K^{0} Signal MC","#DeltaM_{D^{*-}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon_dsm")
#plot_variable(t,"deltam","","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K_{S}^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/ksSignalMC/ks_ds")

#plot_variable(t,"deltam","nb>0.69","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K_{L}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.70,0.70,"/home/tkimmel/Research/plots/klSignalMC/ksRecon69nbcut")



#plot_variable(t,"deltam","","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon")
#plot_variable(t,"deltam","nb>0.69","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.70,0.70,"/home/tkimmel/Research/plots/ksSignalMC/ksRecon69nbcut")

#####################Generic MC#########################3
plot_variable(t,"deltam","bcsflag==1 && nb>-0.076","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From All Generic MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,frame,0.55,0.65,"/home/tkimmel/Research/plots/alldtokpi/ks_ds_bcs_nbn0p076")
