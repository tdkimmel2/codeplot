import sys
import math

Nsig = 171764.0
Nsigerr = 1316

eff = 0.074444
efferr = 0.002619

bdst = 0.307
bdsterr = 0.005

bks = 0.6920
bkserr = 0.0005

ND = 780319184.0
NDerr = math.sqrt(ND)

#bdzs = Nsig/(eff*bdst*ND)
#bdzserr = bdzs*math.sqrt((Nsigerr/Nsig)**2 + (efferr/eff)**2 + (bdsterr/bdst)**2 + (NDerr/ND)**2)
bdzs = Nsig/(eff*bdst*bks*ND)
bdzserr = bdzs*math.sqrt((Nsigerr/Nsig)**2 + (efferr/eff)**2 + (bdsterr/bdst)**2 + (bkserr/bks)**2 + (NDerr/ND)**2)

print("The branching fraction of D0 -> K0S pi0 is: %f +- %f"%(bdzs,bdzserr))

Nsig = 157529.0
Nsigerr = 4314

eff = 0.094734
efferr = 0.00285

bdzl = Nsig/(eff*bdst*ND)
bdzlerr = bdzl*math.sqrt((Nsigerr/Nsig)**2 + (efferr/eff)**2 + (bdsterr/bdst)**2 + (NDerr/ND)**2)

print("The branching fraction of D0 -> K0L pi0 is: %f +- %f"%(bdzl,bdzlerr))

R = (bdzs-bdzl)/(bdzs+bdzl)
print R
