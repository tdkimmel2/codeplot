from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
t = f.Get("dsrecontree")
#t = f.Get("dslrecontree")

exp = RooRealVar("exp","exp",7,73)
nBins = 75
lb = exp.getMin()
rb = exp.getMax()
frame = exp.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#plot_variable(t,"exp","","Reconstructed D*'s by Experiment D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Full Stream MC","Experiment Number",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/fullStream/experimentS")
plot_variable(t,"exp","abs(dsflag)==1","Reconstructed D*'s by Experiment D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Full Stream MC","Experiment Number",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/fullStream/experimentS_TM")

#plot_variable(t,"exp","","Reconstructed D*'s by Experiment D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Full Stream MC","Experiment Number",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/fullStream/experimentL")
#plot_variable(t,"exp","abs(dsflag)==1","Reconstructed D*'s by Experiment D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Full Stream MC","Experiment Number",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/fullStream/experimentL_TM")
