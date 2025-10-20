import numpy as np
#Filtering = Refers to the process of selecting elements
#          = from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                [39,22,15,99,18,19,21,20]])


teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]

adults2 = np.where(ages >= 18, ages, 0)


print("ages :")
print(ages) 
print("teenagers: ")
print(teenagers)
print("adults:")
print(adults)
print("seniors:")
print(seniors)
print("evens:")
print(evens)

print("keeping the shape:")
print(adults2)

