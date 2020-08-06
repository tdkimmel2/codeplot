from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

filename = ["pipx","pipy","pipz","pip"]
#geninfo = ""
#geninfo = "mtr413"
#geninfo = "mtrN413"
#geninfo = "pizmtr421"
geninfo = "pizmtrN421"

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/charmmfrecon.root","READ")
t = f.Get("dsplrecontree")

pipx = RooRealVar("pipx","pipx",-1,1)
pipy = RooRealVar("pipy","pipy",-1,1)
pipz = RooRealVar("pipz","pipz",-1,1)
pip = RooRealVar("pip","pip",0,1)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = pipx.getMin()
rb = pipx.getMax()
frame = pipx.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

######################No Geninfo######################
#plot_variable(t,"pipx","","p^{+} p_{x} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pipy","","p^{+} p_{y} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pipz","","p^{+} p_{z} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pipp","","p^{+} |p| D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)


######################Mother of pi+ is a D*+######################
#plot_variable(t,"pipx","mtrID==413","p^{+} p_{x} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pipy","mtrID==413","p^{+} p_{y} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pipz","mtrID==413","p^{+} p_{z} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pipp","mtrID==413","p^{+} |p| Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is a D0######################
#plot_variable(t,"pipx","pizmtrID==421","p^{+} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"pipy","pizmtrID==421","p^{+} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"pipz","pizmtrID==421","p^{+} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"pipp","pizmtrID==421","p^{+} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is not a D0######################
plot_variable(t,"pipx","pizmtrID!=421","p^{+} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
plot_variable(t,"pipy","pizmtrID!=421","p^{+} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
plot_variable(t,"pipz","pizmtrID!=421","p^{+} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
plot_variable(t,"pipp","pizmtrID!=421","p^{+} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","p^{+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)
