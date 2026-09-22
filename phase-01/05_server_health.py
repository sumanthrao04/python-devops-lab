print("-----First Assignment------")

Server_name= input("Enter the Server name : ")
CPU_usage = int(input("Enter the CPU usage : "))
Memory_usage = int(input("Enter the Memory usage : "))
Disk_usage = int(input("Enter the Disk usage : "))

print("========= SERVER HEALTH =========")
print(f"Server : {Server_name}")
print(f"CPU    : {CPU_usage}%")
print(f"Memory : {Memory_usage}%")
print(f"Disk   : {Disk_usage}%")
print()
if CPU_usage>=80:
    print("CPU STATUS    : WARNING")
else:
    print("CPU STATUS    : HEALTHY")
    
if Memory_usage>=80:
    print("MEMORY STATUS : WARNING")
else:
    print("MEMORY STATUS : HEALTHY")
    
if Disk_usage>=85:
    print("DISK STATUS   : WARNING")
else:
    print("DISK STATUS   : HEALTHY")
    
    
