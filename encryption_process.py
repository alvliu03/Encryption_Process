import bcrypt

def welcome():
    print("Welcome to the website!")

def authentication(Username = None, Password = None):
    Username = input("Please enter your username: ")
    Password = input("Please enter your password: ")

    if not len(Username or Password) < 1:
        #after making sure the length of username and password is greater than one it open the text file, a and b are made
        #into a list and added to d and f with us removing the trailing whitespaces of b. Then dictionary called data is created by zipping
        #d and f together so the first item of d will correspond with first item in f.
        if True:
            #sample_database = open("database.txt", "r")
            d = []
            f = []
            with open("database.txt", "r") as sample_database:
                for i in sample_database:
                    a,b = i.split(",")
                    b = b.strip()
                    d.append(a)
                    f.append(b)
                    data = dict(zip(d,f))
            #the code below is an error checker to make sure the username and password matches in whats the sample database.
            try:
                #Code below get the hased password from the dictionary of data associated with the corresponding username and converts it into a language machines can understand.
                #However, it would first need to strip the letter b from the beginning or end and replace ' with nothing.
                if Username in data:
                    hashed = data[Username].strip("b")
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode("utf-8")
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                            print("Login Successful!")
                            print(f"Hi {Username}!")
                            welcome()
                        else:
                            print("Wrong password")
                    except:
                        print("Incorrect Username or Password!")
                else:
                    print("Username doesn't exist!")
            except:
                print("Password or username doesn't exist.")
        else:
            print("Error logging into the system.")
    else:
        print("Please attempt to sign in again as you need more than one character for username or password.")
        authentication()

def sign_up(Username = None, Password1 = None, Password2 = None):
    Username = input("Enter a username:\n")
    Password1 = input("Create password:\n")
    Password2 = input("Confirm Password:\n")
    #sample_database = open("database.txt", "r")
    d = []
    with open("database.txt", "r") as sample_database:
        for i in sample_database:
            a,b = i.split(",")
            b = b.strip()
            d.append(a)
    #Code below check to see if a newly registered username already exists. It will also hashes and salt a good sized password.
    if not len(Password1) < 13:
        with open("database.txt", "r") as sample_database:
            if not Username == None:
                if len(Username) < 1:
                    print("Please provide a valid username.")
                    sign_up()
                elif Username in d:
                    print("Username exists already.")
                    sign_up()
                else:
                    if Password1 == Password2:
                        Password1 = Password1.encode('utf-8')
                        salted_password1 = bcrypt.gensalt()
                        Password1 = bcrypt.hashpw(Password1, salted_password1)
                                        
                        with open("database.txt", "a") as sample_database:
                            sample_database.write(f"{Username}, {str(Password1)}\n")
                            print("User created successfully!")
                            print("Please login to proceed!")
                    else:
                        print("Passwords do not match")
                        sign_up()
    else:
        print("Please input a password greater than or equal to 13 characters.")

#This is the main function that would allow a user to login in or sign up.
def main(option = None):
    print("Welcome! Please accept an option.")
    option = input("Login | Sign Up\n")
    if option == "Login":
        authentication()
    elif option == "Sign Up":
        sign_up()
    else:
        print("Please enter a valid parameter, this is case-sensitive.")

main()
