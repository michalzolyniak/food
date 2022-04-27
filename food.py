class Ingredient:
    """
    Ingredients of meal.
    :param str name: ingredient name
    :param int proteins: the amount of protein in the ingredient
    :param int carbohydrates: the amount of carbohydrates in the ingredient
    :param int fat: the amount of fat in the ingredient
    """
    def __init__(self, name, proteins, carbohydrates, fat):
        self.name = name
        self.proteins = proteins
        self.carbohydrates = carbohydrates
        self.fat = fat
        self.calories = proteins * 4 + carbohydrates * 4 + fat * 9.4

    def __repr__(self):
        return f"{self.name} (protein {self.proteins}g carbohydrates {self.carbohydrates}g " \
               f"fat {self.fat}g {self.calories} calories)"


class Meal:
    """
    Meal consisting of ingredients.
    :param str meal_name: meal name
    """
    def __init__(self, meal_name):
        self.meal_name = meal_name
        self.ingredient = []

    def ingredients(self, name, proteins, carbohydrates, fat):
        """
        Adding ingredients to the meal.
        :param str name: ingredient name
        :param int proteins: the amount of protein in the ingredient
        :param int carbohydrates: the amount of carbohydrates in the ingredient
        :param int fat: the amount of fat in the ingredient
        """
        self.ingredient.append(Ingredient(name, proteins, carbohydrates, fat))

    def __repr__(self):
        return f"{self.meal_name}"


class DaySchedule:
    """
    Day schedule consisting of meals.
    :param list meals: meals
    """
    def __init__(self):
        self.meals = []

    def add_meal(self, meal):
        """
        Adding meal to the day schedule.
        :param class meal: meal class
        """
        self.meals.append(meal)

    def print_schedule(self):
        """
        Printing schedule.
        """
        meals_fat = 0
        meals_prot = 0
        meals_car = 0
        meals_cal = 0
        for meal in self.meals:
            meal_fat = 0
            meal_prot = 0
            meal_car = 0
            meal_cal = 0
            print(f"Meal: {meal}")
            for ingredient in meal.ingredient:
                meal_prot += ingredient.proteins
                meal_car += ingredient.carbohydrates
                meal_fat += ingredient.fat
                meal_cal += ingredient.calories
                print(f" {ingredient}")
            print(f"Sum: {meal_prot}g proteins {meal_car}g carbohydrates {meal_fat}g fat {meal_cal} calories")
            meals_prot += meal_prot
            meals_car += meal_car
            meals_fat += meal_fat
            meals_cal += meal_cal
        print(f"Sum of all meals: {meals_prot}g proteins {meals_car}g carbohydrates "
              f"{meals_fat}g fat {meals_cal} calories")


if __name__ == '__main__':

    scrambled_eggs = Meal("scrambled eggs")
    scrambled_eggs.ingredients("200g butter", 100, 40, 30)
    scrambled_eggs.ingredients("2 eggs", 1, 1, 1)

    pizza = Meal("pizza")
    pizza.ingredients("100ml water", 0, 0, 0)
    pizza.ingredients("1kg tomatoes", 100, 200, 100)
    pizza.ingredients("200g cheese", 100, 100, 100)
    pizza.ingredients("300g flour", 200, 200, 300)

    Economic = DaySchedule()
    Economic.add_meal(scrambled_eggs)
    Economic.add_meal(pizza)
    Economic.print_schedule()
