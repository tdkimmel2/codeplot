import math

MomBins = [0,1.25,1.625,2.0,2.375,2.75,3.125,3.5]

DataYields = [47437.0,40420.0,28235.0,16630.0,8783.0,5511.0,3267.0,4175.0]
DataErrors = [85.0,143.0,286.0,490.0,100.0,284.0,11.0,78.0]

MCYields = [49702.0,40884.0,27452.0,15779.0,7933.0,4766.0,2310.0,2451.0]
MCErrors = [67.0,58.0,220.0,282.0,137.0,90.0,98.0,358.0]

print("Bins \t Momentum(GeV/c) \t Efficiency")
for i in range(len(DataYields)):
    #print i
    data = DataYields[i]
    mc = MCYields[i]
    eff = data/mc
    daterr = DataErrors[i]
    mcerr = MCErrors[i]
    err = math.sqrt((daterr/data)**2+(mcerr/mc)**2)*eff
    if i+1!=len(DataYields):
        print("%s \t %.3f-%.3f \t\t %.4f +- %.4f"%(i+1,MomBins[i],MomBins[i+1],eff,err))
    else:
        print("%s \t >%.3f \t\t %.4f +- %.4f"%(i+1,MomBins[i],eff,err))
