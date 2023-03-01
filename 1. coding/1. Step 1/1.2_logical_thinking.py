
import string
class Patterns:
    
    
    def pattern_1(self, n):
        for row in range(n):
            for col in range(n):
                print("*", end="")
            print()
            
    def pattern_2(self, n):
        for row in range(n):
            for col in range(row+1):
                print("*", end="")
            print()
            
    def pattern_3(self, n):
        for row in range(n):
            for col in range(row+1):
                print(col+1, end="")
            print()

    def pattern_4(self, n):
        for row in range(n):
            for col in range(row+1):
                print(row+1, end="")
            print()
    
    def pattern_5(self, n):
        for row in range(n):
            for col in range(n-row):
                print("*", end="")
            print()
            
    def pattern_6(self, n):
        for row in range(n):
            for col in range(n-row):
                print(col+1, end="")
            print()
            
    def pattern_7(self, n):
        
        for row in range(n):
            for col in range(n-row-1):
                print(" ", end="")
                
            for col in range(2*row + 1):
                print("*", end="")
            
            for col in range(n-row-1):
                print(" ", end="")
            print()
            
    def pattern_8(self, n):
        
        for row in range(n):
            for col in range(row):
                print(" ", end="")
                
            for col in range(2*n - (2*row+1)):
                print("*", end="")
                
            for col in range(row):
                print(" ", end="")
            print()
            
    def pattern_9(self, n):
        self.pattern_6(n)
        self.pattern_7(n)
        
    def pattern_10(self, n):
        for row in range(2*n - 1):
            if row < 5:
                for col in range(row+1):
                    print("*", end="")
            else:
                for col in range(2*n - row - 1):
                    print("*", end="")
            print("")
            
    def pattern_11(self, n):
        for row in range(n):
            for col in range(row+1):
                if (row+1)%2 != 0:
                    if (col+1) % 2 != 0:
                        print("1 ", end="")
                    else:
                        print("0 ", end="")
                else:
                    if (col+1) % 2 != 0:
                        print("0 ", end="")
                    else:
                        print("1 ", end="")
            print()
        
    def pattern_12(self, n):
        for row in range(n-1):
            for col in range(row+1):
                print(col+1, end="")
            
            for col in range(2 * (n - 1) - 2 * (row + 1)):
                print(" ", end="")
            
            for col in range(row+1, 0, -1):
                print(col, end="")
            
            print()
            
    def pattern_13(self, n):
        num = 0
        for row in range(n):
            for col in range(row+1):
                num += 1
                print(f'{num} ', end="")
            print()
            
    def pattern_14(self, n):
        for row in range(1, n+1):
            print(string.ascii_uppercase[0:row])
            
    def pattern_15(self, n):
        for row in range(1, n+1):
            print(string.ascii_uppercase[0: n + 1 - row])
                
    def pattern_16(self, n):
        for row in range(1, n+1):
            for col in range(row):
                print(string.ascii_uppercase[row-1], end="")
            print()
            
    def pattern_17(self, n):
        for row in range(1, n+1):
            for col in range(n - row):
                print(" ", end="")
            for col in range(row):
                print(string.ascii_uppercase[col], end="")
            for col in range(row-1, 0, -1):
                print(string.ascii_uppercase[col-1], end="")
            for col in range(n - row):
                print(" ", end="")
            print()
        
    def pattern_18(self, n):
        for row in range(1, n+1):
            print(string.ascii_uppercase[n - row])


pattern = Patterns()
pattern.pattern_17(4)