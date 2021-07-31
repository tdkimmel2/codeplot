import math

#D* Systematics
"""
ksmc = 15889.0
ksmcerr = 395.0
ksdat = 12576.0
ksdaterr = 772.0
kspiz = 0.9787
kspizerr = 0.0
kseff = 0.9780
ksefferr = 0.0
kspi = 0.9919
kspierr = 0.0

klmc = 11740.0
klmcerr = 2866.0
kldat = 3172.0
kldaterr = 258.0
klpiz = 0.9793
klpizerr = 0.0
kleff = 0.4923
klefferr = 0.0
klpi = 0.9881
klpierr = 0.0
"""

#Fixed Sigma Ratios
ksmcP = 17355.0
ksmcPerr = 384.0
ksmcM = 17435.0
ksmcMerr = 345.0
ksdatP = 17354.0
ksdatPerr = 296.0
ksdatM = 17350.0
ksdatMerr = 296.0
klmcP = 13899.0
klmcPerr = 484.0
klmcM = 13781.0
klmcMerr = 511.0
kldatP = 6241.0
kldatPerr = 702.0
kldatM = 6214.0
kldatMerr = 611.0
#Partial Data
ksmc = 17336.0
ksmcerr = 458.0
ksdat = 17357.0
ksdaterr = 282.0
kspiz = 1.0682
#kspizerr = 0.0245
kspizerr = 0.0
kseff = 0.9828
#ksefferr = 0.0114
ksefferr = 0.0
kspi = 0.9981
#kspierr = 0.0050
kspierr = 0.0

klmc = 14126.0
klmcerr = 887.0
kldat = 6247.0
kldaterr = 647.0
klpiz = 1.0632
#klpizerr = 0.0240
klpizerr = 0.0
kleff = 0.5283
#klefferr = 0.1179
klefferr = 0.0
klpi = 1.0001
#klpierr = 0.0033
klpierr = 0.0

kseff1 = ksdat/ksmc
kseffP = ksdatP/ksmcP
kseffM = ksdatM/ksmcM
print("Fixed ratio systematic for KShort: %.4f"%((((kseffP-kseff1)/kseff1)+(kseffM-kseff1)/kseff1)/2))
kleff1 = kldat/klmc
kleffP = kldatP/klmcP
kleffM = kldatM/klmcM
print("Fixed ratio systematic for KLong: %.4f"%((((kleffP-kleff1)/kleff1)+(kleffM-kleff1)/kleff1)/2))

kscalc = ksdat/(kspiz*kseff*kspi)
kscalcerr = kscalc*math.sqrt((ksdaterr/ksdat)**2 + (kspizerr/kspiz)**2 + (ksefferr/kseff)**2 + (kspierr/kspi)**2)
print("KShort Calc: %.4f +- %.4f"%(kscalc,kscalcerr))

klcalc = kldat/(klpiz*kleff*klpi)
klcalcerr = klcalc*math.sqrt((kldaterr/kldat)**2 + (klpizerr/klpiz)**2 + (klefferr/kleff)**2 + (klpierr/klpi)**2)
print("KLong Calc: %.4f +- %.4f"%(klcalc,klcalcerr))

ksdseff = kscalc/ksmc
ksdsefferr = ksdseff*math.sqrt((kscalcerr/kscalc)**2 + (ksmcerr/ksmc)**2)
print("KShort Efficiency: %.4f +- %.4f"%(ksdseff,ksdsefferr))

kldseff = klcalc/klmc
kldsefferr = kldseff*math.sqrt((klcalcerr/klcalc)**2 + (klmcerr/klmc)**2)
print("KLong Efficiency: %.4f +- %.4f"%(kldseff,kldsefferr))
