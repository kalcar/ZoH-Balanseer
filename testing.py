import matplotlib.pyplot as plt
import DiceRoller as dr



d6 = dr.die(6)
d12 = dr.die(12)

local_chara = dr.dicetower(d12,d12,d6)
rolls = 1000000
roll_histogram = [0] * (local_chara.stack.get_max_roll() - local_chara.stack.get_min_roll())

for roll in range(rolls):

    roll_histogram[local_chara.stack.roll() - local_chara.stack.get_min_roll()-1] += 1
    

print(roll_histogram)
 


plt.plot( range(local_chara.stack.get_max_roll() - local_chara.stack.get_min_roll()), roll_histogram)
plt.ylabel('hits')
plt.show()
