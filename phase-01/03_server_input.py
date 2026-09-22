server = input("Enter Server Host Name: ")
environmnet = input("Enter Environmnet Name: ")
service= input("Enter Service name: ")

print()
print("----- Server Information -----")
print(f"Server Host name : {server}.")
print(f"Environmnet Name : {environmnet}.")
print(f"Service Name: {service}.")

print("-------------------type conversion. --------------------------------")

Port = input("Enter Port Number: ")
print(type(Port))

Used_Port = input("Enter Used  Port Number: ")
print(type(int(Used_Port)))
