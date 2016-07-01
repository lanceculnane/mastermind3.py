#This is a rough attempt at making the boardgame "mastermind"
#Enjoy!   programmer = lance culnane
#This is my first program I've made all by myself from scratch 
# beyond the tutorial word-scrambling input-output stuff
#woot!
#after midnight... 07/01/2016
#
#
#
#pseudocode planning:
# print welcome screen with instructions and sample board
# input- ask for first guess with the 6 color options ROYGBW- 
#they guess 4 and they can just type them like this 'YWRO' or 
#drag colors once I have a GUI version
#The program checks their submission to the secret colors 
#the program picks in the beginning and displays black for
# right color-right spot and white for right color and wrong spot
#input- ask for 2nd guess- Guess# +=1- check and give clues and 
#then redraw the whole board so it looks nice with the two 
#submissions and two clues
#at the end of each turn guess # increases, and the program 
#checks to see if it is the correct answer and/or when it 
#displays 4 blacks then a "winner" announcement is given
#

import random


print(

    """
    -----------------------------------------------------------
    Welcome to Mastermind, Fool! Try to break the color code! The code is 4 colors of any combo 
    	  (including repeats) of ROYGBW and I will give you hints along the way. A black is given if 
    	  you got a right color
 		  in the right place and a white is given if you got a correct color
 		    but in the incorrect spot
 		  Type QQQQ to quit at any time
 		  (note: this program crashes if there aren't four characters entered
 		       each time- so be sure to enter four values at all times)
    """    

           ) 

#constants
COLORS = ("R", "O", "Y", "G", "B", "W")
code1 = random.choice(COLORS)
code2 = random.choice(COLORS)
code3 = random.choice(COLORS)
code4 = random.choice(COLORS)
code = code1+code2+code3+code4   #is this a list now or string or what?
     #<-----while I'm testing this, I put "print code" here so
# I know the answer and dont have to figure it out 
#initialize variables
tries = 0      #... keeps track of the # of tries
guess = raw_input('You ready to rock? Type "YYYY"')

#main--- I should really recode all this to be more OOP 
# I could easily make each section a function if I'd like
# like introduction(), guess(), main(), goodbye() or something
while guess != code and guess != "QQQQ" and len(guess) == 4:
	print tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries,tries
	print "Crack my code! Enter four colors (ROYGBW)"
	guess = raw_input("????")


	tries += 1
	bs = 0   #below counts total black: right color in right spot
	if code[0] == guess[0]:
		bs += 1
	if code[1] == guess[1]:
		bs += 1
	if code[2] == guess[2]:
		bs += 1
  	if code[3] == guess[3]:
  		bs += 1

  	ws = 0      #below counts total white: right color and wrong spot
  	if code.count("R") == 1 and guess.count("R") >= 1:
  		ws += 1
  	if code.count("R") == 2 and guess.count("R") >= 2:
  		ws += 2
  	if code.count("R") == 2 and guess.count("R") == 1:
  		ws += 1
  	if code.count("R") == 3 and guess.count("R") >= 3:
  		ws += 3
  	if code.count("R") == 3 and guess.count("R") == 2:
  		ws += 2
  	if code.count("R") == 3 and guess.count("R") == 1:
  		ws += 1

  	if code.count("O") == 1 and guess.count("O") >= 1:
  		ws += 1
  	if code.count("O") == 2 and guess.count("O") >= 2:
  		ws += 2
  	if code.count("O") == 2 and guess.count("O") == 1:
  		ws += 1
  	if code.count("O") == 3 and guess.count("O") >= 3:
  		ws += 3
  	if code.count("O") == 3 and guess.count("O") == 2:
  		ws += 2
  	if code.count("O") == 3 and guess.count("O") == 1:
  		ws += 1

  	if code.count("Y") == 1 and guess.count("Y") >= 1:
  		ws += 1
  	if code.count("Y") == 2 and guess.count("Y") >= 2:
  		ws += 2
  	if code.count("Y") == 2 and guess.count("Y") == 1:
  		ws += 1
  	if code.count("Y") == 3 and guess.count("Y") >= 3:
  		ws += 3
  	if code.count("Y") == 3 and guess.count("Y") == 2:
  		ws += 2
  	if code.count("Y") == 3 and guess.count("Y") == 1:
  		ws += 1

   	if code.count("G") == 1 and guess.count("G") >= 1:
  		ws += 1
  	if code.count("G") == 2 and guess.count("G") >= 2:
  		ws += 2
  	if code.count("G") == 2 and guess.count("G") == 1:
  		ws += 1
  	if code.count("G") == 3 and guess.count("G") >= 3:
  		ws += 3
  	if code.count("G") == 3 and guess.count("G") == 2:
  		ws += 2
  	if code.count("G") == 3 and guess.count("G") == 1:
  		ws += 1

   	if code.count("B") == 1 and guess.count("B") >= 1:
  		ws += 1
  	if code.count("B") == 2 and guess.count("B") >= 2:
  		ws += 2
  	if code.count("B") == 2 and guess.count("B") == 1:
  		ws += 1
  	if code.count("B") == 3 and guess.count("B") >= 3:
  		ws += 3
  	if code.count("B") == 3 and guess.count("B") == 2:
  		ws += 2
  	if code.count("B") == 3 and guess.count("B") == 1:
  		ws += 1

   	if code.count("W") == 1 and guess.count("W") >= 1:
  		ws += 1
  	if code.count("W") == 2 and guess.count("W") >= 2:
  		ws += 2
  	if code.count("W") == 2 and guess.count("W") == 1:
  		ws += 1
  	if code.count("W") == 3 and guess.count("W") >= 3:
  		ws += 3
  	if code.count("W") == 3 and guess.count("W") == 2:
  		ws += 2
  	if code.count("W") == 3 and guess.count("W") == 1:
  		ws += 1

