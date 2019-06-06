from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/taylor/Research/root/mfdtokpiworking.root","READ")
t = f.Get("dsprecontree")

coskpiz = RooRealVar("coskpiz","coskpiz",-1,1)
cosdpipcm = RooRealVar("cosdpipcm","cosdpipcm",-1,1)
nBins = 100
lb = coskpiz.getMin()
rb = coskpiz.getMax()
ub = cosdpipcm.getMax()
bb = cosdpipcm.getMin()
frame = coskpiz.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

#plot_2d(t,"coskpiz","cosdpipcm","whomi>3","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/tmksbothanglesplot")
plot_2d(t,"coskpiz","cosdpipcm","","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/tmksbothanglesplot")
