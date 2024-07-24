# A persional finance mannager 
users = {} 
# Username and Password checking
def register(username, Password):
   if username in users:
      return False
   else:
      users[username] = Password
      return True

def authenticate(username, Password):
   if username in users and users[username] == Password:
      return True
   else:
      return False

# Choice making by user

value = 'y'

while(value == 'y' or value == 'Y'):
   print("Welcome To Your Finance Mannager")
   print("To login to Your Account Press 1 \nTo Creat a new Account Press 2")
   choice = int(input("Enter Your Choice : "))

   if choice == 1:
      username = input("Enter The Username : ")
      Password = input("Enter Your Password : ")
      if authenticate(username, Password):
         print("Welcome Back", username, )
         value = input("Do you want to continue (y/n) : ")
      else :
         print("Authentication Failed Please Check Back")
         value = input("Do you want to continue (y/n) : ")

   elif choice == 2:
      username = input("Enter Your Username : ")
      Password = input("Enter Your password ")
      if register(username, Password):
         print("Username and Password Registerd Successfully")
         value = input("Do you want to continue (y/n) : ")
      else:
         print("Print Username Already Exist")
         value = input("Do you want to continue (y/n) : ")

   else:
      print("Wrong Choice Please Check Back")
      value = input("Do you want to continue (y/n) : ")
