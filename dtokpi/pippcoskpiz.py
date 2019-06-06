from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpiworking.root","READ")
t = f.Get("dsprecontree")

pipp = RooRealVar("pipp","pipp",0,1)
coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
nBins = 100
rb = pipp.getMax()
lb = pipp.getMin()
ub = coskpiz.getMax()
bb = coskpiz.getMin()
frame = pipp.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

plot_2d(t,"pipp","coskpiz","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/pippcoskpiz")
