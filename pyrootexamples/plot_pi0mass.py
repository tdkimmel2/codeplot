#from ROOT import TFile, TCanvas, TTree
from ROOT import *

#gSystem.Load("libCintex.so")
#Cintex.Enable()
#gSystem.Load("$SRT_PUBLIC_CONTEXT/lib/Linux2.6-GCC-debug/libStandardRecord_dict.so")
#gInterpreter.AddIncludePath("$SRT_PUBLIC_CONTEXT")

def plot_pi0mass(CUT1, HEADING1, CUT2, HEADING2, TITLE, PDFNAME, legLB):
	h1 = TH1F("h1","h1",nBins,lb,rb)
	h2 = TH1F("h2","h2",nBins,lb,rb)
	h1.SetLineColor(kBlue)
	h2.SetLineColor(kRed)
	h2.SetLineStyle(7)
	h1.SetLineWidth(2)
	h2.SetLineWidth(2)
	h1.SetMinimum(1)
	h2.SetMinimum(1)

	frame1 = pizmass.frame();
	frame1.SetTitle("From enriched #chi_{b1}(2P) #rightarrow #omega #varUpsilon(1S) MC"+TITLE);
	#frame1.SetTitleSize("0.02")
	frame1.GetXaxis().CenterTitle(True);
	frame1.GetXaxis().SetLabelOffset(0.01);
	frame1.GetXaxis().SetLabelSize(0.05);
	frame1.GetXaxis().SetTitle("M_{#pi^{0}} (GeV/c^{2})");
	frame1.GetXaxis().SetTitleSize(0.05);
	frame1.GetXaxis().SetTitleOffset(1.5);
	frame1.GetYaxis().CenterTitle(True);
	frame1.GetYaxis().SetTitleOffset(1.4);
	frame1.GetYaxis().SetLabelSize(0.05);
	frame1.GetYaxis().SetTitleSize(0.05);
	frame1.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins);
	#frame1.SetMinimum(1)
	#frame1.SetMaximum(120000)

	t.Draw("pizmass>>h1",CUT1)
	t.Draw("pizmass>>h2",CUT2)
	nBkg = t.Draw("pizmass>>h2",CUT2)
	tex1 = TLatex(0.7,0.06,"N_{BKG} = %d"%nBkg)
	tex1.SetNDC()

	frame1.addTH1(h1)
	frame1.addTH1(h2)
	frame1.addObject(tex1)
	legWidth=0.24
	leg = TLegend(legLB,0.74,legLB+legWidth,0.89)
	leg.SetFillColor(kWhite)
	leg.SetLineColor(kWhite)
	leg.SetTextSize(0.04)
	leg.AddEntry(frame1.findObject('h1'),HEADING1,"l")
	leg.AddEntry(frame1.findObject('h2'),HEADING2,"l")

	frame1.addObject(leg)


	frame1.Draw()
	c1.Update()

	c1.Print(outfileFormat+"_pi0mass_"+PDFNAME+"_noLog.pdf")

def plot_pi0mass_true():
	#c1.SetLogy(0)
	nBins=100
	h1 = TH1F("h1","h1",nBins,lb,rb)
	h1.SetLineColor(kBlue)
	h1.SetLineWidth(2)
	h1.SetMinimum(1)
	TITLE="True #pi^{0} Candidates"
	frame1 = pizmass.frame();
	frame1.SetTitle("From enriched #chi_{b1}(2P) #rightarrow #omega #varUpsilon(1S) MC: "+TITLE);
	frame1.GetXaxis().CenterTitle(True);
	frame1.GetXaxis().SetLabelOffset(0.01);
	frame1.GetXaxis().SetLabelSize(0.05);
	frame1.GetXaxis().SetTitle("M_{#pi^{0}} (GeV/c^{2})");
	frame1.GetXaxis().SetTitleSize(0.05);
	frame1.GetXaxis().SetTitleOffset(1.5);
	frame1.GetYaxis().CenterTitle(True);
	frame1.GetYaxis().SetTitleOffset(1.4);
	frame1.GetYaxis().SetLabelSize(0.05);
	frame1.GetYaxis().SetTitleSize(0.05);
	frame1.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins);
	#frame1.SetMinimum(1)
	t.Draw("pizmass>>h1","whoru==2")
	frame1.addTH1(h1)
	frame1.Draw()
	c1.Update()
	PDFNAME="truePi0s"
	c1.Print(outfileFormat+"_pi0mass_"+PDFNAME+"_noLog.pdf")



c1 = TCanvas("c1","",800,550)
gPad.SetRightMargin(0.2)
gPad.SetLeftMargin(0.15)
gPad.SetRightMargin(0.05)
gPad.SetBottomMargin(0.2)
gStyle.SetTitleW(0.99)
#c1.SetLogy(1)

filename = "/home/taylor/Research/root/dsprecon.root"
tree = "dspkstree"
outfileFormat = "./mc_u3s-chib1_omega_enrichedSignalMC_"+tree+"_noLog"
f = TFile(filename,"READ")
t = f.Get(tree)
pizmass = RooRealVar('pizmass','pizmass',0.12,0.15)
lb = pizmass.getMin()
rb = pizmass.getMax();
nBins=100

plot_pi0mass_true()
#c1.SaveAs(outfileFormat+"_pi0mass.pdf"+"(")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-26","#gamma_{FSR} + Leptonic Shower", ": #pi^{0} Backgrounds in Signal Channel","_GfsrLeptonicShower", 0.6)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-25","#gamma_{FSR} + Hadronic Shower", ": #pi^{0} Backgrounds in Signal Channel","_GfsrHadronicShower", 0.55)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-24","Hadronic Shower + Leptonic Shower", ": #pi^{0} Backgrounds in Signal Channel","_hadronicShowerLeptonicShower", 0.45)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-23","#gamma_{transition} + #gamma_{FSR}", ": #pi^{0} Backgrounds in Signal Channel","_GtransitionGfsr", 0.65)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-22","#gamma_{transition} + Leptonic Shower", ": #pi^{0} Backgrounds in Signal Channel","_GtransitionLeptonicShower", 0.6)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==-21","#gamma_{transition} + Hadronic Shower", ": #pi^{0} Backgrounds in Signal Channel","_GtransitionHadronicShower", 0.6)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==7","#gamma_{transition} + #gamma_{#pi^{0}}", ": #pi^{0} Backgrounds in Signal Channel","_GtransitionGpi0", 0.7)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==15","#gamma_{FSR} + #gamma_{#pi^{0}}", ": #pi^{0} Backgrounds in Signal Channel","_GfsrGpi0", 0.7)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==17","Hadronic Shower + #gamma_{#pi^{0}}", ": #pi^{0} Backgrounds in Signal Channel","_hadronicShowerGpi0", 0.65)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==18","Electronic Shower + #gamma_{#pi^{0}}", ": #pi^{0} Backgrounds in Signal Channel","_electronicShowerGpi0", 0.63)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf")
#plot_pi0mass("","All #pi^{0} Candidates","pi0tru==19","Muonic Shower + #gamma_{#pi^{0}}", ": #pi^{0} Backgrounds in Signal Channel","_muonicShowerGpi0", 0.65)
#c1.SaveAs(outfileFormat+"_pi0mass.pdf"+")")

