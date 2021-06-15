# Import csv data to a django model
import csv

def import_csv(csv_filename):
    with open(csv_filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ingredient = Ingredient(**row)
            ingredient.save()
            print(ingredient.name)


# import_csv('ingredients.csv')