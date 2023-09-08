import DiceRoller as dr
import itertools

def main():
    pass


main()

# Hello heelo making changes to commit

d6 = dr.die(6)
d12 = dr.die(12)

local_chara = dr.dicetower(d12,d12,d6)

print(local_chara.stack.stddev)
print(local_chara.print_simple_distribution())
print(local_chara.stack.roll())

# changes here and stuff
