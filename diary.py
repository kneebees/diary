##Diary
from os import system, name

numsDay = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
numsMonth = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

def clear(): 
  if name == 'nt': 
      _ = system('cls') 
  else: 
      _ = system('clear')

def intro():
  print("Welcome to your diary. Here, you can write diary entries for whatever day is. If you want to read a diary entry for a certain day, you can put in the date and find your entry for the day.")

def monthask():
  while True:
    month = input("What is the number of the month? ")
    if month in numsMonth:
      break
    else:
      try:
        if len(month) != 2:
          print("Write a 2 digit number to represent the month. If it is a single digit number, put a 0 in front of the number.")
        elif int(month) > 12:
          print("Your number is not a month. Try again.")
      except:
        print("Type a number.")
  return str(month)

def dayask():
  while True:
    day = input("What's the number of the day (e.g. 01)? ")
    if day in numsDay:
      break
    try:
      if len(day) != 2:
        print("Write a 2 digit number to represent the day. If it is a single digit number, put a 0 in front of the number.")
      elif int(day) > 31:
        print("Your number is not a day. Try again.")
    except:
      print('Write a number.')
  return str(day)

def yearask():
  while True:
    try:
      year = int(input("What is the number of the year? "))
      break
    except:
      print('Write a number.')
  return str(year)

def nameOfFile():
  user = input("What's your name? ").capitalize()
  month = monthask()
  day = dayask()
  year = yearask()
  fileName = user + '-' + day + '-' + month + '-' + year + '.txt'
  return fileName

def writeEntry(fileName):
  diaryEntry = open(fileName, 'w')
  clear()
  startWriting = input("\nYour entry: \n\n")
  diaryEntry.write(startWriting)
  diaryEntry.close()

def readEntry(fileName):
  diaryRead = open(fileName, 'r')
  clear()
  i = diaryRead.read()
  print(i)
  diaryRead.close()

def diary():
  intro()
  try:
    readOrWrite = input("\nWould your like to read or write a diary entry? ").lower()
    if readOrWrite == 'r' or readOrWrite == 'read':
      readEntry(fileName = nameOfFile())
    elif readOrWrite == 'w' or readOrWrite == 'write':
      writeEntry(fileName = nameOfFile())
  except:
    clear()
    print("Your diary entry was not found. ")

diary()
