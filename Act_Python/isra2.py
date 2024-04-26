class Point:
    name: str = "Clase Punto"
    def __init__(self ,x:int, y:int) -> None:
        self.x = x
        self.y = y

class Point3D(Point):
    def __init__(self,x:int, y:int, z:int) -> None:
        self.z = z
        super().__init__(x,y)

if __name__ == "__main__":
    point = Point(2,3)
    point2 = Point3D(1,2,3)