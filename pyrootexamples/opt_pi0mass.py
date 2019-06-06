from ROOT import *
import math, sys, os

def printHeader():
	print("Define the type of optimization, ie. (var > CUT) OR (var < CUT)")
	print('type = "lt" : for (var < CUT)')
	print('type = "gt" : for (var > CUT)')

def optimizeCut_greaterThan():
	c1 = TCanvas("c1","",800,800)
	histPad = TPad("histPad","",0.0,0.32,1.0,1.0)
	fomPad = TPad("fomPad","",0.0,0.0,1.0,0.32)
	histPad.SetLeftMargin(0.15)
	histPad.SetTopMargin(0.1)
	histPad.SetBottomMargin(0.02)
	histPad.SetGrid()
	#histPad.SetLogy(1)
	fomPad.SetLeftMargin(0.15)
	fomPad.SetTopMargin(0.04)
	fomPad.SetBottomMargin(0.45)
	fomPad.SetGrid()
	histPad.Draw()
	fomPad.Draw()
	histPad.cd()

	f = TFile(filename,"READ")
	t = f.Get(tree)

	lb = pi0mass.getMin()
	rb = pi0mass.getMax();
	h1 = TH1F("h1","h1",nBins,lb,rb)
	h1.SetLineColor(kBlue)
	h1.SetLineWidth(2)
	h1.SetMinimum(1)
	h2 = TH1F("h2","h2",nBins,lb,rb)
	h2.SetLineColor(kRed)
	h2.SetLineStyle(kDashed)
	h2.SetLineWidth(2)
	h2.SetMinimum(1)

	#---------------------------
	# Begin Optimization Routine
	#---------------------------
	# First Count total number of Bkg and Signal
	nSigTotal = t.Draw("pi0mass>>h1",SignalCUT,"goff")
	nBkgTotal = t.Draw("pi0mass>>h2",BkgCUT,"goff")

	nSigRetained=[]
	nBkgRetained=[]
	FOM=[]

	binWidth = (rb-lb)/nBins

	for i in range(0,nBins):
		CUT = lb + i*binWidth
		#CUT=(float(i+1)/100)-1
		nSigRetained.append(t.Draw("pi0mass>>h1",SignalCUT+"&&pi0mass>%f"%CUT,"goff"))
		nBkgRetained.append(t.Draw("pi0mass>>h2",BkgCUT+"&&pi0mass>%f"%CUT,"goff"))
		print("\npi0mass > %.4f"%CUT)			
		#print nBkgRetained
		#print nSigRetained
