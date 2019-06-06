from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpi.root","READ")
t = f.Get("dsprecontree")

nb = RooRealVar("nb","nb",-1,1)
gm1nb = RooRealVar("gm1nb","gm1nb",-1,1)
gm2nb = RooRealVar("gm2nb","gm2nb",-1,1)
nBins = 100
lb = nb.getMin()
rb = nb.getMax()
ub = gm1nb.getMax()
bb = gm1nb.getMin()
frame = nb.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

plot_2d(t,"nb","gm1nb","whomi==1","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/tmpigmnbplot")
