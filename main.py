import random
import string

#Function Run Quiz


def run_quiz():

  print("\nWelcome, Please Select Quiz Type:")
  print("\n\t1: 1990's")
  print("\n\t2: 2000's")
  print("\n\t3: 2010's")

  choice = 0

  while True:
    try:

      choice = int(input("\n\tInput:"))

      if 0 < choice <= 3:
        break
      else:
        print("\nSorry, Please Try Again")

    except:
      print("\nSorry Invalid Input")

  song_list = []

  match choice:

    case 1:
      song_list = get_data("1990s_songs.txt")

    case 2:
      song_list = get_data("2000s_songs.txt")

    case 3:
      song_list = get_data("2010s_songs.txt")


#We Now Have Clean Data#

  song_list = process_data(song_list)

  #Pick Random Song
  fails = 0
  points = 0
  while fails < 2:

    if fails == 0:
      random_line = random.randint(0, len(song_list) - 1)

      line = song_list[random_line]

    artist, song, prompt = generate_prompt(line, fails)

    print("\nThis Song is by '" + artist + "', What is it Called?\n")
    print(prompt)
    guess = input("\n")

    if guess.lower() == song.lower():
      fails = 0
      points += (10 - (fails * 5))
      print("\nWell Done You Are Correct!")

    elif fails == 0:
      print("\nSorry That's Incorrect, You Have One More Guess!")
      fails += 1

    else:
      print("Sorry Game Over")
      fails += 1

  print("You Scored " + str(points))

  #Adding Points To Scoreboard

  print("Would You Like To Upload Your Points To The Scoreboard?")


def generate_prompt(line, attempt_num):

  line = line.split(',')

  artist = line[0]

  song = line[1]

  #Hyphonating song
  prompt = song
  split_song = song.split(' ')

  i = 0

  while i < len(split_song):
    word = split_song[i]
    i += 1

    j = 0

    latch = False

    while j < len(word):
      letter = word[j]
      j += 1
      #if retunrns not -1
      if string.ascii_uppercase.find(letter) != -1 and attempt_num == 1:
        latch = True
      elif string.ascii_lowercase.find(letter) != -1:
        if latch == False:
          prompt = prompt.replace(letter, "-", 1)
        latch = False

  #remove every lowercase accpet directly after capitals

  #if caps then skip next
  #if not caps continue

  return artist, song, prompt


#Splitting The Line

#A Tribe Called Quest, Can I Kick It?

#C-- I K--- I-?
#
# This Song is by 'A Tribe Called Quest', What is it Called?
#
# answer here


#Function for reading the files and reading them
def get_data(file_name):

  file = open(file_name, 'r')
  data = file.readlines()
  file.close
  return data


#Function Process Data


def process_data(dirty_data):

  i = 0

  while i < len(dirty_data):
    dirty_data[i] = dirty_data[i].strip("\n")
    i += 1

  return dirty_data


run_quiz()

