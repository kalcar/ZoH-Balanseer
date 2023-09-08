import DiceRoller as dr
import itertools

def main():
    pass


main()
 # look changes

def myfunc2(var):
    return 20
# create a conflict 


 # hello code here
def myfunc():
    return 12

d6 = dr.die(6)
d12 = dr.die(12)

local_chara = dr.dicetower(d12,d12,d6)

print(local_chara.stack.stddev)
print(local_chara.print_simple_distribution())
print(local_chara.stack.roll())

