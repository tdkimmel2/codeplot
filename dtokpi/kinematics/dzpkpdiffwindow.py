from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

filename = ["dzpx","dzpy","dzpz","dzpp"]
#geninfo = "kpdiffwindow"
#geninfo = "mtr413kpdiffwindow"
#geninfo = "pizmtr421kpdiffwindow"
geninfo = "pizmtrN421kpdiffwindow"

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/charmmfrecon.root","READ")
t = f.Get("dsplrecontree")

dzpx = RooRealVar("dzpx","dzpx",-5,5)
dzpy = RooRealVar("dzpy","dzpy",-5,5)
dzpz = RooRealVar("dzpz","dzpz",-5,5)
dzpp = RooRealVar("dzpp","dzpp",0,5)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = dzpx.getMin()
rb = dzpx.getMax()
frame = dzpx.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

######################No Geninfo######################
#plot_variable(t,"dzpx","kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{x} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dzpy","kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{y} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dzpz","kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{z} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dzpp","kpdiff>-0.1 && kpdiff<0.1","D^{0} |p| D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)


######################Mother of pi+ is a D*+######################
#plot_variable(t,"dzpx","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{x} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dzpy","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{y} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dzpz","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{z} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dzpp","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","D^{0} |p| Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is a D0######################
#plot_variable(t,"dzpx","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dzpy","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dzpz","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dzpp","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is not a D0######################
plot_variable(t,"dzpx","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
plot_variable(t,"dzpy","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
plot_variable(t,"dzpz","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
plot_variable(t,"dzpp","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","D^{0} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)