# There was proly an easier way than above... it was a pretty
# tough and fun problem to figure out how to calculate the white #
# I first just wanted to check if code[0] was in guess etc
# but after some paper trials I realized it would double count 
# and mess up. I also thought of loops involving:
# A) after comparing code to guess, popping out or deleting any 
# matches, but I kept getting a string error that I didn't understand
# B) making a dictionary with keys as letters and values 
# as number of counts, but I couldn't figure out that either
# so I ended up just counting it straight-up- it seems a good way to
# do it... there would be a lot of confusing typing either way
# because you don't want to penalize someone who guessed 3 oranges "O"
# and there was only 1 or 2 etc- you cant just not give them a white
# peg, or a white peg count that is inaccurate!

  	wfinal = ws - bs     #I have to subtract it because the white double counted any blacks


	print "look carefully at my hints:"
	if bs == 0 and wfinal == 0:
		print "\t- - - -"
	if bs == 0 and wfinal == 1:
		print "\tW - - -"
	if bs == 0 and wfinal == 2:
		print "\tW W - -"
	if bs == 0 and wfinal == 3:
		print "\tW W W -"
	if bs == 0 and wfinal == 4:
		print "\tW W W W"
	if bs == 1 and wfinal == 0:
		print "\tB - - -"
	if bs == 1 and wfinal == 1:
		print "\tB W - -"
	if bs == 1 and wfinal == 2:
		print "\tB W W -"
	if bs == 1 and wfinal == 3:
		print "\tB W W W"
	if bs == 2 and wfinal == 0:
		print "\tB B - -"
	if bs == 2 and wfinal == 1:
		print "\tB B W -"
	if bs == 2 and wfinal == 2:
		print "\tB B W W"
	if bs == 3 and wfinal == 0:
		print "\tB B B -"
	if bs == 3 and wfinal == 1:
		print "\tB B B W"
	if bs == 4:
		print "\tB B B B"
	
# theres probably a sexy 'for' and 'in' loop-type way to do the above
# printout, but it didnt take long. Also this way I can add
# smartass quotes later if I want, like "W - - - only 1 right color
# ?! You gotta be kidding me? Are you trying to fail? buhuhaha!"

if len(guess) != 4 :
	print "Sorry man- fatal error. You have to start over if you"
	print " don't put in FOUR CHARACTERS. I could fix it so that"
	print " you don't lose your game... but that would take effort"
	print " ...kinda like how following directions takes effort"
if guess == code:
	print "You got it!" 
print "The answer was: ", code 
print   "It only took you ", tries; print " tries."
print "My creator, Lance, usually does it in 6 tries or less."
print "I've heard that anything <10 is considered pretty good."
if guess == "QQQQ":
	print "Goodbye- better luck next time, although I don't believe in luck because I'm a computer"


         

#end program
raw_input("press the enter key to exit")







