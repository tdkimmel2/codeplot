import math

MomBins = [1,1.25,1.625,2.0,2.375,2.75,3.125,3.5]

PlusDataYields = [25964.0,40269.0,27734.0,15945.0,8803.0,5031.0,2848.0,3594.0]
PlusDataErrors = [165.0,211.0,201.0,174.0,148.0,134.0,100.0,98.0]

PlusMCYields = [27055.0,41859.0,27696.0,15400.0,8009.0,4263.0,2293.0,2509.0]
PlusMCErrors = [172.0,207.0,187.0,170.0,128.0,103.0,85.0,86.0]

MinusDataYields = [26038.0,40523.0,28019.0,16188.0,8931.0,5120.0,2683.0,3645.0]
MinusDataErrors = [166.0,406.0,200.0,178.0,152.0,138.0,90.0,109.0]

MinusMCYields = [27130.0,42179.0,27953.0,15581.0,8100.0,4319.0,2319.0,2584.0]
MinusMCErrors = [120.0,406.0,198.0,177.0,139.0,107.0,87.0,171.0]

asyms = [0.9578,0.9613,1.0014,1.0361,1.0995,1.2202,1.1646,1.4163]

print("Bins \t Momentum(GeV/c) \t %Diff")
for i in range(len(PlusDataYields)):
    #print i
    dataP = PlusDataYields[i]
    dataM = MinusDataYields[i]
    mcP = PlusMCYields[i]
    mcM = MinusMCYields[i]
    eff = asyms[i]
    errP = dataP/mcP*math.sqrt((PlusDataErrors[i]/dataP)**2+(PlusMCErrors[i]/mcP)**2)
    errM = dataM/mcM*math.sqrt((MinusDataErrors[i]/dataM)**2+(MinusMCErrors[i]/mcM)**2)
    diffP = ((dataP/mcP) - eff)/eff
    diffM = ((dataM/mcM) - eff)/eff
    diff = (diffP+diffM)/2
    if i+1!=len(PlusDataYields):
        print("%s \t %.3f-%.3f \t\t %.4f +- %.4f"%(i+1,MomBins[i],MomBins[i+1],diff,errP))
    else:
        print("%s \t >%.3f \t\t %.4f +- %.4f"%(i+1,MomBins[i],diff,errM))
