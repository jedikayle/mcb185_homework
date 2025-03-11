# Assessment
import math

def isprobdist(prob):
    total = 0
    for p in prob: 
        total += p
        if p < 0 or p > 1: return False
    if math.isclose(total, 1.0): return True
    else: return False 
    z
p1 = 0.3, 0.2, 0.5
p2 = 0.3, 0.3, 0.3, 0.07
p3 = 0.8, 0.5, -20.0

print(isprobdist(p1))
print(isprobdist(p2))
print(isprobdist(p3))



