import sys 
#function
def main():
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
    if shape == "1":
        sidelength = input('Side Length:')
        area = int(sidelength) * 2
        print("Area = ", int(area))

        

#calling the function
if __name__ == "__main__":
    main()



