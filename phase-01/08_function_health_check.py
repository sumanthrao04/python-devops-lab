print("--------------Function -----------------")
def checkHealth():
    print("Checking server Health")
checkHealth()
print()

print("--------------Function Parameters-----------------")

def checkServerHealth(server):
    print(f"checking the server health : {server}")

checkServerHealth("prod-1-web")

print("--------------Multiple Parameters -----------------")
def server_info(hostname,cpu):
    print(f"server : {hostname}")
    print(f"cpu : {cpu}%")

server_info("prod-1-web", 80)

def check_cpu(cpu):
    if cpu >=80:
        print("CPU Status : WARNING...")
    else:
        print("CPU Status : Healthy...")

check_cpu(45)
check_cpu(90)

print("--------------Understanding return -----------------")

def check_cpu_health(cpu):
    if cpu>=80:
        return("CPU Status : WARNING...")
    else:
        return("CPU Status : Healthy...")
        
cpu_status=check_cpu_health(30)   
print(cpu_status) 

print("--------------Refactor Your Health Checker Using Functions -----------------")

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

def check_health(usage, threshold):
    if usage>=threshold:
        return "WARNING"
    else:
        return "HEALTHY"
        
    
def cpustatus():
        return(f"CPU STATUS    : ")
        
def memorystatus():
        return(f"MEMORY STATUS : ")        
        
def diskstatus():
    return(f"DISK STATUS   : ")        
        

print("========= MULTI SERVER HEALTH CHECK =========")        
for server in Assignment_servers:
    print(f"Server  : {server["hostname"]}")
    print(f"CPU     : {server["cpu"]}%")
    print(f"Memory  : {server["memory"]}%")
    print(f"Disk    : {server["disk"]}%")
    print()
    print(cpustatus(),check_health(server["cpu"],80))
    print(memorystatus(),check_health(server["memory"],80))
    print(diskstatus(),check_health(server["disk"],85))
    print()
    print("--------------------------------------------")
        
        
    
        