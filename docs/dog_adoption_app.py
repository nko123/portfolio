# Interactive Dog Adoption Application
# University of Ottawa - ADM 4311
# By: Nkem Okweye

# Part 1 - Basic Login and Search Functionality

# Login function
user_name = ['vbrad','nokwe','dadel','hjami']
user_password = ['brad123','okwe123','johnhancock1977','jami1234']

login_username = input("Enter your username (Note: Case Sensitive): ")
login_password = input("Enter your password (Note: Case Sensitive): ")

# For loop to login
for n in user_name and user_password:
  if login_username in user_name and login_password in user_password:
    print("Login Successful")
    break
  else:
    print("Username or Password is wrong, Try again")
    break

stuff = ["Adopt a Dog", "Foster a Dog ", "Donate a Dog", "Dog Therapy", "Dog Yoga ", "Dog Training", "Dog Grooming","Dog Recipes"]

print("Welcome to Woof Woof, a one stop for all things dogs!")

search_function = input("What Service are you looking for today: ")
search_function = search_function.lower()

options_list = []

# Using a for loop to search for a partial match in the list
for s in stuff:
  s = s.lower()
  m = s.startswith((search_function))
  if m == True or search_function in s:
    options_list.append(s)

# Check if anything was found
if options_list == []:
  print(f"No results found with search")
else:
    print(f"Here are results that match your search:")
    for index, op in enumerate(options_list):
        new_index = index + 1
        print(f"{new_index}. {op}")

    num_stuff_selec = int(input("Select an option from the list: "))
    new_num_stuff_selec = int(num_stuff_selec) - 1

    if new_num_stuff_selec >= 0 and new_num_stuff_selec < len(options_list):
        print(f'You have chosen {num_stuff_selec} and want to view {options_list[new_num_stuff_selec]}')
    else:
        print(f'You have entered {num_stuff_selec}, which is not on the list.')

# Part 2 - Enhanced Application with Dictionary-based Authentication

user_details = {'vbrad': {'firstname':'valerie', 'lastname': 'bradley', 'password': 'brad123' },
                'nokwe': {'firstname':'nkemdibe', 'lastname': 'okweye', 'password': 'okwe123'},
                'dadel': {'firstname':'daniel', 'lastname': 'adelberg', 'password': 'johnhancock1977'},
                'hjami': {'firstname':'hisham', 'lastname': 'jamil', 'password': 'jami1234'}
        }

stuff = ["Adopt a Dog", "Foster a Dog ", "Dog Therapy", "Dog Yoga ", "Dog Training", "Dog Grooming"]

dog_database = {'luna': {'breed':'husky', 'gender':'female', 'age': '12 months', 'status': 'available','attribute': 'good with kids'},
             'rex': {'breed':'greman shepherd', 'gender':'male', 'age': '6 months', 'status': 'available','attribute': 'good around other dogs '},
             'prince': {'breed':'doberman', 'gender':'male', 'age': '2 years', 'status': 'unavailable','attribute': 'freindly'},
             'daisy': {'breed':'goldendoodle', 'gender':'male', 'age': '2 years', 'status': 'available','attribute': 'energetic'},
             'koda': {'breed':'samoyed', 'gender':'female', 'age': '4 months', 'status': 'unavailable','attribute': 'playful'},
                'mona': {'breed':'husky', 'gender':'female', 'age': '7 months', 'status': 'available','attribute': 'nice'},
                'lola': {'breed':'dalmation', 'gender':'female', 'age': '2 months', 'status': 'available','attribute': 'protective'}
             }

options_list, avail_dog_database = [], []

# Check if the user's name matches their password
login_user = input("Enter your username (Note: Case Sensitive): ")
login_pass = input("Enter your password (Note: Case Sensitive): ")

