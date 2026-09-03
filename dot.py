lol = [1, 2, 3, 2, 5, 1]


def GetMax(lol):
    max_num = lol[0]

    for x in lol:
        if x > max_num:
            max_num = x

    return max_num


def GetMin(lol):
    min_num = lol[0]

    for x in lol:
        if x < min_num:
            min_num = x

    return min_num


def GetSum(lol):
    total = 0

    for x in lol:
        total += x

    return total


def GetProduct(lol):
    product = 1

    for x in lol:
        product *= x

    return product


def GetInvSum(lol):
    total = 0

    for x in lol:
        if x != 0:
            total += 1 / x

    return total


def GetArithmeticMean(lol):
    return GetSum(lol) / len(lol)


def GetGeometricMean(lol):
    product = GetProduct(lol)
    return product ** (1 / len(lol))


def GetHarmonicMean(lol):
    return len(lol) / GetInvSum(lol)


def GetMedian(lol):
    temp = sorted(lol)
    n = len(temp)

    if n % 2 == 0:
        return (temp[n // 2 - 1] + temp[n // 2]) / 2
    else:
        return temp[n // 2]


def GetModus(lol):
    freq = {}

    for x in lol:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    max_count = 0
    modus = None

    for key in freq:
        if freq[key] > max_count:
            max_count = freq[key]
            modus = key

    return modus


def GetFrequency(lol):
    freq = {}

    for x in lol:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq


def WriteFrequency(lol):
    freq = GetFrequency(lol)

    print("Absolutní frekvence:")

    for key in freq:
        print(key, "->", freq[key])


def WriteRelativeFrequency(lol):
    freq = GetFrequency(lol)

    print("Relativní frekvence:")

    for key in freq:
        print(key, "->", (freq[key] / len(lol)) * 100, "%")


def WriteHistogram(lol):
    freq = GetFrequency(lol)

    print("Histogram:")

    for key in freq:
        print(str(key) + ": " + "*" * freq[key])


print("Max:", GetMax(lol))
print("Min:", GetMin(lol))
print("Sum:", GetSum(lol))
print("Product:", GetProduct(lol))
print("InvSum:", GetInvSum(lol))
print("ArithmeticMean:", GetArithmeticMean(lol))
print("GeometricMean:", GetGeometricMean(lol))
print("HarmonicMean:", GetHarmonicMean(lol))
print("Median:", GetMedian(lol))
print("Modus:", GetModus(lol))

WriteFrequency(lol)
WriteRelativeFrequency(lol)
WriteHistogram(lol)