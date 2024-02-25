#print outputs a string
print("Welcome to my computer quiz!")

#below takes the input that the user inputs after the below statement
playing = input("Do you want to play? (yes/no) ")

#this checks if they said yes or no.
#we change to is lower so we can accept all inputs, inlcuding yes,Yes,yES and so on.
if playing.lower() != "yes":

    #this line is indented because it is within the statement above, from the if statement. 
    #use tabs for this indentation.
    quit()

#this line has no indentation because we are outside the if statement.
print("Okay! Let's play :)")

#this makes an integer to score the total score.
score = 0



##################################################################################################
##          BELOW IS THE COMPONENTS OF ONE QUESTION                                             ##
##################################################################################################
answer1 = input("What does CPU stand for? ")

if answer1.lower() == "central processing unit":
    #single and double quotes are interchangeable in python. THIS IS NOT TRUE FOR OTHER LANGUAGES
    print('Correct!')
    #this adds one point to the score
    score = score + 1

#else statement runs if the ifstatement is not true.
else:
    print('Incorrect.')
##################################################################################################
    
answer2 = input("What does PSU stand for? ")

if answer2.lower() == "power supply unit":
    #single and double quotes are interchangeable in python. THIS IS NOT TRUE FOR OTHER LANGUAGES
    print('Correct!')
    #this adds one point to the score
    score = score + 1

#else statement runs if the ifstatement is not true.
else:
    print('Incorrect.')



#this ends the program and prints the score.
    
#the f below turns it into a f-string. This allows you to add data inside.
# these can include python expressions in curly braces as shown below.
    # the .str() changes it to a string. It is currently an integer and cannot be [printed]
scorestr = str(score)
print(f"You scored  {scorestr}/2!")