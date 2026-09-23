print("-----------------For Loop------------------")

servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]

for server in servers:
    print(f"Connecting into the {server}")
    print(f"Checking Health of {server} Server..")
    print("Health Check Completed..")
    print()
    
    
cpu_usage=[45,82,65,91]

for cpu in cpu_usage:
    if cpu >=80:
        print(f"CPU is {cpu}% : WARNING ")
    else: 
        print(f"CPU is {cpu}% : HEALTHY")
        

print("-----------------Range------------------")  

for x in range(5):
        print(x)

print()

for y in range(1,6):
        print(y)

print()        

for z in range(2,14,2):
    print(z)    
    
    
print("--------Looping Through a Dictionary----------")    
server_details = {
    "hostname": "prod-app-01",
    "environment": "production",
    "cpu": 78,
    "memory": 85,
    "disk": 67
}

print()
for key in server_details:
    print(key)
    
print()

for value in server_details.values():
    print(value)
    
print()    
for key,value in server_details.items():
        print(f"{key} : {value}")
 

Multi_servers = [
    {
        "hostname": "prod-web-01",
        "cpu": 45
    },
    {
        "hostname": "prod-web-02",
        "cpu": 82
    },
    {
        "hostname": "prod-app-01",
        "cpu": 91
    }
] 

print("--------Multi-Server Information----------")
for server in Multi_servers:
    print(f"Hostname : {server['hostname']}")
    print(f"CPU : {server['cpu']}%")
    
    if server['cpu'] >=80:
        print("Status: WARNING")
        
    else:
        print("Status: HEALTHY")
    print()    


New_servers = [
    "prod-web-01",
    "maintenance-server",
    "prod-app-01"
]

print("--------Continue Statement----------")
for server in New_servers:

    if server == "maintenance-server":
        continue

    print(f"Checking {server}")


servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-db-01",
    "prod-app-01"
]

print("--------Break Statement----------")
for server in New_servers:

    if server == "maintenance-server":
        break

    print(f"Checking {server}")    

print("--------While Loop----------")
count = 1

while count <= 5:
    print(count)
    count = count + 1       

print("--------Assignment  — Multi-Server Health Checker----------")    

Assignment_servers = [
    {
        "hostname": "prod-web-01",
        "cpu": 45,
        "memory": 60,
        "disk": 55
    },
    {
        "hostname": "prod-web-02",
        "cpu": 85,
        "memory": 70,
        "disk": 65
    },
    {
        "hostname": "prod-app-01",
        "cpu": 65,
        "memory": 88,
        "disk": 70
    },
    {
        "hostname": "prod-db-01",
        "cpu": 55,
        "memory": 65,
        "disk": 92
    }
]

print("========= MULTI SERVER HEALTH CHECK =========")

for server in Assignment_servers:
    print(f"Server  : {server['hostname']}")
    print(f"CPU     : {server['cpu']}%")
    print(f"Memory  : {server['memory']}%")
    print(f"Disk    : {server['disk']}%")
    
    print()
    if server["cpu"]>=80:
        print("CPU STATUS    : WARNING")
    else:
        print("CPU STATUS    : HEALTHY")
        
    if server["memory"]>=80:
        print("Memory STATUS    : WARNING")
    else:
        print("Memory STATUS    : HEALTHY")    
        
    if server["disk"]>=85:
        print("Disk STATUS    : WARNING")    
    else:
        print("Disk STATUS    : HEALTHY") 

    print("--------------------------------------------") 

    