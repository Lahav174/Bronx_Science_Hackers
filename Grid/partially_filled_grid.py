import random
import numpy as np

odds_of_grain = 30
width, height = 20, 34
Map = (np.random.randint(100, size=(height,width)) < odds_of_grain).astype(int)
print(Map)