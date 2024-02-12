import matplotlib.pyplot as plt
import DiceRoller as dr



d6 = dr.die(6)
d12 = dr.die(12)
d4 = dr.die(4)
d100 = dr.die(100)


local_chara = dr.dicetower(d12,d12,d100,d4)
rolls = 1000000
roll_range = local_chara.stack.get_max_roll() - local_chara.stack.get_min_roll()+1
roll_histogram = [0] * roll_range

print(local_chara.stack.get_face_array())


for roll in range(rolls):
    roll_histogram[local_chara.stack.roll() - local_chara.stack.get_min_roll()] += 1
    

print(roll_histogram)

plt.plot( range(local_chara.stack.get_min_roll(),local_chara.stack.get_max_roll()+1), roll_histogram)
plt.ylabel('hits')
plt.show()