# Define FIGURE OF MERIT (FOM) 
		denominator = math.sqrt(nSigRetained[i]+nBkgRetained[i])
		FOM.append(nSigRetained[i]/float(denominator))
		print("FOM = %.3f"%FOM[i])

	print("The maximal figure of merit is %.3f"%max(FOM))
	optimalIteration = FOM.index(max(FOM))
	optimalCut = lb+optimalIteration*binWidth
	print "This is attained for a cut of pi0mass > %.3f"%optimalCut
	effiRetainSIG = float(nSigRetained[optimalIteration])/nSigTotal
	effiRejectBKG = float(nBkgTotal - nBkgRetained[optimalIteration])/nBkgTotal
	print("Effi_rejectBKG = %.3f"%effiRejectBKG)
	print("Effi_retainSIG = %.3f"%effiRetainSIG)
	#---------------------------
	# End Optimization Routine
	#---------------------------
	bottomBound = min(FOM)
	topBound = max(FOM)
	topBound+=int(float(topBound-bottomBound)/6+0.5)
	bottomBound-=int(float(topBound-bottomBound)/6+0.5)
	RESULT = "#splitline{Optimal Cut:}{%s > %.3f}"%(xAxisTitle,optimalCut)
	tex1 = TLatex(0.72,0.15,RESULT)
	tex1.SetTextSize(0.1)
	tex1.SetNDC()



	frame1 = pi0mass.frame();
	frame1.SetTitle(TITLE);
	frame1.GetXaxis().CenterTitle(True);
	frame1.GetXaxis().SetLabelOffset(0.02);
	frame1.GetXaxis().SetLabelSize(0.05);
	frame1.GetXaxis().SetTitle("");
	frame1.GetXaxis().SetTitleSize(0.05);
	frame1.GetXaxis().SetTitleOffset(1.5);
	frame1.GetYaxis().CenterTitle(True);
	frame1.GetYaxis().SetTitleOffset(1.4);
	frame1.GetYaxis().SetLabelSize(0.05);
	frame1.GetYaxis().SetTitleSize(0.05);
	frame1.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins);
	frame1.SetMinimum(1)

	# Draw pi0mass histograms
	t.Draw("pi0mass>>h1",SignalCUT)
	t.Draw("pi0mass>>h2",BkgCUT)
	frame1.addTH1(h1)
	frame1.addTH1(h2)
	maxY = [h1.GetMaximum(), h2.GetMaximum()]
	minY = [h1.GetMinimum(), h2.GetMinimum()]
	topArrow = max(maxY)
	bottomArrow= min(minY)
	topArrow = int(2*float(topArrow)/10+0.5)
	bottomArrow += int(float(topArrow-bottomArrow)/20+0.5)
	a = TArrow(optimalCut, bottomArrow, optimalCut, topArrow,0.02,"<|")
	a.SetLineWidth(3)
	a.SetLineColor(kBlack)
	a.SetLineStyle(7)
	l = TLine(optimalCut, bottomBound, optimalCut, topBound)
	l.SetLineWidth(2)
	l.SetLineColor(kBlack)
	l.SetLineStyle(7)
	frame1.addObject(a)
	h1.Draw()
	h2.Draw()
	legLB=0.55
	leg = TLegend(legLB,0.74,0.34+legLB,0.89)
	leg.SetFillColor(kWhite)
	leg.SetLineColor(kWhite)
	leg.SetTextSize(0.04)
	leg.AddEntry(frame1.findObject('h1'),SignalLegendTitle,"l")
	leg.AddEntry(frame1.findObject('h2'),BkgLegendTitle,"l")
	frame1.addObject(leg)
	frame1.Draw()
	histPad.cd()
	histPad.Draw()
	histPad.Draw()

	fomPad.cd()
	hFOM = TH1F("hFOM","hFOM",nBins,lb,rb)
	hFOM.SetLineColor(kBlack)
	# Fill FOM histogram	
	for k in range (0,nBins):  
	    hFOM.SetBinContent(k,FOM[k])
	hFOM.Draw()

	fomFrame = pi0mass.frame()
	fomFrame.SetTitle("")
	fomFrame.GetXaxis().CenterTitle(True)
	fomFrame.GetXaxis().SetLabelOffset(0.03)
	fomFrame.GetXaxis().SetLabelSize(0.07)
	fomFrame.GetXaxis().SetTitle(xAxisTitle)
	fomFrame.GetXaxis().SetTitleSize(0.1)
	fomFrame.GetXaxis().SetTitleOffset(1.7)
	fomFrame.GetYaxis().CenterTitle(True)
	fomFrame.GetYaxis().SetTitleOffset(0.55)
	fomFrame.GetYaxis().SetLabelSize(0.05)
	fomFrame.GetYaxis().SetTitleSize(0.1)
	fomFrame.GetYaxis().SetTitle("#frac{S}{#sqrt{S+B}}")

	fomFrame.addTH1(hFOM);
	fomFrame.addObject(l);
	fomFrame.addObject(tex1)
	fomFrame.SetAxisRange(bottomBound,topBound,"Y")

	fomPad.SetTickx()
	fomPad.SetTicky()
	fomFrame.SetStats(0)
	fomFrame.Draw()
	fomPad.Draw()
	histPad.cd()

	c1.SaveAs(pdfname)
	os.system("open %s"%pdfname)


