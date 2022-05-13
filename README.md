# bai-tap-buoi-2
# Bài 1:
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y  = y
        
        
    def __str__(self):
        return f"{self.x}/{self.y}"
    
    def __add__(self, other):  
        import math
        x = math.sqrt((self.x - other.x) ** 2) 
        y = math.sqrt((self.y - other.y) ** 2)
   
    def __add__(self, other):
        x = (self.x + other.x) 
        y = (self.y  + other.y)

    def __sub__(self, other):
        x = (self.x - other.x) 
        y = (self.y  - other.y)
A  = Point2D(1,2)
B  = Point2D(2,4)
khoangcach  = A + B
tong  = A + B
hieu  = A - B

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y  = y
        self.z  = z
        
    def __str__(self):
        return f"{self.x}/{self.y}/{self.z}"

    def __add__(self, other):  
        import math
        x = math.sqrt((self.x - other.x) ** 2) 
        y = math.sqrt((self.y - other.y) ** 2)
        z = math.sqrtt((self.z - other.z) ** 2)

    def __add__(self, other):
        x = (self.x + other.x) 
        y = (self.y  + other.y)
        z = (self.z + other.z)

    def __sub__(self, other):
        x = (self.x - other.x) 
        y = (self.y  - other.y)
        z = (self.z - other.z)
X = Point3D(1,2,3)            
Y  = Point3D(3,4,5)
khoangcach = X + Y
tong  = X + Y
hieu  = X - Y
    
#Bài 2:
class  Warehouse:
    def __init__(self, _listitem, key, value):
        key = self.key
        value = self.value

    def getAllValues(self): 
        value = self.value[0] + self.value[99]
    
    def  addItem(self, name, value):
        name = self +   self.name
        value  = self.value  + 1

    def  removeItem(self, name, value):
        name = self - self.name
        value  = self.value  - 1
