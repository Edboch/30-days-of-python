import random
import string

def random_user_id():
    id = ''
    for i in range(6):
        id += random.choice(string.ascii_letters+string.digits)
    return id

print(random_user_id())

def user_id_gen_by_user():
    idlength, numtogenerate = input('User input: ').split()
    ids = []
    for x in range(int(numtogenerate)):
        id = ''
        for y in range(int(idlength)):
            id+= random.choice(string.ascii_letters+string.digits)
        ids.append(id)
    return ids
#print(user_id_gen_by_user())

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return 'rgb({},{},{})'.format(r,g,b)

print(rgb_color_gen())


def list_of_hexa_colors(index = 5):
    hexchar = 'abcdef'+string.digits
    colors = []
    for i in range(index):
        color = '#' + ''.join([random.choice(hexchar) for x in range(6)])
        colors.append( color)
    print((colors))
list_of_hexa_colors()

def list_of_rbg_colors(index = 5):
    colors = []
    for i in range(index):
        colors.append(rgb_color_gen())
    print(colors)
list_of_rbg_colors()

def generate_colors(unit, quantity):
    if unit == 'hexa':
        list_of_hexa_colors(quantity)
    else:
        list_of_rbg_colors(quantity)

generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 

example = [1,2,3,4,5,6,7,8,9]
def shuffle_list(l):
    return random.sample(l, k=len(l))
print(shuffle_list(example))

def random_seven():
    digits = ['0','1','2','3','4','5','6','7','8','9']
    number = ''
    for i in range(7):
        chosen = random.choice(digits)
        digits.remove(chosen)
        number+=chosen
    return number
print(random_seven())