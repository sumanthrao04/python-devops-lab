server=input("Enter the Server Name: ")
cpu_usage=float(input("Enter the CPU Usage: "))
print()
print(f"Checking : {server}...")

if cpu_usage>=90:
    print(f"CRITICAL CPU USAGE IS : {cpu_usage}%")
    
elif cpu_usage>=80:
    print(f"WARNING CPU USAGE IS : {cpu_usage}% ")

else:
    print(f"HEALTHY: CPU USAGE IS: {cpu_usage}%")