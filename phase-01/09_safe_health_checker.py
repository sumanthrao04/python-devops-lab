def validate_usage(usage):
    if usage < 0 or usage > 100:
        raise ValueError("Usage must be between 0 and 100")


def check_health(usage, threshold):
    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"


def server_health(server_name, cpu_usage, memory_usage, disk_usage):

    validate_usage(cpu_usage)
    validate_usage(memory_usage)
    validate_usage(disk_usage)

    print()
    print("========= SERVER HEALTH =========")
    print()

    print(f"Server : {server_name}")
    print()
    print(f"CPU    : {cpu_usage}%")
    print(f"Memory : {memory_usage}%")
    print(f"Disk   : {disk_usage}%")

    print()

    print(f"CPU STATUS    : {check_health(cpu_usage, 80)}")
    print(f"MEMORY STATUS : {check_health(memory_usage, 80)}")
    print(f"DISK STATUS   : {check_health(disk_usage, 85)}")


try:
    server_name = input("Enter server name : ")

    cpu_usage = int(input("Enter CPU usage : "))
    memory_usage = int(input("Enter Memory usage : "))
    disk_usage = int(input("Enter Disk usage : "))

    server_health(
        server_name,
        cpu_usage,
        memory_usage,
        disk_usage
    )

except ValueError as error:
    print(f"ERROR: {error}")