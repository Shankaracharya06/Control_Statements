import pickle
import time
from datetime import datetime


'''This is a class of Quotify which is a social media application in which users can post their thoughts'''
class Quotify:

    '''This is the constructor method'''
    def __init__(self):

        self.post = {'unique_id_post_list': []}  # Initialize a dictionary to store posts (initially empty)
        self.blocked = {}
        print()
        print("Welcome to Quotify")

        while True:
            print()

            choice = input("Would you like to:\n1.Sign up \n2.Sign in \n3.Exit:\n ")

            if choice == "1":
                self.register()  # Call the register method to create a new user

                # To Save the user's post data we need a new pickle file
                # after successfull registration,immediately assigning a dictionary(pickle file) which will store all the post related infromation
                with open(self.user + '.pickle' , "wb") as file:
                    pickle.dump(self.post, file) 

                with open('blocked_user' + '.pickle' , "wb") as file:
                    pickle.dump(self.post, file)  

            elif choice == "2":
                self.username = input("Enter Username:")
                if self.block() == True:
                    break
                else:
                    if self.login() != True:  # Call the login method to allow an existing user to log in
                        break

                while True:
                    # Display options for logged-in user
                    choice = input("1.New Post\n2.Your Posts\n3.Logout\n ")
                    if choice == "1":
                        # To add a new post
                        self.add_a_post()

                    elif choice == "2":
                        # To get and display user's own posts
                        self.get_own_post()
                        print()

                    elif choice == "3":
                        # To get and display user's own posts
                        self.find_friend()
                        print()
                    else:
                        self.logout()  # Log out the user if they choose this option
                        break
        
            elif choice == "3":
                break  # Exit the application
            else:
                print("Invalid choice. Please try again..")

    '''This Method is for Registering a New User'''
    def register(self):
        username = input("Enter Username:")
        self.user = username
        self.username = username  # Store the username

        try:
            with open('accounts.pickle', "rb") as file:
                data = pickle.load(file)  # Load existing accounts from the file
        except:
            data = {}  # If the file doesn't exist or is corrupted, initialize an empty dictionary

        # Check if the username already exists
        if username not in data:
            for _ in range(5):
                actual_password = input("Enter Password:")

                # Validate password length and content
                if len(actual_password) > 8:
                    if actual_password.isalnum() == False:
                        confirm_password = input("Confirm Password:")

                        # Validation of the entered password and the confirm password both are same or not
                        if actual_password == confirm_password:
                            # Save the username and password to the 'accounts.pickle' file
                            data[username] = actual_password
                            with open('accounts.pickle', "wb") as file:
                                pickle.dump(data, file)

                            print("Account Created Successfully...")
                            break
                        else:
                            print("Password and confirm password should be the same.")
                    else:
                        print("Password should be a combination of alphanumeric and special characters. Please try again.")
                else:
                    print("Password length should be greater than 8.")
            else:
                print("5 attempts done... Thank you for visiting.")
        else:
            print("Username Already Exists!")

    '''This Method is for Login'''
    def login(self):
        print()

        # Load account data
        with open('accounts.pickle', "rb") as file:
            data = pickle.load(file)  

        # Check if the entered username exists in the data
        if self.username in data:
            for _ in range(3):
                password = input("Enter Password:")

                # Validate the entered password
                if password == data[self.username]:
                    print("Login Successful...")
                    print()
                    return True
                else:
                    print("Wrong Password. Please try again.")
            else:
                print("3 Attempts Failed, you are blocked for 24 hours.")
                with open('blocked_user.pickle', "rb") as file:
                    block_user = pickle.load(file)
                
                current_time = datetime.now()

                current_hours = current_time.strftime("%Y%m%d%H%M%S%f")
                # current_minutes = current_time.strftime("%M")
                # current = current_hours * 60 + current_minutes

                block_user[self.username] = current_hours
                
                with open('blocked_user.pickle',"wb") as file:
                    pickle.dump(block_user,file)
                return False

        else:
            print("User Not Found!")
            print()
            choice = input("1.Create a New Account\n2.Sign In ")
            if choice == "1":
                self.register()  # If the user doesn't exist, offer to create a new account
            elif choice == "2":
                self.login()  # Allow the user to try logging in again

    '''This method is for adding a new post'''
    def add_a_post(self):

        print()
        actual_time_now = datetime.now()

        # Generate a unique post ID based on the current time
        unique_id_post = actual_time_now.strftime("%Y%m%d%H%M%S%f")[:-6]

        quote = input("Write Your Quote Here...\n")

        post_key = self.username + f"{unique_id_post}"  # Combine the username and unique post ID to create the post key
                          
        # Load the user's pickle file containing posts
        with open(self.username + '.pickle' , "rb") as file:
            data = pickle.load(file)

        data[post_key] = quote  # Add the new post with the generated key and quote as the value
        
        # Append the post key to the list of unique IDs in the user's file
        data['unique_id_post_list'].append(post_key)

        print("Uploading...")
        time.sleep(1.5) 
        print("Posted Successfully...")

        # Save the updated posts data to the user's file
        with open(self.username + '.pickle' , 'wb') as file:
            pickle.dump(data, file)
        print()

    '''This method is for printing all posts of a user'''
    def get_own_post(self):
        print()
        print("----------  POSTS  ----------")

        # Load the user's post data
        with open(self.username + '.pickle', "rb") as file:
            data = pickle.load(file)

        if len(data['unique_id_post_list']) == 0:
            print("No Post")
            print("What are you thinking Dear!!")
        else:
            count = 0
            # Loop through the posts and display them
            for item in data:
                if item == 'unique_id_post_list':  # Skip the 'unique_id_post_list' key
                    continue
                count += 1
                print(f"{count}.{data[item]}")

            # Ask if the user wants to delete a post
            
            while True:
                choice = input("Do you want to delete a post (Y/N)? ")
                if choice in ('Y', 'y'):
                    self.delete_a_post()
                    break
                else:
                    print("invalid option")

    '''This method is for deleting an existing post'''
    def delete_a_post(self):
        with open(self.username + ".pickle", 'rb') as file:
            data = pickle.load(file)

        if not data:
            print("Nothing to delete! Please add some posts first.")
        else:
            while True:
                try:
                    user_choice = int(input("Choose the post from above to delete: "))
                    break
                except Exception as error_msg:
                    print(error_msg)

            # Loop through the list of posts and match the user choice to the post
            for choice in range(1, len(data['unique_id_post_list']) + 1):
                if choice == user_choice:
                    deleted_key = data['unique_id_post_list'].pop(choice - 1)  # Remove the post key from list
                    data.pop(deleted_key)  # Remove the post entry from the dictionary

                    print("Deleting...")
                    time.sleep(1.5)  
                    print("Post Deleted Successfully...")

                    # Save the updated data back to the user's file
                    with open(self.username + ".pickle", 'wb') as file:
                        pickle.dump(data, file)

    '''This Method is for logging out from the application'''
    def logout(self):
        print("Logged Out Successfully")
        print()
        print("---------- THANK YOU!! VISIT AGAIN ----------")

    def find_friend(self):
        username = input("Enter friend's name or username or first char:")
        with open('accounts.pickle', 'rb') as file:
            data = pickle.load(file)
        for actual_username in data:
            if username or username[0] in actual_username:
                print(actual_username)
                #######################################################################################################
                while True:
                    choice = input("Do you want to send a request:(Y/N)")
                    if choice == "Y" or "y":
                        with open("actual_username.pickle", 'rb') as file:
                            data = pickle.load(file)
                        
                    elif choice == "N" or "n":
                        break
                    else:
                        print("Wrong choice")
    def send_request(self):
        ...

    def see_friend_post(self):
        ...

    def like_post(self):
        ...

    def unfriend(self):
        ...

    def show_friend(self):
        ...

    def friend_requests(self):
        ...

    def block(self):
        
        # Load account data
        with open('blocked_user.pickle', "rb") as file:
            data = pickle.load(file)  

        if self.username in data:
            print(" Already Blocked for 24 hours")
            return True

    def comment_a_post(self):
        ...


# Create an instance 3(object) of the Quotify class to start the program
shan = Quotify()