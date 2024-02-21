import matplotlib.pyplot as plt
import DiceRoller as dr



d6 = dr.Die(6)
d12 = dr.Die(12)
d4 = dr.Die(4)
d100 = dr.Die(100)



local_chara = dr.Dicetower(d6)

local_chara.calc_prob_dist()

plt.plot( local_chara.get_prob_dist().keys(), local_chara.get_prob_dist().values() )
plt.ylabel("probabliliy of occurence")
plt.xlabel("sum of diceroll")
plt.show()

# rolls = 1000000
# roll_range = local_chara.diestack.get_max_roll() - local_chara.diestack.get_min_roll()+1
# roll_histogram = [0] * roll_range

# print(local_chara.diestack.get_face_array())


# for roll in range(rolls):
#     roll_histogram[local_chara.diestack.roll() - local_chara.diestack.get_min_roll()] += 1
    

# print(roll_histogram)

# plt.plot( range(local_chara.diestack.get_min_roll(),local_chara.diestack.get_max_roll()+1), roll_histogram)
# plt.ylabel('hits')
# plt.show()
