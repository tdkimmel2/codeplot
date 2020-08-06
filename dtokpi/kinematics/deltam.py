from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/klsignalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/kssignalmfrecon.root","READ")
t = f.Get("dsplrecontree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#plot_variable(t,"deltam","kpdiff>-0.2 && kpdiff<0.2","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/deltamsinsdkpdiff")
#plot_variable(t,"deltam","kpdiff<-0.2 || kpdiff>0.2","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From K_{S}^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/deltamsoutsdkpdiff")

#KLong
#plot_variable(t,"deltam","kpdiff>-0.2 && kpdiff<0.2","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.35,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/deltamsinsdkpdiffL")
plot_variable(t,"deltam","kpdiff<-0.2 || kpdiff>0.2","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/deltamsoutsdkpdiffL")
