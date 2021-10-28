# inheritance

from chef import Chef
from chineseChef import ChineseChef

myChef = Chef()

myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()

ChineseChef = ChineseChef()

ChineseChef.make_chicken()
ChineseChef.make_fried_rice()
ChineseChef.make_special_dish()

# ... end
