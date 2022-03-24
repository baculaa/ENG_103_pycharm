## AUTHOR: Alexandra Bacula
## FOR ENG 103 Studio 1

def print_hi(name):
    # This function will print the following text and replace {name} with the value of the name variable
    print(f'Hi, I am {name}')

def print_animal(animal):
    # This function will print the following text and replace {animal} with the value of the animal variable
    print(f'My favorite animals are {animal}')

def print_goals(my_goals):
    # This function will print the following text and replace {my_goals} with the value of the my_goals variable
    print(f'My goals for this class are {my_goals}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Change your variable values here, be sure to leave the quotation marks

    # PUT YOUR NAME HERE
    name = 'Alexandra'

    # PUT YOUR FAVORITE ANIMAL HERE
    animal = 'cats'

    # PUT YOUR GOALS FOR THE CLASS HERE
    my_goals = 'to help you all learn python and have fun creating cool visualizations and art along the way.'

    # Call the functions to print your answers
    print_hi(name)
    print_animal(animal)
    print_goals(my_goals)