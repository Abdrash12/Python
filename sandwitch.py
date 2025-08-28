def make_sandwich(bread_type: str, filling: str, cheese: str = "none", toasted: bool = False) -> str:
    """Constructs a descriptive sentence about the sandwich being made.

    Args:
        bread_type (str): Type of bread.
        filling (str): Main sandwich filling.
        cheese (str, optional): Type of cheese. Defaults to "none".
        toasted (bool, optional): Whether the sandwich is toasted. Defaults to False.

    Returns:
        str: A descriptive sentence about the sandwich.
    """
    description = "Making a "

    # Toasted or not
    if toasted:
        description += "toasted "

    description += f"{bread_type} sandwich with {filling}"

    # Cheese check
    if cheese.lower() != "none":
        description += f" and {cheese} cheese"

    description += "."

    return description


# Example usage
print(make_sandwich("wheat", "turkey", "cheddar", True))
print(make_sandwich("rye", "ham"))
