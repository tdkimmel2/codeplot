from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

filename = ["dspx","dspy","dspz","dspPmag"]
geninfo = "deltamwindow"
#geninfo = "mtr413deltamwindow"
#geninfo = "pizmtr421deltamwindow"
#geninfo = "pizmtrN421deltamwindow"

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/charmmfrecon.root","READ")
t = f.Get("dsplrecontree")

dspx = RooRealVar("dspx","dspx",-5,5)
dspy = RooRealVar("dspy","dspy",-5,5)
dspz = RooRealVar("dspz","dspz",-5,5)
dspPmag = RooRealVar("dspPmag","dspPmag",0,5)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = dspx.getMin()
rb = dspx.getMax()
frame = dspx.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

######################No Geninfo######################
plot_variable(t,"dspx","deltam>0.145 && deltam<0.146","D^{*+} p_{x} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
plot_variable(t,"dspy","deltam>0.145 && deltam<0.146","D^{*+} p_{y} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
plot_variable(t,"dspz","deltam>0.145 && deltam<0.146","D^{*+} p_{z} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
plot_variable(t,"dspPmag","deltam>0.145 && deltam<0.146","D^{*+} |p| D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)


######################Mother of pi+ is a D*+######################
#plot_variable(t,"dspx","mtrID==413 && deltam>0.145 && deltam<0.146","D^{*+} p_{x} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dspy","mtrID==413 && deltam>0.145 && deltam<0.146","D^{*+} p_{y} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dspz","mtrID==413 && deltam>0.145 && deltam<0.146","D^{*+} p_{z} Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dspPmag","mtrID==413 && deltam>0.145 && deltam<0.146","D^{*+} |p| Mother of #pi^{+} is a D^{*+} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is a D0######################
#plot_variable(t,"dspx","pizmtrID==421 && deltam>0.145 && deltam<0.146","D^{*+} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dspy","pizmtrID==421 && deltam>0.145 && deltam<0.146","D^{*+} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dspz","pizmtrID==421 && deltam>0.145 && deltam<0.146","D^{*+} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dspPmag","pizmtrID==421 && deltam>0.145 && deltam<0.146","D^{*+} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)

######################Mother of pi0 is not a D0######################
#plot_variable(t,"dspx","pizmtrID!=421 && deltam>0.145 && deltam<0.146","D^{*+} p_{x} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{x} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[0]+geninfo)
#plot_variable(t,"dspy","pizmtrID!=421 && deltam>0.145 && deltam<0.146","D^{*+} p_{y} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{y} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[1]+geninfo)
#plot_variable(t,"dspz","pizmtrID!=421 && deltam>0.145 && deltam<0.146","D^{*+} p_{z} Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} p_{z} (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[2]+geninfo)
#plot_variable(t,"dspPmag","pizmtrID!=421 && deltam>0.145 && deltam<0.146","D^{*+} |p| Mother of #pi^{0} is a D^{0} - D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","D^{*+} |p| (GeV/c^{2})",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/k0signalMC/"+filename[3]+geninfo)
