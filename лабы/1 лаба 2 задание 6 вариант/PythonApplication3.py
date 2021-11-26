import math

R = float(input())
a = float(input())

Scircle = float()
Ssquare = float()
State = bool()

Scircle = math.pi * (R * R)
Ssquare = a * a

if(Scircle > Ssquare):
    
    print("площадь круга, больше площади квадрата, и равна:", Scircle)
else:
    
    print("площадь квдарата больше площади круга, и равна:", Ssquare)