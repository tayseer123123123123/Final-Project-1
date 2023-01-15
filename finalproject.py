import sys 
import math

#function
def main():
    pi = 3.14159265359
    print("What would you like to do:")
    print("1: Calculate the Area of a shape.")
    print("2: Calculate the Surface Area of a 3d shape.")
    print("3: Calculate the Volume of a 3d shape.")
    #choosing the mode 
    mode = sys.argv[1]

    #mode number 1 getting the area of a 2d shape
    if mode == "1":
        print('Shapes: \n 1. Square \n 2. Circle \n 3. Triangle \n 4. Pentagon \n 5. Octagon \n 6. Rectangle \n 7. Rhombus \n 8. Trapezium \n 9. Kite \n 10. Polygons \n')
        shape = input('Select shape: ')
    #square
    if (shape == "1"):
        sidelength = input('Side Length:')
        area = float(sidelength) * 2
        print("Area = ", float(area))
    #circle
    if shape == "2":
        radius = input('Radius:')
        area = (float(radius)**2) * float(pi)
        print("Area = ", float(area))
    #triangle
    if shape == "3":
        height_one = input('Height:')
        height_two = input('Base Length:')
        area = (float(height_one) * float(height_two))/2
        print("Area = ", float(area))
    #pentagon
    if shape == "4":
        side_one_p = input('Side length:')
        area = ((1/4)(5(5+2(5**1/2)))*float(side_one_p **2))
        print("Area = ", float(area))
    #octagon
    if shape == "5":
        side_one_o = input('Side length:')
        area = (2(1+((2) math.sqrt(1/2))float(side_one_o))
        print("Area = ", float(area))
    #Rectangle
    #rhombus
    #Trapezium
    #kite
    #polygons

    #mode number 2 getting the surface area of a 3d shape
    if mode == "2":
        print('Cube: \n 1. Cylinder \n 2. Sphere \n 3. Triangular Prism \n 4. Cone \n 5. Cuboid \n 6. Pyramid \n')
        shape = input('Select shape: ')
    

    #mode number 3 getting the volume of a 3d shape
    if mode == "3":
        print('Cube: \n 1. Cylinder \n 2. Sphere \n 3. Triangular Prism \n 4. Cone \n 5. Cuboid \n 6. Pyramid \n')
        shape = input('Select shape: ')

#calling the function
if __name__ == "__main__":
    main()



