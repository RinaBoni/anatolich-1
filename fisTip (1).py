import matplotlib.pyplot as plt

def linsmf(x, a, b):
    if x < a:
        return 0
    elif x <= b:
        return (x - a) / (b - a)
    else:
        return 1

def linzmf(x, a, b):
    if x < a:
        return 1
    elif x <= b:
        return 1 - (x - a) / (b - a)
    else:
        return 0

# Sugeno algorithm of order 0
def Sugeno0(foodRank, serviceRank):
    TipLow = 5
    TipBig = 25

    # 1. Find the values of fuzzy variables
    foodIsGood = mfFoodIsGood(foodRank)
    foodIsBad = mfFoodIsBad(foodRank)
    serviceIsGood = mfServiceIsGood(serviceRank)
    serviceIsBad = mfServiceIsBad(serviceRank)

    # 2. Apply conditions
    #    1- If food is bad or service is bad, then tips are low
    #    2- If food is good and service is good, then tips are high
    ant1 = max(foodIsBad, serviceIsBad)  # At least one bad
    ant2 = min(foodIsGood, serviceIsGood)  # Both good

    # 3. Consequents (weights w_i)
    cons1 = ant1
    cons2 = ant2

    # 4. Implication
    impl1 = cons1 * TipLow
    impl2 = cons2 * TipBig

    # 5. Defuzzification, finding the centroid
    if cons1 + cons2 == 0:  # Avoid division by zero
        return 0
    resTip = (impl1 + impl2) / (cons1 + cons2)
    return resTip

# Membership functions for food quality
mfFoodIsBad = lambda rank: linzmf(rank, 0, 5)
mfFoodIsGood = lambda rank: linsmf(rank, 4, 10)

# Membership functions for service quality
mfServiceIsBad = lambda rank: linzmf(rank, 0, 5)
mfServiceIsGood = lambda rank: linsmf(rank, 4, 10)

# Collecting results
rank, resS = [], []
for foodRank in range(11):
    for serviceRank in range(11):
        rank.append((foodRank, serviceRank))
        resS.append(Sugeno0(foodRank, serviceRank))

# Plotting results
fig = plt.gcf()
plt.clf()
ax1 = fig.add_subplot(211)
ax1.plot(range(11), [mfFoodIsGood(r) for r in range(11)], label='Food is Good')
ax1.plot(range(11), [mfFoodIsBad(r) for r in range(11)], label='Food is Bad')
ax1.legend()

ax2 = fig.add_subplot(212)
ax2.plot(range(len(resS)), resS, label='Sugeno Tips')
ax2.legend()
plt.show()