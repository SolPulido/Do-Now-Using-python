#Sol pulido
#09/19/2023
#___Create a variable that allows the user to enter it's name and output it on the console ____
name=input("Hello , what's your name ? ")
print ("nice to meet you , " + name)
#___Create a variable that allows the user to enter it's favorite animal and output it on the console ____
animal = input( name  + ", Could you tell me your favorite animal:")
print ("Your favorite animal is a " + animal ,"i like more ferrets")
#___Create a variable that allows the user to enter a random number and output it 3 times in the console 
number=input("please enter a number: ")
print ("The number you enter was " + number , number , number  )
#lets the user input 3 numbers in 3 different lines and give them the average of those 3 numbers in the console as an output 
gradeAverage1=int (input("lets calculate the first grade average: "))
gradeAverage2=int (input("enter next grade:"))
gradeAverage3=int (input( "Enter last grade :"))
sumresult = gradeAverage1+ gradeAverage2 + gradeAverage3
average = sumresult/3
print("Your average is "+ str(average))

#Let the user choose 3 words and input them then output them in the console
word1=input("enter a ramdon word : ")
word2=input("enter a ramdon word : ")
word3=input("enter a ramdon word : ")
print(word3 , word2 , word1)

#print a box ask use the number given by the user 

length1 = int(input("Please enter a length of a box : "))
width1 = int(input("please enter a width of a box : "))

area = length1 * width1
print("_________\n|\t\n|\t" + str(width1) + "\n|_________|\n" )