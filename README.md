# Final-Project-1

In the README file for your project, use Markdown to include all of the following information:

* A video of your program running (1min or less, no voiceover)

* Summarize program's functionality (what does it do?) and purpose (why does it exist and/or who is it for?)

My program has three modes, first mode is to calculate area, second mode is to calculate surface area, and third mode is to calculate volume. Each of these modes has 5-10 shapes that you can choose from and then you can input your dimensions and get the output. After you get your output the program will ask you if you want to enter new dimensions and if you do you can say Yes and it will give you one more time to input the dimensions but if you say No it will exit the program. This is for students mainly or engerneers so that instead of heaving to lookup each formula they can have them all in one place for them. People can use this for many diffrent things starting at homework/assignments, to building a house.

* A description, with code segments, of a "breakthrough moment" in which you solved a particularly difficult problem, learned to do something new, or independently overcame being stuck

Throughout my code I had to use many diffrent equations to calculate the volume, area, and surface area. One thing that I was challenged with at first is doing exponents and square roots. 

import math
area = ((1/4)* (math.sqrt((5)*((5)+ (2 * math.sqrt(5))))))* (float(side_one_p)**2)

As you can see in the code segments above I imported math to be able to get the square root of 5 and I also used **2 to make the float have an exponenet of two.



* An explanation of data abstraction as it is used in your program.
- Include code segments that show where data is being stored and where data is being retrived and accompanying explanation.

if shape == "1":
        sidelength = input('Side Length:')
        area = float(sidelength) * 2
        print("Area = ", float(area))
This code segment above shows the user inputting information and it being outputed with the area.
        
mode = sys.argv[1]

Also you can see data abstraction being used with the command line argument above to choose the mode.

- Identify what the abstracted data represents in your program

In my program the abstracted data represents firsly the initial mode that the user will be using and secondly the input and output of the shapes and there volumes, areas, and surface areas.

- Explain how the selected abstraction manages complexity in your program code (why your program code could not be written, or how it would be written differently, if you did not abstract the data in the way you did)

* An explanation of procedural abstraction as it is used in your program.

Procedural abstraction is used in my program to make seperate functions for each of the diffrent modes.

if mode == "1":
        print('Shapes: \n 1. Square \n 2. Circle \n 3. Triangle \n 4. Pentagon \n 5. Octagon \n 6. Rectangle \n 7. Rhombus \n 8. Trapezium \n 9. Kite \n 10. Polygons \n')
        shape = input('Select shape: ')
        area(shape)

    if mode == "2":
            print('Shape: \n 1. Cylinder \n 2. Sphere \n 3. Cone \n 4. Cuboid \n 5. Tetrahedron \n 6. Cube \n')
            shapes = input('Select shape: ')        
            surface_area(shapes)
    if mode == "3":
        print('Shape: \n 1. Cylinder \n 2. Sphere \n 3. Tetrahedron \n 4. Cone \n 5. Cuboid \n 6. Pyramid \n 7. Cube \n')
        shapev = input('Select shape: ')
        volume(shapev)
    
def area(shape):
    
    if shape == "1":
        sidelength = input('Side Length:')
        area = float(sidelength) * 2
        print("Area = ", float(area))
        #asking user if he wants to reenter dimentions
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

- Explain how the algorithm in the above code segment functions and why it is important for the purpose of your program

This algorithm functions by first taking the mode from the command line argument, then it gives the user choices of the diffrent shapes, then after the user inputes the shape it runs the seperate function for the mode using paramaters. This helps the program run more efficiently.

- Explain how the procedural abstraction helps to manage complexity in your program (be specific!)

Procedural abstraction helps to manage complecity in my program because you can easily change something inside a function or delete a function.


