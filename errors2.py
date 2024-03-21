# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #String declaration is required here for variable "animal"
animal_type = "cub"
number_of_teeth = 16


#instead using full_spec variable, we can simply put it directly in print() function with .format style which prints required values
print('This is a {}. It is a {} and it has {} teeth'.format(animal, animal_type, number_of_teeth)) #print() should be properly used

