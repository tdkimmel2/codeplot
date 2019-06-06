from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfrecon.root","READ")
t = f.Get("kltree")

kly = RooRealVar("kly","kly",-1,1)
klx = RooRealVar("klx","klx",-1,1)
nBins = 100
lb = klx.getMin()
rb = klx.getMax()
ub = kly.getMax()
bb = kly.getMin()
frame = kly.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

plot_2d(t,"klx","kly","","BOX","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/nynxplot")
