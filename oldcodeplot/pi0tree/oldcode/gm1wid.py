from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dspsmallset.root","READ")
t = f.Get("pi0tree")

gamma1wid = RooRealVar("gamma1wid","gamma1wid",0,10)
nBins = 100
lb = gamma1wid.getMin()
rb = gamma1wid.getMax()
frame = gamma1wid.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gamma1wid","","From MC: Shower Width of #gamma_{1}","Shower Width (cm)",h1,frame,0.2,"/home/taylor/Research/plots/pi0tree/gm1wid")
