print("========= LIST OF SERVER DETAILS =========")

servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]

print()
print("========= SERVER INVENTORY =========")

print(f"First Server  : {servers[0]}")
print(f"Second Server : {servers[1]}")
print(f"Total Servers : {len(servers)}")

servers.append("prod-monitoring-01")

print(f"Updated Total Servers : {len(servers)}")


server_details = {
    "hostname": "prod-app-01",
    "environment": "production",
    "cpu": 78,
    "memory": 85,
    "disk": 67
}

print()
print("========= SERVER DETAILS =========")

print(f"Hostname    : {server_details['hostname']}")
print(f"Environment : {server_details['environment']}")
print(f"CPU         : {server_details['cpu']}%")
print(f"Memory      : {server_details['memory']}%")
print(f"Disk        : {server_details['disk']}%")

print()
print("========= HEALTH CHECK =========")

if server_details["cpu"] >= 80:
    print("CPU STATUS    : WARNING")
else:
    print("CPU STATUS    : HEALTHY")

if server_details["memory"] >= 80:
    print("MEMORY STATUS : WARNING")
else:
    print("MEMORY STATUS : HEALTHY")

if server_details["disk"] >= 85:
    print("DISK STATUS   : WARNING")
else:
    print("DISK STATUS   : HEALTHY")