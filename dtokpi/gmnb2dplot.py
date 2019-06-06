from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpiworking.root","READ")
t = f.Get("dsprecontree")

gm1nb = RooRealVar("gm1nb","gm1nb",-1,1)
gm2nb = RooRealVar("gm2nb","gm2nb",-1,1)
nBins = 100
lb = gm1nb.getMax()
rb = gm1nb.getMin()
ub = gm2nb.getMax()
bb = gm2nb.getMin()
frame = gm1nb.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

#plot_2d(t,"gm1nb","gm2nb","whomi==1","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/gmnb2dplot")
plot_2d(t,"gm1nb","gm2nb","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/gmnb2dplot")
