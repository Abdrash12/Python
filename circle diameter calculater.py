
def calculate_diameter_circle(radius: float)-> float: 
    """
    The diameter of a circle is calculated through this function
    Formula:
    Diameter = radius * 2
    Parameters:
    radius (float): The radius of the circle
    Returns:
    float: The diameter of the circle
    """
    diameter = radius*2
    if radius<0:
        return -1
    return diameter
radius_input = float(input("Enter the radius of the circle: "))
print(calculate_diameter_circle"The diameter of the circle is: "(radius_input))