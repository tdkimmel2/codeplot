from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/dspsmallset.root","READ")
t = f.Get("pi0tree")

gamma1wid = RooRealVar("gamma1wid","gamma1wid",0,6)
nBins = 100
lb = gamma1wid.getMin()
rb = gamma1wid.getMax()
frame = gamma1wid.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

plot_variable2histos(t,"gamma1wid","whoru==1","Truth Matched","","Total","From MC: Width of #gamma_{1} Shower","Width (cm)",h1,h2,frame,0.2,"/home/taylor/Research/plots/pi0tree/tmgamma1wid")
