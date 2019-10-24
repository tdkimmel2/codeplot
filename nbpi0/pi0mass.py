from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/smallccsetasymwindow.root","READ")
t = f.Get("pi0tree")

#pi0mass = RooRealVar("pi0mass","pi0mass",0.035,0.235)
#pi0mass = RooRealVar("pi0mass","pi0mass",0.085,0.185)
pi0mass = RooRealVar("pi0mass","pi0mass",0.11989,0.14758)

nBins = 100
lb = pi0mass.getMin()
rb = pi0mass.getMax()
frame = pi0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#plot_variable(t,"pi0mass","","From Inclusive MC: #pi^{0} Mass","#pi^{0} Mass",h1,frame,0.65,0.25,"/home/taylor/Research/plots/nbpi0/pi0masssmallasymwindow")
#plot_variable(t,"pi0mass","mcflag<2","From MC: #pi^{0} Mass","#pi^{0} Mass",h1,frame,0.65,0.25,"/home/taylor/Research/plots/nbpi0/pi0massinclusive")
plot_variable2histos(t,"pi0mass","whomi==1","Truth Matched","","All","From MC: Truth Matched #pi^{0} Mass","#pi^{0} Mass",h1,h2,frame,0.15,0.65,"/home/taylor/Research/plots/nbpi0/pi0massasymwindowtm")
