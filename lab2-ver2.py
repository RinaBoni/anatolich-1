import nashpy as nash
import numpy as np
# Create the payoff matrix

A = np.array([[2,0],[4,2]]) # A is the row player
B = np.array([[4,2],[2,0]]) # B is the column player
game1 = nash.Game(A,B)
game1

# Find the Nash Equilibrium with Support Enumeration

equilibria = game1.support_enumeration()
for eq in equilibria:
    print(eq)

# # Create the payoff matrix
#
# A = np.array([[4,0],[0,2]]) # A is the row player
# B = np.array([[2,0],[0,4]]) # B is the column player
# game2 = nash.Game(A,B)
# # game2
#
# # Find the Nash Equilibrium with Support Enumeration
#
# equilibria = game2.support_enumeration()
# for eq in equilibria:
#     print(eq)
#
# # Calculate Utilities
#
# sigma_r = np.array([.67,.33])
# sigma_c = np.array([.33,.67])
# pd = nash.Game(A, B)
# pd[sigma_r, sigma_c]
#
# #ur(σr,σc)
# ur=0.67*0.33*4 +0.33*0.67*0+0.33*0.67*0+0.33*0.67*2
#
#
# uc = 0.33*0.67*2 + 0.67*0.33*0 + 0.33*0.67*0+0.67*0.33*4