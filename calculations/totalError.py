import math

klgen = 130971.0
lgner = math.sqrt(klgen)
#lgner = 0.0
klmcr = 19770.0
klmce = 809.0
#klmce = 0.0
kleff = klmcr/klgen
lefer = kleff*math.sqrt((lgner/klgen)**2 + (klmce/klmcr)**2)
print("KL Efficiency: %.4f +- %.4f"%(kleff,lefer))
ksgen = 90638.0
sgner = math.sqrt(ksgen)
#sgner = 0.0
ksmcr = 23983.0
ksmce = 335.0
#ksmce = 0.0
kseff = ksmcr/ksgen
sefer = kseff*math.sqrt((sgner/ksgen)**2 + (ksmce/ksmcr)**2)
print("KS Efficiency: %.4f +- %.4f"%(kseff,sefer))

#D*+-
numkl = 135382.0
nkler = 1101.0
numks = 161020.0
nkser = 913.0
#D*+
"""
numkl = 72046.0
nkler = 1154.0
numks = 88919.0
nkser = 617.0
"""
#D*-
"""
numkl = 75878.0
nkler = 1054.0
numks = 89867.0
nkser = 588.0
"""
#PartialData
"""
numkl = 6247.0/(0.5283*1.0633)
nkler = 645.0
numks = 17357.0/(0.9828*0.9981*1.0681)
nkser = 282.0
"""

brmes = 0.6920
brerr = 0.0005

x=numkl*kseff*brmes
xerr = numkl*kseff*brmes*math.sqrt((sefer/kseff)**2 + (nkser/numks)**2 + (brerr/brmes)**2)
y=numks*kleff
yerr = numks*kleff*math.sqrt((lefer/kleff)**2 + (nkler/numkl)**2)
num = x-y
den = x+y

Err = math.sqrt((4*(y**2*xerr**2+x**2*yerr**2)/(x+y)**4))
syserrl = 0.0175
syserrs = 0.0037
syserr = math.sqrt(syserrl**2+syserrs**2)
print syserr
sysErr = (x-y)/(x+y)*math.sqrt((syserrl/numkl)**2+(syserrs/numks)**2)
print("%.4f +- %.4f +- %.4f"%(num/den,Err,sysErr))
nds = 17590262.0
ksgenn = 131655.0
nksser = math.sqrt(ksgenn)
ndser = math.sqrt(nds)
xgen = ksgenn/nds
xgenerr = xgen*math.sqrt((nksser/ksgenn)**2 + (ndser/nds)**2)
ygen = klgen/nds
ygenerr = ygen*math.sqrt((nkler/numkl)**2 + (ndser/nds)**2)
rd0gen = (ksgenn/nds - klgen/nds)/(ksgenn/nds + klgen/nds)
rd0gener = math.sqrt((4*(ygen**2*xgenerr**2+xgen**2*ygenerr**2)/(xgen+ygen)**4))
print("%.4f +- %.4f"%(rd0gen,rd0gener))
