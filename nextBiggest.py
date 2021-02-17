import itertools

"""
Inputs: a number

Purpose: Take in a valid input(number) and return the next largest number. 
         If a number can't be returned,then return -1.
"""

def main():
        while True:
            try: 
                someInt = int(input("Enter your number:"))
            except ValueError:
                print("Not a valid input. Please enter a number.")
            else: 
                break
        num = str(someInt)
        listOfNums = set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])   
        listOfNums = sorted(list(listOfNums))
        try:
                print(listOfNums[listOfNums.index(someInt)+1])
        except Exception:
                print(-1)
main() 
