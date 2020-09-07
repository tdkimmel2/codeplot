from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t = f.Get("dsplrecontree")

dspPmagcms = RooRealVar("dspPmagcms","dspPmagcms",0,5)
nBins = 100
lb = dspPmagcms.getMin()
rb = dspPmagcms.getMax()
frame = dspPmagcms.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)
h3 = TH1F("h3","h3",nBins,lb,rb)
h4 = TH1F("h4","h4",nBins,lb,rb)
h5 = TH1F("h5","h5",nBins,lb,rb)

#plot_variable5histos(rb,lb,t,"dspPmagcms","mcflag==1","Inclusive MC","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,h5,frame,0.65,0.6,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag")

plot_variable4histos(rb,lb,t,"dspPmagcms","mcflag==2","Charm MC","mcflag==3","Mixed MC","mcflag==4","Charged MC","mcflag==5","UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,frame,0.75,0.7,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag")
#plot_variable4histos(rb,lb,t,"dspPmagcms","mcflag==2 && nb>0.832","Charm MC","mcflag==3 && nb>0.832","Mixed MC","mcflag==4 && nb>0.832","Charged MC","mcflag==5 && nb>0.832","UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,frame,0.75,0.7,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag_nb832")
#plot_variable4histos(rb,lb,t,"dspPmagcms","mcflag==2 && abs(kpdiff)<0.1","Charm MC","mcflag==3 && abs(kpdiff)<0.1","Mixed MC","mcflag==4 && abs(kpdiff)<0.1","Charged MC","mcflag==5 && abs(kpdiff)<0.1","UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,h3,h4,frame,0.75,0.7,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag_kpdiff1_4histos")

#plot_variable2histos(t,"dspPmagcms","mcflag==2 && nb>0.832","Charm MC","mcflag!=2 && nb>0.832","B or UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,0.65,0.65,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag_2Histos_nb832")
#plot_variable2histos(t,"dspPmagcms","mcflag==2 && abs(kpdiff)<0.1","Charm MC","mcflag!=2 && abs(kpdiff)<0.1","B or UDS MC","Reconstructed D^{*+} 3-Momentum Magnitude in CoM Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From All MC","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,0.65,0.65,"/home/tkimmel/Research/plots/alldtokpi/alldsplPmag_2Histos_kpdiff1")
