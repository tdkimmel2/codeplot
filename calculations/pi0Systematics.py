import math

MomBins = [1,1.25,1.625,2.0,2.375,2.75,3.125,3.5]

DataYields = [25983.0,40292.0,27846.0,16035.0,8852.0,5065.0,2667.0,3569.0]
DataErrors = [165.0,208.0,200.0,171.0,150.0,136.0,88.0,107.0]

MCYields = [27128.0,41914.0,27808.0,15477.0,8051.0,4151.0,2290.0,2520.0]
MCErrors = [171.0,212.0,189.0,165.0,128.0,106.0,85.0,87.0]

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
