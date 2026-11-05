
def count_occurrences(target, values):
    if len(values) == 0:
        return 0
    firstValue =values[0]
    restValue = values[1:]
    countValues = count_occurrences(target,  restValue)

    if firstValue == target:
        return countValues + 1

    return countValues



def is_sorted(values):
    if len(values) <=1:
        return True
    firstValue = values[0]
    secondValue = values[1]
    if firstValue > secondValue:
        return False
    restOfValue = values[1:]
    return is_sorted(restOfValue)

    


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def area(self):
        return self.width * self.height
        

    def perimeter(self):
        return 2 * (self.width + self.height)
        
        pass

    def __str__(self):
        return f"{self.width}x{self.height}"


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        super().__init__(side,side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    # print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    # print(is_sorted([1, 2, 3]))                    # True
    # print(Rectangle(3, 4).area())                  # 12
    # print(Square(5))                               # 5x5
    pass


if __name__ == "__main__":
    main()
