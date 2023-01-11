import sys 

#function
def main():
    pi = 3.14159265359
    print("What would you like to do:")
    print("1: Calculate the Area of a shape.")
    print("2: Calculate the Surface Area of a 3d shape.")
    print("3: Calculate the Volume of a 3d shape.")
    mode = sys.argv[1]
#choosing the mode 
    if mode == "1":
        print('Shapes: \n 1. Square \n 2. Circle \n 3. Triangle \n 4. Pentagon \n 5. Octagon \n 6. Rectangle \n 7. Rhombus \n 8. Trapezium \n 9. Kite \n 10. Polygons \n')
        shape = input('Select shape: ')
    
    
    #square
    if (shape == "1"):
        sidelength = input('Side Length:')
        area = float(sidelength) * 2
        print("Area = ", float(area))

    if shape == "2":
        radius = input('Radius:')
        area = (float(radius)**2) * float(pi)
        print("Area = ", float(area))

    if shape == "3":
        height_one = input('Height:')
        height_two = input('Base Length:')
        area = (float(height_one) * float(height_two))/2
        print("Area = ", float(area))
#1 45(5+25)a2
    if shape == "4":
        side_one_p = input('Side length:')
        area = ((1/4)(5(5+2(5**1/2)))*float(side_one_p **2))
        print("Area = ", float(area))

        

#calling the function
if __name__ == "__main__":
    main()



