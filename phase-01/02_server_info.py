server_name = "prod-web-01"
environment = "production"
port = 8080
cpu_usage = 67.5
nginx_running = True
service = "nginx"
status = "running"

print("Server:", server_name)
print("Environment:", environment)
print("Port:", port)
print("CPU Usage:", cpu_usage)
print("Nginx Running:", nginx_running)


print("-------------------F Strings --------------------------------")
print(f"Server Name : {server_name} ")
print(f"Envrionment : {environment}")
print(f"Port : {port}")
print(f"Cpu Usage : {cpu_usage }%")
print(f"service {service} is {status}")
print(F"Nginx Running :  {nginx_running}")