# list of variables to be intitialized to hold important info

loggedIn = False

# this is the parent class, which holds guests and registered users
class User:
  def __init__(self, name):
    self.name = name,
    self.balance = 0,    

  # classmethods for User parent class

  # users need to deposit
  # users need to withdraw
  # users only get to play with 1 deck
  # users need to be able to hit, stand, split, and double down


class RegUser(User):
  def __init__(self, name, password):
    super().__init__(name)
    self.password = password,
  

    # classmethods for registered users
    # needs a login option
  def loginRUser(self, password):
    print(self.password, password, type(self.password), type(password))
    if str(self.password) != password:
      print('incorrect username/password, please try again')
      return False
    else:
      print('Welcome to the Casino! ', self.name)
      return True
    
    
    # registered users should have access to everything in the parent class
    # registered users need to have an option for a loan
    # registered users should be able to deposit crypto here (we will make a conversion rate that is similar to the current conversions)
    # registered users should be able to select number of decks


  



def homepage_menu():
  print(' this is the menu')

def register():
  name = input('Please enter a UserName: ')
  password = input('Please enter your password: ')
  user = RegUser(name, password)
  return user

def login(curUser, loggedIn):
  print(curUser, curUser.name, curUser.password)
  username = input('Please enter your Username: ')
  password = input('Please enter your Password: ')
  if curUser.loginRUser(password):
    loggedIn = True
  else: 
    loggedIn = False
  return loggedIn

curUser = False

while True:
  choice = int(input('1 reg, 2 log, 3 leave'))
  print(curUser)
  if not loggedIn:
    print('you are not logged in')
  if loggedIn:
    print('logged in')
  if choice == 1:
    curUser = register()
    print('chose to register')
  elif choice == 2:
    print('chose to login')
    if not curUser:
      print('you need to register before you can loging you fuckface')
      continue
    login(curUser, loggedIn)
  elif choice == 3:
    break

print('loop over')