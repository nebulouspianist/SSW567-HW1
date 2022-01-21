
import unittest


list = []

# test command

def TypeOfTriangle(a,b,c):
    list = [a,b,c]

    list.sort()

    if(list[0] + list[1] <= list[2]):
        return "not a triangle"

    if(list[0]==list[1] and list[1]==list[2]):
        return "equilateral"

    elif list[0]==list[1] or list[1]==list[2]:
        return "isosceles"

    elif list[0]**2 + list[1]**2 == list[2]**2:
        return "right"

    else:
        return "scalene"



class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual("right", TypeOfTriangle(3,4,5))
        self.assertEqual("equilateral", TypeOfTriangle(1,1,1))
        self.assertEqual("isosceles", TypeOfTriangle(3,5,3))
        self.assertEqual("scalene",TypeOfTriangle(7,6,5))

    def test2(self):
        self.assertEqual("not a triangle", TypeOfTriangle(9,1,1))
        self.assertEqual("not a triangle",TypeOfTriangle(-1,0,0))
    
    




if __name__ == "__main__":

    unittest.main()

    


    