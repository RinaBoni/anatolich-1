#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Нечётко-логическая система.
Решение задачи с чаевыми (и далее переход к системе управления)
"""
import matplotlib.pyplot as plt

#  Функции принадлежности, логические функции (нечёткие)
def linsmf(x,a,b):
    if x<a:
        return 0
    elif x<=b:
        return (x-a)/(b-a)
    else:
        return 1

def linzmf(x,a,b):
    if x<a:
        return 1
    elif x<=b:
        return 1-(x-a)/(b-a)
    else:
        return 0

def trapmf(x, a,b,c,d):
    return max(min((x-a)/(b-a),1,(d-x)/(d-c)),0)

def notf(a):
    return 1-a
def orf(*A):
    return max(*A)
def andf(*A):
    return min(*A)



# алгоритм Сугено, порядок 0
def Sugeno0(foodRank):
    TipLow = 5
    TipBig = 25

    # 1. Находим значения логических переменных
    foodIsGood = mfFoodIsGood(foodRank)
    foodIsBad  = mfFoodIsBad(foodRank)

    # 2. Применяем условия
    #    1- Если еда так себе, то чаевые маленькие
    #    2- Если еда вкусная, то чаевые щедрые
    ant1 = foodIsBad
    ant2 = foodIsGood

    # 3. Выводы (consequent), они же веса w_i
    cons1 = ant1
    cons2 = ant2

    # 4. Импликация (а здесь единственное число)
    impl1 = cons1 * TipLow
    impl2 = cons2 * TipBig

    # 4. Агрегации как таковой и нет..
    # 5. Дефаззификация, находим ЦМ
    resTip = (impl1+impl2)/(cons1+cons2)
    return resTip


# Сугено (0-го порядка)
mfFoodIsBad  = lambda rank: linzmf(rank, 0, 10)
mfFoodIsGood = lambda rank: linsmf(rank, 0, 8)

rank, resS = [], []
foodIsBad, foodIsGood = [], []
for r in range(10 + 1):
    rank.append(r)
    resS.append( Sugeno0(r))
    foodIsBad.append(mfFoodIsBad(r))
    foodIsGood.append(mfFoodIsGood(r))


fig = plt.gcf()
plt.clf()
ax1 = fig.add_subplot(211)
ax1.plot(rank, foodIsGood, rank, foodIsBad)
plt.legend(['foodIsGood', 'foodIsBad'])

ax2 = fig.add_subplot(212)
ax2.plot(rank, resS)
plt.legend(['Sugeno'])
plt.show()
