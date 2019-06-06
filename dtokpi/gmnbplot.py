from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsprecontree")

gm1nb = RooRealVar("gm1nb","gm1nb",-1,1)
gm2nb = RooRealVar("gm2nb","gm2nb",-1,1)
nBins = 100
lb = gm1nb.getMin()
rb = gm1nb.getMax()
#lb = gm2nb.getMin()
#rb = gm2nb.getMax()
frame = gm1nb.frame()
#frame = gm2nb.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

plot_variable(t,"gm1nb","whomi==1","From MC: #gamma_{1} NeuroBayes Output","#gamma_{1} NB",h1,frame,0.2,"/home/taylor/Research/plots/dtokpi/tmgm1nbplot")
#plot_variable(t,"gm2nb","whomi==1","From MC: #gamma_{2} NeuroBayes Output","#gamma_{2} NB",h1,frame,0.2,"/home/taylor/Research/plots/dtokpi/tmgm2nbplot")