def optimizeCut_lessThan():
	c1 = TCanvas("c1","",800,800)
	histPad = TPad("histPad","",0.0,0.32,1.0,1.0)
	fomPad = TPad("fomPad","",0.0,0.0,1.0,0.32)
	histPad.SetLeftMargin(0.15)
	histPad.SetTopMargin(0.1)
	histPad.SetBottomMargin(0.02)
	histPad.SetGrid()
	#histPad.SetLogy(1)
	fomPad.SetLeftMargin(0.15)
	fomPad.SetTopMargin(0.04)
	fomPad.SetBottomMargin(0.45)
	fomPad.SetGrid()
	histPad.Draw()
	fomPad.Draw()
	histPad.cd()

	f = TFile(filename,"READ")
	t = f.Get(tree)

	lb = pi0mass.getMin()
	rb = pi0mass.getMax();
	h1 = TH1F("h1","h1",nBins,lb,rb)
	h1.SetLineColor(kBlue)
	h1.SetLineWidth(2)
	h1.SetMinimum(1)
	h2 = TH1F("h2","h2",nBins,lb,rb)
	h2.SetLineColor(kRed)
	h2.SetLineStyle(kDashed)
	h2.SetLineWidth(2)
	h2.SetMinimum(1)

	#---------------------------
	# Begin Optimization Routine
	#---------------------------
	# First Count total number of Bkg and Signal
	nSigTotal = t.Draw("pi0mass>>h1",SignalCUT,"goff")
	nBkgTotal = t.Draw("pi0mass>>h2",BkgCUT,"goff")

	nSigRetained=[]
	nBkgRetained=[]
	FOM=[]

	binWidth = (rb-lb)/nBins

	for i in range(0,nBins):
		print i
		CUT = rb - i*binWidth
		#CUT=(float(i+1)/100)-1
		nSigRetained.append(t.Draw("pi0mass>>h1",SignalCUT+"&&pi0mass<%f"%CUT,"goff"))
		nBkgRetained.append(t.Draw("pi0mass>>h2",BkgCUT+"&&pi0mass<%f"%CUT,"goff"))
		print("\npi0mass < %.4f"%CUT)			
		#print nBkgRetained
		#print nSigRetained
