class Car:
    """
    A class representing a car with basic attributes and behavior.
    """

    def __init__(self, brand, model, year, color, horse_power,):
        """
        Initialize a new Car instance.

        Args:
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (int): The production year of the car.
            color (str): The color of the car.
            horse_power (int): The horsepower of the car.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.horse_power = horse_power

    # --- Properties (Getters) ---

    @property
    def brand(self):
        """Return the car's brand."""
        return self.brand

    @property
    def model(self):
        """Return the car's model."""
        return self.model

    @property
    def year(self):
        """Return the car's production year."""
        return self.year

    @property
    def color(self):
        """Return the car's color."""
        return self.color

    @property
    def horse_power(self):
        """Return the car's horsepower."""
        return self.horse_power
    # --- Behavior Methods ---

    def change_color(self, new_color):
        """
        Change the car's color if it's different from the current one.

        Args:
            new_color (str): The new color to apply.

        Returns:
            bool: True if the color was changed, False otherwise.
        """
        if self.color != new_color:
            self.color = new_color
            return True
        return False

    def increase_horse_power(self, additional_hp):
        """
        Increase the car's horsepower by a positive amount.

        Args:
            additional_hp (int): The amount of horsepower to add.

        Returns:
            bool: True if horsepower was increased, False if the input was invalid.
        """
        if additional_hp > 0:
            self.horse_power += additional_hp
            return True
        return False
