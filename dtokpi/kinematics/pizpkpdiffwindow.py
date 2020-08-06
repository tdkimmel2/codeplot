from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

filename = ["pizxcm","pizycm","pizzcm","pizpcm"]
#geninfo = "kpdiffwindow"
#geninfo = "mtr413kpdiffwindow"
#geninfo = "pizmtr421kpdiffwindow"
geninfo = "pizmtrN421kpdiffwindow"

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/charmmfrecon.root","READ")
t = f.Get("dsplrecontree")

#pizxcm = RooRealVar("pizxcm","pizxcm",-1,1)
#pizycm = RooRealVar("pizycm","pizycm",-1,1)
#pizzcm = RooRealVar("pizzcm","pizzcm",-1,1)
pizxcm = RooRealVar("pizxcm","pizxcm",-3,3)
pizycm = RooRealVar("pizycm","pizycm",-3,3)
pizzcm = RooRealVar("pizzcm","pizzcm",-3,3)
pip = RooRealVar("pip","pip",0,1)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = pizxcm.getMin()
rb = pizxcm.getMax()
frame = pizxcm.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

######################No Geninfo######################
#plot_variable(t,"pizxcm","kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{x} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pizycm","kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{y} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pizzcm","kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{z} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pi0p3cms","kpdiff>-0.1 && kpdiff<0.1","p^{0} |p| D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)


######################Mother of pi+ is a D*+######################
#plot_variable(t,"pizxcm","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{x} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pizycm","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{y} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pizzcm","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{z} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pi0p3cms","mtrID==413 && kpdiff>-0.1 && kpdiff<0.1","p^{0} |p| Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#pi^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is a D0######################
#plot_variable(t,"pizxcm","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pizycm","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pizzcm","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pi0p3cms","pizmtrID==421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is not a D0######################
plot_variable(t,"pizxcm","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
plot_variable(t,"pizycm","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
plot_variable(t,"pizzcm","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
plot_variable(t,"pi0p3cms","pizmtrID!=421 && kpdiff>-0.1 && kpdiff<0.1","p^{0} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{0} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)
