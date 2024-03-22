# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #print method must be declared like print("Welcome to the error program")
print("\n") #print() method should be properly used and must be properly indented with the whole program

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #indentation corrected and '==' cannot be used here since there's no IF-Else being used only assignment is here, years old needs to be removed as "24" will be converted to an int
age = int(age_Str) 
print("I'm " + str(age) + " years old.") #needed to convert age back to str here

    # Variables declaring additional years and printing the total years of age
years_from_now = 3 #indentation corrected and '3' should be an int here as in next line '+' operator has been used to add up the years
total_years = int(age) + years_from_now #indentation corrected

print("The total number of years:" + str(total_years)) #print() method should be correctly used, total_years variable should be used here instead of answer_years string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12 ) + 6 #total_years should be used instead of total as it's undefined, 6 is added because of six months as per the statement below and 12 deals with the years
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #print() method should be properly used

#HINT, 330 months is the correct answer

