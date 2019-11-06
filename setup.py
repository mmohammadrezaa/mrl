import sys
class DoAction():
    def __index__(self):
        self.user_input_number = ''

    def user_input(self):
        self.user_input_number = input("SELECT A NUMBER:\n"
                          "1.+\n"
                          "2.-\n"
                          "3.x\n"
                          "4./\n"
                          "5.Area of cycle\n"
                          "6.Circumference\n"
                          "7.Draw foursquare\n")
        try:
            val = int(self.user_input_number)
            if val == 1:
                num1 = int(input("please enter one number...:"))
                num2 = int(input("please enter another number:"))
                self.input_sum(num1,num2)
            elif val == 2:
                num1 = int(input("please enter one number...:"))
                num2 = int(input("please enter another number:"))
                self.input_sub(num1, num2)
            elif val == 3:
                num1 = int(input("please enter one number...:"))
                num2 = int(input("please enter another number:"))
                self.input_multiplication(num1, num2)
            elif val == 4:
                num1 = int(input("please enter one number...:"))
                num2 = int(input("please enter another number:"))
                mood = int(input("SELECT MOOD:\n"
                      "1.integer\n"
                      "2.float\n"))
                if mood > 2 or mood < 1:
                    print("you Enter a incorrect value please try again")
                    self.user_input()
                self.input_division(num1, num2, mood)
            elif val == 5:
                radius = int(input("please enter cycle radius:"))
                self.Area_Of_Cycle(radius)
            elif val == 6:
                radius = int(input("please enter cycle radius:"))
                self.circumference(radius)
            elif val == 7:
                width = int(input("please enter foursquare width:"))
                height = int(input("please enter foursquare height:"))
                mood = int(input("1.fully\n"
                                 "2.empty\n"))
                if mood < 1 or mood > 2:
                    print("you Enter a incorrect value please try again")
                    self.user_input()
                self.draw_foursquare(width, height, mood)
            else:
                print("you Enter a incorrect value please try again\n")
                self.user_input()
        except ValueError:
            print("you Enter a incorrect value please try again")
            self.user_input()

    def input_sum(self,num1 , num2):
        print(num1 + num2)

    def input_sub(self, num1, num2):
        print(num1 - num2)

    def input_multiplication(self, num1, num2):
        print(num1 * num2)

    def input_division(self, num1, num2 , mood):
        if mood == 1:
            result = num1 // num2
        else:
            result = num1 / num2
        print(result)

    def Area_Of_Cycle(self, radius):
        print(3.14 * int(radius)**2)

    def circumference(self, radius):
        print(2 * 3.14 * int(radius))

    def draw_foursquare(self, width, height, mood):
        print(" ")
        if mood == 1:
            for y in range(height):
                print("*"*width)
            print("\n")
        else:
            write = sys.stdout.write
            for y in range(height):
                for x in range(width):
                    if x == 0 or y == 0:
                        write('*')
                    elif x == width-1 or y == height-1:
                        write('*')
                    else:
                        write(" ")

                write('\n')
    def __del__(self):
        print("HAVE YOU ANOTHER WORK?")
        finish = int(input("1.yes\n"
                           "2.no\n"))
        if finish == 1:
            cl = DoAction()
            cl.user_input()
        else:
            print("FINISH\n"
                  "THANKS YOU FOR USED MY APP\n"
                  "//******** CREATED BY MOHAMMADREZA ********//")
            write = sys.stdout.write
            for y in range(10):
                write("             ")
                for x in range(20):
                    if x == 0 or y == 0:
                        write('*')
                    elif x == 19 or y == 9:
                        write('*')
                    elif (x == 7 and y == 3) or (x == 13 and y == 3):
                        write("*")
                    elif (x == 6 and y == 4) or (x == 8 and y == 4) or (x == 12 and y == 4) or (x == 14 and y == 4):
                        write("*")
                    elif (x == 5 and y == 5) or (x == 9 and y == 5) or (x == 11 and y == 5) or (x == 15 and y == 5):
                        write("*")
                    elif (x == 4 and y == 6) or (x == 10 and y == 6) or (x == 16 and y == 6):
                        write("*")
                    else:
                        write(" ")

                write('\n')


cl = DoAction()
cl.user_input()