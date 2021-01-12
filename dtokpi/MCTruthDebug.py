from ROOT import *
import sys
sys.path.append('/home/tkimmel/Research/codeplot/functions/')
from plottingfunctions import *

#f = TFile("/home/tkimmel/Research/root/k0signalmfrecon.root","READ")
f = TFile("/home/tkimmel/Research/root/k0signalrecon.root","READ")
t = f.Get("dsrecontree")
t2 = f.Get("dstree")

deltam = RooRealVar("deltam","deltam",0.138,0.18)
nBins = 75
lb = deltam.getMin()
rb = deltam.getMax()
frame = deltam.frame()

h1 = TH1F("h1","h1",nBins,lb,rb)
h2 = TH1F("h2","h2",nBins,lb,rb)

#D*+: 413
#D0: 421
#nb: 0.854

#plot_variable(t,"deltam","pizmtrID!=421 && pizgmaID!=413","#DeltaM_{D^{*+}D^{0}} D^{*+} -> D^{0}(-> #pi^{0} + K_{L}^{0}) + #pi^{+}: From K^{0} Signal MC Grandmother of #pi^{0} is Not a D^{*+} and Mother of #pi^{0} is Not a D^{0}","#DeltaM_{D^{*+}D^{0}} (GeV/c^{2})",h1,frame,0.65,0.65,"/home/tkimmel/Research/plots/MCDebug/piznotfromd0ordsp")

#plot_variable2trees(t2,t,"deltam","","Normal Reconstruction","","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/deltamCompare")

#plot_variable2trees(t2,t,"deltam","abs(dsflag)==10","Normal Reconstruction","abs(dsflag)==10","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsflag10Compare")
#plot_variable2trees(t2,t,"deltam","abs(dsflag)==20","Normal Reconstruction","abs(dsflag)==20","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsflag20Compare")

#plot_variable2trees(t2,t,"deltam","whoru==0","Normal Reconstruction","whoru==0","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/whoru0Compare")

#plot_variable2trees(t2,t,"deltam","abs(dsIDpi)==413","Normal Reconstruction","abs(dsIDpi)==413","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsIDpi413Compare")
#plot_variable2trees(t2,t,"deltam","abs(dsIDpi)!=413","Normal Reconstruction","abs(dsIDpi)!=413","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.15,0.7,"/home/tkimmel/Research/plots/MCDebugS/dsIDpiN413Compare")

#plot_variable2trees(t2,t,"deltam","abs(dsIDpiz)==413","Normal Reconstruction","abs(dsIDpiz)==413","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsIDpiz413Compare")
plot_variable2trees(t2,t,"deltam","abs(dsIDpiz)!=413","Normal Reconstruction","abs(dsIDpiz)!=413","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsIDpizN413Compare")

#plot_variable2trees(t2,t,"deltam","whomi==1","Normal Reconstruction","abs(dsflag)==1 || abs(dsflag)==10 || abs(dsflag)==11 || abs(dsflag)==20","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/TruthMatchCompare")
#plot_variable2trees(t2,t,"deltam","abs(dsflag)==1","Normal Reconstruction","abs(dsflag)==1","Location Reconstruction","#DeltaM_{D*D^{0}} D* -> D^{0}(-> #pi^{0} + K_{S}^{0}) + #pi: From K^{0} Signal MC","#DeltaM_{D*D^{0}} (GeV/c^{2})",h1,h2,frame,0.35,0.65,"/home/tkimmel/Research/plots/MCDebugS/dsflag1Compare")
