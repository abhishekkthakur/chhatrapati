import math

## Function to calculate the Gibbs energy
def gibbsCalculate(tempElemA, tempElemB, T):
    R = 8.314
    if (tempElemA == 'Cr'):
        if (T <= 2180):
            g0ElemA = -8856.94 + 157.48 * T - 26.908 * T * math.log(T) + 1.89435E-3 *T**2 - 1.47721E-6 * T**3 + 139250 * T**(-1)
        else:
            g0ElemA = -34869.344 + 344.18 * T - 50 * T * math.log(T) - 2885.26E29 * T**(-9)
    elif (tempElemA == 'W'):
        if (T <= 3695):
            g0ElemA = -7646.311 + 130.4 * T - 24.1 * T * math.log(T) - 1.936E-3 * T**2 + 0.207E-6 * T**3 + 44500 * T**(-1) - 0.0533E-9 * T**4
        else:
            g0ElemA = -82868.801 + 389.362335 * T - 54 * T * math.log(T) + 1528.621E30 * T**(-9)
    else:
        if (T <= 1300):
            g0ElemA = -7285.889 + 119.139857 * T - 23.7592624 * T * math.log(T) - 2.623033E-3 * T**2 + 0.170109E-6 * T**3 -3293 * T**(-1)
        elif (T <= 2500):
            g0ElemA = -22389.955 + 243.88676 * T - 41.137088 * T * math.log(T) + 6.167572E-3 * T**2 - 0.655136E-6 * T**3 + 2429586 * T**(-1)
        elif (T <= 3290):
            g0ElemA = 229382.886 - 722.59722 * T + 78.5244752 * T * math.log(T) - 17.983376E-3 * T**2 + 0.195033E-6 *T**3 - 93813648 * T**(-1)
        else:
            g0ElemA = -1042384.014 + 2985.491246 * T - 362.1591318 * T * math.log(T) + 43.117795E-3 * T**2 - 1.055148E-6 * T**3 + 554714342 * T**(-1)
    if (tempElemB == 'Cr'):
        if (T <= 2180):
            g0ElemB = -8856.94 + 157.48 * T - 26.908 * T * math.log(T) + 1.89435E-3 *T**2 - 1.47721E-6 * T**3 + 139250 * T**(-1)
        else:
            g0ElemB = -34869.344 + 344.18 * T - 50 * T * math.log(T) - 2885.26E29 * T**(-9)
    elif (tempElemB == 'W'):
        if (T <= 3695):
            g0ElemB = -7646.311 + 130.4 * T - 24.1 * T * math.log(T) - 1.936E-3 * T**2 + 0.207E-6 * T**3 + 44500 * T**(-1) - 0.0533E-9 * T**4
        else:
            g0ElemB = -82868.801 + 389.362335 * T - 54 * T * math.log(T) + 1528.621E30 * T**(-9)
    else:
        if (T <= 1300):
            g0ElemB = -7285.889 + 119.139857 * T - 23.7592624 * T * math.log(T) - 2.623033E-3 * T**2 + 0.170109E-6 * T**3 -3293 * T**(-1)
        elif (T <= 2500):
            g0ElemB = -22389.955 + 243.88676 * T - 41.137088 * T * math.log(T) + 6.167572E-3 * T**2 - 0.655136E-6 * T**3 + 2429586 * T**(-1)
        elif (T <= 3290):
            g0ElemB = 229382.886 - 722.59722 * T + 78.5244752 * T * math.log(T) - 17.983376E-3 * T**2 + 0.195033E-6 *T**3 - 93813648 * T**(-1)
        else:
            g0ElemB = -1042384.014 + 2985.491246 * T - 362.1591318 * T * math.log(T) + 43.117795E-3 * T**2 - 1.055148E-6 * T**3 + 554714342 * T**(-1)

    
    return g0ElemA, g0ElemB