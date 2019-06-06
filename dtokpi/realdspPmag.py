from ROOT import *
import sys
sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/taylor/Research/root/inclusivemfrecon.root","READ")
#f = TFile("/home/taylor/Research/root/genericmfrecon.root","READ")
f = TFile("/home/taylor/Research/root/mixedmfrecon.root","READ")
t = f.Get("realdsptree")

rdspPmag = RooRealVar("rdspPmag","rdspPmag",0,5)
nBins = 100
lb = rdspPmag.getMin()
rb =  rdspPmag.getMax()
frame = rdspPmag.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

#plot_variable(t,"rdspPmag","","Generated D^{*+} 3-Momentum Magnitude: From Inclusive c#bar{c} MC","|#vec{p}_{D^{*+}}| (GeV/c)",h1,frame,0.15,0.6,"/home/taylor/Research/plots/dtokpi/generatedinclusiverdspPmag")
#plot_variable(t,"rdspPmag","","Generated D^{*+} 3-Momentum Magnitude: From Inclusive c#bar{c} MC","|#vec{p}_{D^{*+}}| (GeV/c)",h1,frame,0.15,0.6,"/home/taylor/Research/plots/dtokpigeneric/genericgenerateddspPmag")
plot_variable(t,"rdspPmag","","Generated D^{*+} 3-Momentum Magnitude: From Mixed MC","|#vec{p}_{D^{*+}}| (GeV/c)",h1,frame,0.6,0.6,"/home/taylor/Research/plots/dtokpimixed/mixedgenerateddspPmag")
