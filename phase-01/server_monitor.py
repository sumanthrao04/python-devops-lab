import health_utils
cpu=85
status=health_utils.check_health(cpu, 80)
print(f"CPU STATUS    : {status}")


try:
   cpu_usage=int(input("Enter the cpu value : "))
   print(f"The cpu Uage is : {cpu_usage}%")

except ValueError:
    print("Invalid CPU value, Please enter the numeric value between 0 to 100")
else:
    print(f"CPU Usage: {cpu_usage}%")
finally:
    print("Health check completed")
    
print("--------Multiple Exceptions-----------")

try:
    number1=int(input("Enter first Number"))
    number2=int(input("Enter Second Number"))
    result=number1/number2
    print(f"The result is : {result}")
    
except ValueError:
    print("Please Enter the Numeric Value")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
else:
    print("The result is output above")
    
finally:
    print("The Division operation is complted")    
    
 
try:
    cpuUse = int(input("Enter CPU usage: "))

except ValueError as error:
    print(f"Error: {error}")
    
    
try:
    file = open("servers.txt")
    
except FileNotFoundError:
    print("ERROR: servers.txt was not found")

except PermissionError:
    print("ERROR: Permission denied")

print("------------------raise — Creating Our Own Exception--------------------")    

try:
    Cpu_Result=int(input("Enter the CPU value"))
    print(f"The CPU usage : {Cpu_Result}")
    if Cpu_Result <0 or Cpu_Result >100:
      raise ValueError("CPU usage must be between 0 and 100")

except ValueError as error:
    print(f"ERROR: {error}")    
    