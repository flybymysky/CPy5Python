#Name: TOP 2 SCORER'S NAME AND SCORE EXTRACTHOR.
#Author: Ng Yi Jun Alan (NALA)
#Created: 2/5/2013
#Modified: 2/5/2013
#Description: Find top 2 highest scorers' name & score from list of students & their scores.

print("Welcome to the Fahrenheit to Celcius CONVERTER! :D")
print()

#Collate list of students and their scores
number = input("no. of students:")
totalscore = input("total score of test in 3 digits(i.e.098,005,100):")
print()

name = []
score = []

while len(score)<= int(number)-1:
    name.append(input("NAME of student:"))
    score.append(input("SCORE in 3 digits(i.e.098,005,100):"))
    print()

#Extract Top 2 highest scorers' name & score
TopScorePlacing = score.index(max(score))
TopStudent = name[TopScorePlacing]
TopScore= max(score)

name.remove(TopStudent)
score.remove(TopScore)

SecondTopScorePlacing = score.index(max(score))
SecondTopStudent = name[SecondTopScorePlacing]
SecondTopScore= max(score)

#Print Top 2 highest scorers' name & score
print()
print("Highest Scorer:", TopStudent,",", TopScore+"/"+totalscore)
print("Second Highest:", SecondTopStudent,",", SecondTopScore+"/"+totalscore)

print()
input("press enter to exit.")