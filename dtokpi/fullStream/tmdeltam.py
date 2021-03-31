from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/fullStream.root","READ")
#t = f.Get("dslrecontree")
t = f.Get("dsrecontree")

deltam = RooRealVar("deltam","deltam",0.139,0.153)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)

#plot_variable3histos(rb,lb,t,"deltam","","Total","abs(dsflag)==1","Signal","abs(dsflag)!=1","Background","#DeltaM_{D*D^{0}}  D* -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi: From Full Stream of MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.17,0.7,"/home/tkimmel/Research/plots/fullStream/tmkl")
plot_variable3histos(rb,lb,t,"deltam","","Total","abs(dsflag)==1","Signal","abs(dsflag)!=1","Background","#DeltaM_{D*D^{0}}  D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From Full Stream of MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,h3,frame,0.17,0.7,"/home/tkimmel/Research/plots/fullStream/tmks")
