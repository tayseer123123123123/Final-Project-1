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
        if shape == "1":
            sidelength = input('Side Length:')
            area = float(sidelength) * 2
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if (shape == "1"):
                        sidelength = input('Side Length:')
                    area = float(sidelength) * 2
                    print("Area = ", float(area))
                    break
            else:
                exit()

            

        #circle
        if shape == "2":
            radius = input('Radius:')
            area = (float(radius)**2) * float(pi)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "2":
                        radius = input('Radius:')
                    area = (float(radius)**2) * float(pi)
                    print("Area = ", float(area))
                    break
            else:
                exit()

        #triangle
        if shape == "3":
            height_one = input('Height:')
            height_two = input('Base Length:')
            area = (float(height_one) * float(height_two))/2
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "3":
                        height_one = input('Height:')
                        height_two = input('Base Length:')
                    area = (float(height_one) * float(height_two))/2
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #pentagon
        if shape == "4":
            side_one_p = input('Side length:')
            area = ((1/4)* (math.sqrt((5)*((5)+ (2 * math.sqrt(5))))))* (float(side_one_p)**2)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "4":
                        side_one_p = input('Side length:')
                    area = ((1/4)* (math.sqrt((5)*((5)+ (2 * math.sqrt(5))))))* (float(side_one_p)**2)
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #octagon
        if shape == "5":
            side_one_o = input('Side length:')
            area = (2)*((1) + math.sqrt(2)) * (float(side_one_o)**2)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "5":
                        side_one_o = input('Side length:')
                    area = (2)*((1) + math.sqrt(2)) * (float(side_one_o)**2)
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #Rectangle
        if shape == "6":
            lengthr = input('Width:')
            lengthre = input('Length:')
            area = float(lengthr) * float(lengthre)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "6":
                        lengthr = input('Width:')
                        lengthre = input('Length:')
                    area = float(lengthr) * float(lengthre)
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #rhombus
        if shape == "7":
            d1 = input('Diagonal Length 1:')
            d2 = input('Diagonal Length 2:')
            area = (float(d1) * float(d2))/2
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "7":
                        d1 = input('Diagonal Length 1:')
                        d2 = input('Diagonal Length 2:')
                    area = (float(d1) * float(d2))/2
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #Trapezium
        if shape == "8":
            d1 = input('Base:')
            d2 = input('Base 2:')
            h1 = input('Height:')
            area = ((float(d1)+float(d2))/2) * float(h1)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "8":
                        d1 = input('Base:')
                        d2 = input('Base 2:')
                        h1 = input('Height:')
                    area = ((float(d1)+float(d2))/2) * float(h1)
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #kite
        if shape == "9":
            dd1 = input('Diagonal:')
            dd2 = input('Diagonal 2:')
            area = ((float(dd1)*float(dd2))/2)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "9":
                        dd1 = input('Diagonal:')
                        dd2 = input('Diagonal 2:')
                        area = ((float(dd1)*float(dd2))/2)
                    print("Area = ", float(area))
                    break
            else:
                exit()
        #polygons
        if shape == "10":
            num_sides = input('Number of sides :')
            length_sides = input('Length of one side:')
            rc = input('Radius of an inscribed circle:')
            area = (float(num_sides)/2) * float(length_sides) * float(rc)
            print("Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shape == "10":
                        num_sides = input('Number of sides :')
                        length_sides = input('Length of one side:')
                        rc = input('Radius of an inscribed circle:')
                    area = (float(num_sides)/2) * float(length_sides) * float(rc)
                    print("Area = ", float(area))
                    break
            else:
                exit()
    #mode number 2 getting the surface area of a 3d shape
    if mode == "2":
        print('Shape: \n 1. Cylinder \n 2. Sphere \n 3. Cone \n 4. Cuboid \n 5. Tetrahedron \n 6. Cube \n')
        shapes = input('Select shape: ')
            
        if shapes == "1":
            radius = input('Radius:')
            height = input('Height:')
            area = (2 * (float(pi)) * (float(radius)) * float(height)) + (2 * (float(pi)) * (float(radius) **2))
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "1":
                        radius = input('Radius:')
                        height = input('Height:')
                    area = (2 * (float(pi)) * (float(radius)) * float(height)) + (2 * (float(pi)) * (float(radius) **2))
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()

        if shapes == "2":
            radiuss = input('Radius:')
            area = 4 * (float(pi)) * (float(radiuss)**2)
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "2":
                        radiuss = input('Radius:')
                    area = 4 * (float(pi)) * (float(radiuss)**2)
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()

        if shapes == "3":
            radiusccc = input('Radius:')
            heightccc = input('Height:')
            area = (float(pi)*float(radiusccc))*(float(radiusccc)+(math.sqrt((float(heightccc)**2)+float(radiusccc)**2)))
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "3":
                        radiusccc = input('Radius:')
                        heightccc = input('Height:')
                    area = (float(pi)*float(radiusccc))*(float(radiusccc)+(math.sqrt((float(heightccc)**2)+float(radiusccc)**2)))
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()

        if shapes == "4":
            lengthcu = input('Length:')
            widthcu = input('Width:')
            heightcu = input('Height:')
            area = (2*((float(lengthcu))*(float(widthcu))))+(2*((float(lengthcu))*(float(heightcu))))+(2*((float(heightcu))*(float(widthcu))))
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "4":
                        lengthcu = input('Length:')
                        widthcu = input('Width:')
                        heightcu = input('Height:')
                    area = (2*((float(lengthcu))*(float(widthcu))))+(2*((float(lengthcu))*(float(heightcu))))+(2*((float(heightcu))*(float(widthcu))))
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()

#!!!TETRAHEDRON FIX!!!
        if shapes == "5":
            sidet = input('Side Length:')
            area = math.sqrt((3)*(float(sidet)**2))
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "5":
                        sidet = input('Side Length:')
                        area = math.sqrt((3)*(float(sidet)**2))
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()

        if shapes == "6":
            lengthc = input('Length of one side:')
            area = 6 * (float(lengthc)**2)
            print("Surface Area = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapes == "6":
                        lengthc = input('Length of one side:')
                        area = 6 * (float(lengthc)**2)
                    print("Surface Area = ", float(area))
                    break
            else:
                exit()
                

    #mode number 3 getting the volume of a 3d shape
    if mode == "3":
        print('Shape: \n 1. Cylinder \n 2. Sphere \n 3. Tetrahedron \n 4. Cone \n 5. Cuboid \n 6. Pyramid \n 7. Cube \n')
        shapev = input('Select shape: ')

        if shapev == "1":
            radiusv = input('Radius:')
            heightv = input('Height:')
            area = float(pi)*(float(radiusv)**2)*float(heightv)
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "1":
                        radiusv = input('Radius:')
                        heightv = input('Height:')
                    area = float(pi)*(float(radiusv)**2)*float(heightv)
                    print("Volume = ", float(area))
                    break
            else:
                exit()
        
        if shapev == "2":
            radiussp = input('Radius:')
            area = (4/3)*float(pi)*(float(radiussp)**3)
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "2":
                        radiussp = input('Radius:')
                    area = (4/3)*float(pi)*(float(radiussp)**3)
                    print("Volume = ", float(area))
                    break
            else:
                exit()

        if shapev == "3":
            lengthtt = input('Side Length:')
            area = (float(lengthtt)**3)/(6*(math.sqrt(2)))
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "3":
                        lengthtt = input('Side Length:')
                    area = (float(lengthtt)**3)/(6*(math.sqrt(2)))
                    print("Volume = ", float(area))
                    break
            else:
                exit()

        if shapev == "4":
            radiusc = input('Radius:')
            heightc = input('Height:')
            area = float(pi)*(float(radiusc)**2)*((float(heightc))/3)
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "4":
                        radiusc = input('Radius:')
                        heightc = input('Height:')
                    area = float(pi)*(float(radiusc)**2)*((float(heightc))/3)
                    print("Volume = ", float(area))
                    break
            else:
                exit()
            
        if shapev == "5":
            lengthcc = input('Length:')
            widthcc = input('Width:')
            heightcc = input('Height:')
            area = (float(widthcc))*(float(heightcc))*(float(lengthcc))
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "5":
                        lengthcc = input('Length:')
                        widthcc = input('Width:')
                        heightcc = input('Height:')
                    area = (float(widthcc))*(float(heightcc))*(float(lengthcc))
                    print("Volume = ", float(area))
                    break
            else:
                exit()

        if shapev == "6":
            lengthpp = input('Base Length:')
            widthpp = input('Base Width:')
            heightpp = input('Pyramid Height:')
            area = ((float(widthpp))*(float(heightpp))*(float(lengthpp)))/3
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "6":
                        lengthpp = input('Base Length:')
                        widthpp = input('Base Width:')
                        heightpp = input('Pyramid Height:')
                    area = ((float(widthpp))*(float(heightpp))*(float(lengthpp)))/3
                    print("Volume = ", float(area))
                    break
            else:
                exit()

        if shapev == "7":
            lengthccc = input('Side Length:')
            area = float(lengthccc)**3
            print("Volume = ", float(area))
            repeat = input('Would you like to re enter the dimentions? (Yes/No):')
            if repeat == "Yes":
                while True:
                    if shapev == "7":
                        lengthccc = input('Side Length:')
                    area = float(lengthccc)**3
                    print("Volume = ", float(area))
                    print("Volume = ", float(area))
                    break
            else:
                exit()

#calling the function
if __name__ == "__main__":
    main()



