highway_initial_number = int(input("Enter your highway number: "))
while highway_initial_number != 0:
  while highway_initial_number > 999:
    highway_initial_number = int(input("Please re-enter your highway number. Remember that that the number must be less than 1000 here: "))
  if highway_initial_number > 99:
    highway_type = "auxilliary highway"
    highway_initial_number_last_two_digits = highway_initial_number % 100
  if highway_initial_number <= 99:
    highway_type = 1
    print(highway_initial_number)
  if highway_initial_number % 2 == 0:
    highway_direction = "east to west"
  if highway_initial_number % 2 == 1:
    highway_direction = "north to south"
  if highway_type == 1:
    highway_type = "main highway"
    print("The highway is a  " + highway_type + ", and runs " + highway_direction)
  if highway_type == "auxilliary highway":
    print("The highway is a  " + highway_type + ", and runs " + highway_direction + ". It serves main highway number " + str(highway_initial_number_last_two_digits))
  highway_initial_number = int(input("Enter your highway number: "))
print("Thank you for using the highway database!")
