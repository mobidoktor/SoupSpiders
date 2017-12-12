from bs4 import BeautifulSoup
import urllib.request

url = "http://codeschool.com/users/"

for user in range(2017, 4000000):
  url = url + str(user)
  page = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(page)
  names = soup.find('h1').contents 
  
  for listItem in soup.findAll('li', class_='list-item'):
    if listItem.decode_contents(formatter="html").find('Levels Completed') != -1:
        levels = (listItem.find('strong').contents)        
  
  if levels != []:
    level = levels[0]
    levelString = str(level)
    levelInt = int(levelString)
  else:
    levelString = "No information"
    levelInt = 0

  if names != []:
    name = names[0]
    nameString = str(name)
  else:
    nameString = "No Name Given"

  if (nameString.find("404") != 0):
    if levelInt <= 100:
      print(url) 
      print(nameString)
      print(levelString)  

    if levelInt > 100:
      writeString = "User: " + url + "\nName: " + nameString + "\nLevels Complete: " + levelString + "\n"
      print(writeString)   
      f = open("profile.txt", "a")
      f.write(writeString)
      f.close()
