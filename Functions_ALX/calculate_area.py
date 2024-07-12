def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    area = length * width
    return area
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = calculate_area(length, width)
print(area)