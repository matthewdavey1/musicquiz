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

  random_line = random.randint(0, len(song_list) - 1)

  line = song_list[random_line]

  line = line.split(',')

  artist = line[0]

  song = line[1]

  #Hyphonating song

  song = song.split(' ')

  i = 0

  while i < len(song):
    word = song[i]
    i += 1

    j = 0

    while j < len(word):
      letter = word[j]
      j += 1
      print(letter)


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
