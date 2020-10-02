from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon_reducedpi0fittingsample.root","READ")
t = f.Get("pi0tree")

mfchi2 = RooRealVar("mfchi2","mfchi2",0,10)
gmthetacms = RooRealVar("gmthetacms","gmthetacms",0,3.14)
nBins = 100
lb = mfchi2.getMax()
rb = mfchi2.getMin()
ub = gmthetacms.getMax()
bb = gmthetacms.getMin()
frame = mfchi2.frame()

h2 = TH2F("h2","h2",nBins,lb,rb,nBins,bb,ub)

#plot_2d(t,"gm1nb","gm2nb","whomi==1","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/taylor/Research/plots/dtokpi/gmnb2dplot")
plot_2d(t,"mfchi2","gmthetacms","mfchi2<=10 && whomi==0","COLZ","From MC: Title","XTitle","YTitle",h2,frame,0.65,"/home/tkimmel/Research/plots/nbpi0/mfchigmtheta2d_bkg")
