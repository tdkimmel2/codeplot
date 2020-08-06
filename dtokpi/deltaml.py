from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
#f = TFile("/home/taylor/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/taylor/Research/root/kssignalmfrecon.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#plot_variable(t,"deltam","","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{L}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/klSignalMC/klRecon")
#plot_variable(t,"deltam","nb>0.69","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{L}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/klSignalMC/klRecon69nbcut")


#plot_variable(t,"deltam","","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/ksSignalMC/klRecon")
#plot_variable(t,"deltam","nb>0.69","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.70,"/home/tkimmel/Research/plots/ksSignalMC/klRecon69nbcut")

##################Kinematics######################
#plot_variable(t,"deltam","","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{0}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/deltam")
#plot_variable(t,"deltam","pizmtrID==421","#DeltaM_{D^{*+}D^{0}} #pi^{0} from D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{0}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/deltampiz421")
#plot_variable(t,"deltam","pizmtrID!=421","#DeltaM_{D^{*+}D^{0}} #pi^{0} not from D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{0}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/deltampizN421")
#plot_variable(t,"deltam","klp<1 && pizgmaID!=413","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{0}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/deltamklppizN413")
cuts = "klp<4 && klpz>-1 && klpz<2 && klpx>-1 && klpx<1 && klpy>-1 && klpy<1"
plot_variable(t,"deltam",cuts+" && pizgmaID==413","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K_{0}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/deltamcuts413")
