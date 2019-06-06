from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

f = TFile("/home/tkimmel/Research/root/allmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/genericmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/mixedmfdtokpi.root","READ")
#f = TFile("/home/taylor/Research/root/inclusivemfdtokpi.root","READ")
t = f.Get("dsprecontree")

dspPmag = RooRealVar("dspPmag","dspPmag",0,5)
dspPmagCM = RooRealVar("dspPmagCM","dspPmagCM",0,5)
nBins = 100
lb = dspPmag.getMin()
rb =  dspPmag.getMax()
#lb = dspPmagCM.getMin()
#rb = dspPmagCM.getMax()
frame = dspPmag.frame()
#frame = dspPmagCM.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#plot_variable2histos(t,"dspPmag","whomi>3","Truth Matched","","Total","Truth Matched D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Generic MC","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,0.15,0.6,"/home/taylor/Research/plots/dtokpigeneric/genericdsplPmag")
#plot_variable2histos(t,"dspPmag","whomi>3","Truth Matched","","Total","Truth Matched D^{*+} 3-Momentum Magnitude D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Mixed MC","|p_{D^{*+}}| (GeV/c)",h1,h2,frame,0.65,0.6,"/home/tkimmel/Research/plots/alldtokpi/mixeddsplPmag")
#plot_variable2histos(t,"dspPmagCM","whomi>3","Truth Matched","","Total","Truth Matched D^{*+} 3-Momentum Magnitude in Center-of-Mass Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From Inclusive MC","|p_{D^{*+}}|_{CM} (GeV/c)",h1,h2,frame,0.15,0.6,"/home/taylor/Research/plots/dtokpiinclusive/dsplPmag")
plot_variable2histos(t,"dspPmagCM","whomi>3 && mcflag==5","Truth Matched","","Total","Truth Matched D^{*+} 3-Momentum Magnitude in Center-of-Mass Frame D^{*+} -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi^{+}: From UDS MC","|p_{D^{*+}}|_{CM} (GeV/c)",h1,h2,frame,0.15,0.6,"/home/tkimmel/Research/plots/dtokpiuds/tmdspsPmag")
