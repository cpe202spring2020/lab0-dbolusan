def weight_on_planets():
   # write your code here
   # Takes input as string, cast to float
   val = float(input("What do you weigh on earth? "))
   # Print Statement with formatting, Format statement with
   # Format equations
   # Mars Weight = val * .38
   # Jupiter Weight = val * 2.34

   print("\nOn Mars you would weigh %.2f pounds.\n" \
   		 "On Jupiter you would weigh %.2f pounds." 
   		 % (val * .38, val * 2.34))


if __name__ == '__main__':
   weight_on_planets()
