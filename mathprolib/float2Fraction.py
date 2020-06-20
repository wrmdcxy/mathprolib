from Fraction import VulgarFraction
def float2VulgarFraction(num:float):
    i = 1
    while True:
        i+=1
        if abs(round(num*i)-num*i) < 1e-3:
            return VulgarFraction(round(num*i),i)

def float2MixedFraction(num:float):
    return float2VulgarFraction(num).toMixed()
        