for user in user_details:
  if login_user in user_details and login_pass == user_details[login_user]['password']:
    print("Login Successful")

    print(f"Welcome {user_details[login_user]['firstname']} {user_details[login_user]['lastname']} to Woof Woof, a one-stop for all things dogs!")
    search_function = input("What Service are you looking for today: ")
    search_function = search_function.lower()

    # Search for matching services
    for s in stuff:
      s = s.lower()
      m = s.startswith((search_function))
      if m == True or search_function in s:
        options_list.append(s)
        continue

    if options_list != []:
      print(f"Here are results that match your search:")

      for index, op in enumerate(options_list):
        new_index = index + 1
        print(f"{new_index}. {op}")

      num_stuff_selec = int(input("Select an option from the list: "))
      new_num_stuff_selec = int(num_stuff_selec) - 1

      # Check if the number entered is valid
      if new_num_stuff_selec >= 0 and new_num_stuff_selec < len(options_list):
        print(f'You have chosen {num_stuff_selec} and want to view {options_list[new_num_stuff_selec]}')

        print(f'Here are the dogs available:')
        for dog in dog_database:
          if dog_database[dog]['status'] == 'available':
            avail_dog_database.append(dog)

      else:
        print(f'You have entered {num_stuff_selec}, which is not on the list.')
        break

    else:
      print(f"No results found with search")

  else:
    print("Username or Password is wrong, Try again")

  break

# Handle dog adoption
if avail_dog_database != [] and options_list[new_num_stuff_selec] == "adopt a dog":
  for i, adog in enumerate(avail_dog_database):
    new_i = i + 1
    print(f"{new_i}. {adog}, {dog_database[adog]['breed']}, {dog_database[adog]['gender']}, {dog_database[adog]['age']}, {dog_database[adog]['attribute']}")

  num_avail_dog = int(input("Select a dog from the list: "))
  new_num_avail_dog = int(num_avail_dog) - 1

  if new_num_avail_dog >= 0 and new_num_avail_dog < len(avail_dog_database):
    print(f'You have chosen {avail_dog_database[new_num_avail_dog]}')

    adopt_choice = input("Enter Yes to confirm adoptions and No to cancel: ")
    adopt_choice = adopt_choice.lower()

    if adopt_choice == "yes":
      dog_database[avail_dog_database[new_num_avail_dog]]['status']='unavailable'

      print(f'Your adoption process of {avail_dog_database[new_num_avail_dog]} is complete')
      print(f"{avail_dog_database[new_num_avail_dog]} status has now been updated to {dog_database[avail_dog_database[new_num_avail_dog]]['status']}")

    else:
      print(f'Your adoption process of {avail_dog_database[new_num_avail_dog]} was not complete')

  else:
    print(f'You have entered {num_avail_dog}, which is not on the list ')

# Handle other services
if avail_dog_database != [] and options_list[new_num_stuff_selec] != "adopt a dog":
    for i, adog in enumerate(avail_dog_database):
        print(f"{i+1}. {adog}, {dog_database[adog]['breed']}, {dog_database[adog]['gender']}, {dog_database[adog]['age']}, {dog_database[adog]['attribute']}")

    num_service_dog = int(input("Select a dog from the list for the service: "))
    new_num_service_dog = num_service_dog - 1

    if new_num_service_dog >= 0 and new_num_service_dog < len(avail_dog_database):
        selected_dog = avail_dog_database[new_num_service_dog]
        print(f'You have chosen {selected_dog} for {options_list[new_num_stuff_selec]}.')

        confirm_choice = input("Enter Yes to confirm and No to cancel: ").lower()
        if confirm_choice == "yes":
            dog_database[selected_dog]['status'] = 'unavailable'
            print(f'{selected_dog} has been booked for {options_list[new_num_stuff_selec]}.')
            print(f"{avail_dog_database[new_num_service_dog]} status has now been updated to {dog_database[avail_dog_database[new_num_service_dog]]['status']}")
        else:
            print(f'Your booking of {selected_dog} for {options_list[new_num_stuff_selec]} was not complete.')
    else:
        print(f'You have entered {num_service_dog}, which is not on the list.')
