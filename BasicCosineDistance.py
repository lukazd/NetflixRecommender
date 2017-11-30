def cosine_distance(a, b):
    if len(a) != len(b):
        raise ValueError("a and b must be same length") #Steve
    numerator = 0
    denoma = 0
    denomb = 0
    for i in range(len(a)):       #Mike's optimizations:
        ai = a[i]             #only calculate once
        bi = b[i]
        numerator += ai*bi    #faster than exponent (barely)
        denoma += ai*ai       #strip abs() since it's squaring
        denomb += bi*bi
    result = 1 - numerator / (math.sqrt(denoma)*math.sqrt(denomb))
    return result

#Results of -1 indicates that the two vectors are exact opposites
#Results of 1 indicates that two vectors are exactly the same
