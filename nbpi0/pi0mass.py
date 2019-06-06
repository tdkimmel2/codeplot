from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/nbpi0/nnout.root","READ")
t = f.Get("pi0tree")

pi0mass = RooRealVar("pi0mass","pi0mass",0.035,0.235)
nBins = 100
lb = pi0mass.getMin()
rb = pi0mass.getMax()
frame = pi0mass.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"pi0mass","","No NB Cut","nb>0.9099988","Optimal NB Cut","From MC: #pi^{0} Mass","#pi^{0} Mass",h1,h2,frame,0.65,"/home/taylor/Research/plots/nbpi0/pi0mass")
