import math
from ROOT import *

f = TFile("/home/tkimmel/Research/root/allmfrecon.root","READ")
t = f.Get("reald0tree")
ts = f.Get("realdecay0stree")
tl = f.Get("realdecay0ltree")
tstar = f.Get("realdstree")
tsstar = f.Get("realdecaystree")
tlstar = f.Get("realdecayltree")

num = float(t.Draw("mcflag","","goff"))
numkl = float(tl.Draw("mcflag","","goff"))
numks = float(ts.Draw("mcflag","","goff"))
brks = numks/num
brkl = numkl/num
print("D0D0-bar: %.4f"%((brks-brkl)/(brks+brkl)))

num = float(t.Draw("mcflag","chrgflag==1","goff"))
numkl = float(tl.Draw("mcflag","chrgflag==1","goff"))
numks = float(ts.Draw("mcflag","chrgflag==1","goff"))
brks = numks/num
brkl = numkl/num
print("D0: %.4f"%((brks-brkl)/(brks+brkl)))

num = float(t.Draw("mcflag","chrgflag==-1","goff"))
numkl = float(tl.Draw("mcflag","chrgflag==-1","goff"))
numks = float(ts.Draw("mcflag","chrgflag==-1","goff"))
brks = numks/num
brkl = numkl/num
print("D0-bar: %.4f"%((brks-brkl)/(brks+brkl)))

num = float(tstar.Draw("mcflag","","goff"))
numkl = float(tlstar.Draw("mcflag","","goff"))
numks = float(tsstar.Draw("mcflag","","goff"))
brks = numks/num
brkl = numkl/num
print("D*+-: %.4f"%((brks-brkl)/(brks+brkl)))

num = float(tstar.Draw("mcflag","chrgflag==1","goff"))
numkl = float(tlstar.Draw("mcflag","chrgflag==1","goff"))
numks = float(tsstar.Draw("mcflag","chrgflag==1","goff"))
brks = numks/num
brkl = numkl/num
print("D*+: %.4f"%((brks-brkl)/(brks+brkl)))

num = float(tstar.Draw("mcflag","chrgflag==-1","goff"))
numkl = float(tlstar.Draw("mcflag","chrgflag==-1","goff"))
numks = float(tsstar.Draw("mcflag","chrgflag==-1","goff"))
brks = numks/num
brkl = numkl/num
print("D*-: %.4f"%((brks-brkl)/(brks+brkl)))
