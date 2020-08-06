from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
#sys.path.append('/home/taylor/Research/codeplot/functions/')
from plottingfunctions import *

filename = ["kpdiff"]
geninfo = "L"
#geninfo = "mtr413L"
#geninfo = "pizmtr421L"
#geninfo = "pizmtrN421L"

f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
#f = TFile("/home/tkimmel/Research/root/charmmfrecon.root","READ")
t = f.Get("dsplrecontree")

kpdiff = RooRealVar("kpdiff","kpdiff",-5,5)
nb = RooRealVar("nb","nb",-1,1)
nBins = 75
lb = kpdiff.getMin()
rb = kpdiff.getMax()
frame = kpdiff.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)

######################No Geninfo######################
plot_variable(t,"kpdiff","","#Delta|p|_{K_{nisKs}K_{calc}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#Delta|p|_{K_{nisKs}K_{calc}} (GeV/c)",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/"+filename[0]+geninfo)

######################Mother of pi+ is a D*+######################
#plot_variable(t,"kpdiff","mtrID==413","#Delta|p|_{K_{nisKs}K_{calc}} Mother of #pi^{+} is a D^{0} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#Delta|p|_{K_{nisKs}K_{calc}} (GeV/c)",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/"+filename[0]+geninfo)

######################Mother of pi0 is a D0######################
#plot_variable(t,"kpdiff","pizmtrID==421","#Delta|p|_{K_{nisKs}K_{calc}} Mother of #pi^{0} is a D^{0} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#Delta|p|_{K_{nisKs}K_{calc}} (GeV/c)",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/"+filename[0]+geninfo)

######################Mother of pi0 is not a D0######################
#plot_variable(t,"kpdiff","pizmtrID!=421","#Delta|p|_{K_{nisKs}K_{calc}} Mother of #pi^{0} is not a D^{0} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC","#Delta|p|_{K_{nisKs}K_{calc}} (GeV/c)",h1,frame,0.15,0.65,"/home/tkimmel/Research/plots/MCDebugL/Kinematics/kpdiff/"+filename[0]+geninfo)
