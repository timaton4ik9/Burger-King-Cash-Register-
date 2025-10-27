print("Добро пожаловать в Бургер Кинг") # by timaton4ik9
# print("Бургеры (Говядина)")
costWhopperJulien = 4.32
costSpicyWhopperJulien = 4.45
costWhopperandCheeseburgerandDrinkandFries = 7.41
costXXLChiliСheeseSauce = 1.36
# costAnguswithChanterelles = 6.79
# costSpicyAnguswithChanterelles = 6.92
quantityWhopperJulien = int(input("Введите количество [Воппер Жюльен]:"))
quantitySpicyWhopperJulien = int(input("Введите количество [Острый Воппер Жюльен]:"))
quantityWhopperandCheeseburgerandDrinkandFries = int(input("Введите количество [Воппер + Чизбургер + Напиток + Картофель]:"))
quantityXXLChiliСheeseSauce = int(input("Введите количество [XXL соус Чили Чиз]:"))
# quanityAnguswithChanterelles = int(input("Введите количество [Ангус с Лисичками]:"))
# quanitySpicyAnguswithChanterelles = int(input("Введите количество [Острый Ангус с Лисичками]:"))
total = costWhopperJulien * quantityWhopperJulien + costSpicyWhopperJulien * quantitySpicyWhopperJulien + costWhopperandCheeseburgerandDrinkandFries * quantityWhopperandCheeseburgerandDrinkandFries + costXXLChiliСheeseSauce * quantityXXLChiliСheeseSauce
print("С вас", total, "$")