# Define FIGURE OF MERIT (FOM) 
		denominator = math.sqrt(nSigRetained[i]+nBkgRetained[i])
		FOM.append(nSigRetained[i]/float(denominator))
		print("FOM = %.3f"%FOM[i])

	print("The maximal figure of merit is %.3f"%max(FOM))
	optimalIteration = FOM.index(max(FOM))
	optimalCut = rb-optimalIteration*binWidth
	print "This is attained for a cut of pi0mass < %.3f"%optimalCut
	effiRetainSIG = float(nSigRetained[optimalIteration])/nSigTotal
	effiRejectBKG = float(nBkgTotal - nBkgRetained[optimalIteration])/nBkgTotal
	print("Effi_rejectBKG = %.3f"%effiRejectBKG)
	print("Effi_retainSIG = %.3f"%effiRetainSIG)
	#---------------------------
	# End Optimization Routine
	#---------------------------
	bottomBound = min(FOM)
	topBound = max(FOM)
	topBound+=int(float(topBound-bottomBound)/6+0.5)
	bottomBound-=int(float(topBound-bottomBound)/6+0.5)
	
	RESULT = "#splitline{Optimal Cut:}{%s < %.3f}"%(xAxisTitle,optimalCut)
	tex1 = TLatex(0.72,0.15,RESULT)
	tex1.SetTextSize(0.1)
	tex1.SetNDC()


	frame1 = pi0mass.frame();
	frame1.SetTitle(TITLE);
	frame1.GetXaxis().CenterTitle(True);
	frame1.GetXaxis().SetLabelOffset(0.02);
	frame1.GetXaxis().SetLabelSize(0.05);
	frame1.GetXaxis().SetTitle("");
	frame1.GetXaxis().SetTitleSize(0.05);
	frame1.GetXaxis().SetTitleOffset(1.5);
	frame1.GetYaxis().CenterTitle(True);
	frame1.GetYaxis().SetTitleOffset(1.4);
	frame1.GetYaxis().SetLabelSize(0.05);
	frame1.GetYaxis().SetTitleSize(0.05);
	frame1.GetYaxis().SetTitle("Events/[%.f Bins]"%nBins);
	frame1.SetMinimum(1)

	# Draw pi0mass histograms
	t.Draw("pi0mass>>h1",SignalCUT)
	t.Draw("pi0mass>>h2",BkgCUT)
	frame1.addTH1(h1)
	frame1.addTH1(h2)
	maxY = [h1.GetMaximum(), h2.GetMaximum()]
	minY = [h1.GetMinimum(), h2.GetMinimum()]
	topArrow = max(maxY)
	bottomArrow= min(minY)
	topArrow = int(2*float(topArrow)/10+0.5)
	bottomArrow += int(float(topArrow-bottomArrow)/20+0.5)
	a = TArrow(optimalCut, bottomArrow, optimalCut, topArrow,0.02,"<|")
	a.SetLineWidth(3)
	a.SetLineColor(kBlack)
	a.SetLineStyle(7)
	l = TLine(optimalCut, bottomBound, optimalCut, topBound)
	l.SetLineWidth(2)
	l.SetLineColor(kBlack)
	l.SetLineStyle(7)

	frame1.addObject(a)
	h1.Draw()
	h2.Draw()
	legLB=0.55
	leg = TLegend(legLB,0.74,0.34+legLB,0.89)
	leg.SetFillColor(kWhite)
	leg.SetLineColor(kWhite)
	leg.SetTextSize(0.04)
	leg.AddEntry(frame1.findObject('h1'),SignalLegendTitle,"l")
	leg.AddEntry(frame1.findObject('h2'),BkgLegendTitle,"l")
	frame1.addObject(leg)
	frame1.Draw()
	histPad.cd()
	histPad.Draw()
	histPad.Draw()

	fomPad.cd()
	hFOM = TH1F("hFOM","hFOM",nBins,lb,rb)
	hFOM.SetLineColor(kBlack)
	# Fill FOM histogram	
	for k in range (0,nBins):  
	    hFOM.SetBinContent(k+1,FOM[nBins-1-k])
	hFOM.Draw()

	fomFrame = pi0mass.frame()
	fomFrame.SetTitle("")
	fomFrame.GetXaxis().CenterTitle(True)
	fomFrame.GetXaxis().SetLabelOffset(0.03)
	fomFrame.GetXaxis().SetLabelSize(0.07)
	fomFrame.GetXaxis().SetTitle(xAxisTitle)
	fomFrame.GetXaxis().SetTitleSize(0.1)
	fomFrame.GetXaxis().SetTitleOffset(1.7)
	fomFrame.GetYaxis().CenterTitle(True)
	fomFrame.GetYaxis().SetTitleOffset(0.55)
	fomFrame.GetYaxis().SetLabelSize(0.05)
	fomFrame.GetYaxis().SetTitleSize(0.1)
	fomFrame.GetYaxis().SetTitle("#frac{S}{#sqrt{S+B}}")

	fomFrame.addTH1(hFOM);
	fomFrame.addObject(l);
	fomFrame.addObject(tex1)
	fomFrame.SetAxisRange(bottomBound,topBound,"Y")

	fomPad.SetTickx()
	fomPad.SetTicky()
	fomFrame.SetStats(0)
	fomFrame.Draw()
	fomPad.Draw()
	histPad.cd()

	c1.SaveAs(pdfname)
	os.system("open %s"%pdfname)


###########################################################################################
#
# User Defined Quantities
#
###########################################################################################

filename = "/Users/Stottler/Documents/GradSchool/Research/omega/rootfiles/signalMC/noRefit/mc_u3s-chib1_omega_signalMC.root" # Define Path to root file
tree = "pi0Tree" # Define TTree name

mcfile = filename.split("/")[-1:][0].strip(".root")
mcType = mcfile.split("_")[-1:][0]
pdfname = "./plots/"+mcType+"/"+mcfile+"_"+tree+"_pi0mass_ltOPT.pdf" # Define pdf name & output directory 

pi0mass = RooRealVar('pi0mass','pi0mass',0.085,0.185) # Define variable to be optimized
nBins=100 # Set Binning and consequently number of steps in the optimization

xAxisTitle = "M_{#pi^{0}}"

TITLE="From #chi_{b1}(2P) #rightarrow #omega #varUpsilon(1S) MC" # Define title of histogram
SignalCUT = "pi0tru==1"
SignalLegendTitle = "Truly Reconstructed #pi^{0}"
BkgCUT = "pi0tru!=1"
BkgLegendTitle = "Misreconstructed #pi^{0}"



# Run Optimization
optimizeCut_greaterThan()
#optimizeCut_lessThan()






