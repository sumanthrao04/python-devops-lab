# Phase 1 — Python Fundamentals for DevOps

We'll assume **zero Python knowledge**, but every concept will be connected to a DevOps use case.

Our goal for Phase 1 is not just learning syntax. By the end, you'll build a small **DevOps Server Health Report**.

## Phase 1 roadmap

| #  | Topic         | DevOps connection            |
| -- | ------------- | ---------------------------- |
| 1  | Python setup  | Running automation scripts   |
| 2  | `print()`     | Script output                |
| 3  | Variables     | Server/config values         |
| 4  | Data types    | Ports, hostnames, status     |
| 5  | Strings       | Logs, URLs, commands         |
| 6  | Lists         | Server/resource collections  |
| 7  | Tuples & Sets | Immutable/unique values      |
| 8  | Dictionaries  | JSON/config/cloud resources  |
| 9  | Conditions    | Threshold checking           |
| 10 | Loops         | Multiple servers/resources   |
| 11 | Functions     | Reusable automation          |
| 12 | Modules       | Organizing scripts           |
| 13 | Exceptions    | Handling automation failures |
| 14 | Files         | Logs/configuration           |
| 15 | JSON          | REST APIs/AWS                |
| 16 | YAML          | Kubernetes/CI/CD             |
| 17 | Mini project  | DevOps health reporter       |

---

# Lesson 1 — Python Setup

First check whether Python is installed.

Open PowerShell or CMD:

```powershell
python --version
```

If that doesn't work:

```powershell
py --version
```

You should get something similar to:

```text
Python 3.13.x
```

If Python isn't installed, install the current Python 3 release from Python's official site and enable **Add Python to PATH** during installation.

Also install **VS Code** and the Microsoft **Python extension**.

Create a learning directory:

```powershell
mkdir python-for-devops
cd python-for-devops
mkdir phase-01
cd phase-01
```

Create:

```text
01_hello_devops.py
```

---

# Lesson 2 — Your First Python Program

Put this inside the file:

```python
print("Hello DevOps!")
print("Starting Python automation journey")
```

Run:

```powershell
python 01_hello_devops.py
```

Output:

```text
Hello DevOps!
Starting Python automation journey
```

## What is `print()`?

`print()` displays information.

```python
print("Deployment started")
print("Checking server health")
print("Deployment completed")
```

Think of it like output from a Jenkins pipeline or shell script.

Bash:

```bash
echo "Deployment started"
```

Python:

```python
print("Deployment started")
```

---

# Lesson 3 — Variables

Variables are extremely important.

A variable stores a value so we can use it later.

```python
server_name = "prod-web-01"

print(server_name)
```

Think:

```text
variable
   ↓
server_name
   ↓
"prod-web-01"
```

You can create multiple variables:

```python
server_name = "prod-web-01"
environment = "production"
port = 8080
cpu_usage = 72

print(server_name)
print(environment)
print(port)
print(cpu_usage)
```

### Why variables matter in DevOps

Suppose your script checks a server:

```python
server = "app-prod-01"
port = 8080
environment = "production"
```

Hardcoding everything repeatedly would be messy:

```python
print("Checking app-prod-01")
print("Environment of app-prod-01 is production")
print("Port of app-prod-01 is 8080")
```

Instead:

```python
server = "app-prod-01"
environment = "production"
port = 8080

print("Checking", server)
print("Environment:", environment)
print("Port:", port)
```

Output:

```text
Checking app-prod-01
Environment: production
Port: 8080
```

---

# Lesson 4 — Python Data Types

This is one of the most important fundamentals.

Start with these four.

| Type    | Meaning      | DevOps example |
| ------- | ------------ | -------------- |
| `str`   | Text         | hostname       |
| `int`   | Whole number | port           |
| `float` | Decimal      | CPU usage      |
| `bool`  | True/False   | service status |

## 1. String — `str`

Text is represented using quotes.

```python
server_name = "prod-server-01"
environment = "production"
region = "ap-south-1"
```

These are strings.

Check:

```python
print(type(server_name))
```

Output:

```text
<class 'str'>
```

---

## 2. Integer — `int`

Whole numbers:

```python
port = 8080
instance_count = 5
restart_count = 3
```

Check:

```python
print(type(port))
```

Output:

```text
<class 'int'>
```

Notice the difference:

```python
port = 8080
```

versus:

```python
port = "8080"
```

The first is an integer.

The second is a string.

This distinction becomes important when processing environment variables, APIs and configuration files.

---

## 3. Float — `float`

Numbers containing decimals:

```python
cpu_usage = 72.5
memory_usage = 81.2
response_time = 1.45
```

Check:

```python
print(type(cpu_usage))
```

Output:

```text
<class 'float'>
```

---

## 4. Boolean — `bool`

Boolean means:

```text
True
False
```

For example:

```python
nginx_running = True
database_connected = False
```

Notice the capital letters:

```python
True
False
```

not:

```python
true
false
```

---

# Combine Them

Create:

```text
02_server_info.py
```

Add:

```python
server_name = "prod-web-01"
environment = "production"
port = 8080
cpu_usage = 67.5
nginx_running = True

print("Server:", server_name)
print("Environment:", environment)
print("Port:", port)
print("CPU Usage:", cpu_usage)
print("Nginx Running:", nginx_running)
```

Run:

```powershell
python 02_server_info.py
```

Output:

```text
Server: prod-web-01
Environment: production
Port: 8080
CPU Usage: 67.5
Nginx Running: True
```

You've already created the beginning of a monitoring script.

---

# Lesson 5 — f-strings

This is something you'll use **constantly** in Python automation.

Instead of:

```python
server = "prod-server-01"

print("Checking server", server)
```

Python provides f-strings:

```python
server = "prod-server-01"

print(f"Checking server {server}")
```

Output:

```text
Checking server prod-server-01
```

Multiple variables:

```python
server = "prod-server-01"
cpu = 75
memory = 82

print(f"Server: {server}")
print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
```

Output:

```text
Server: prod-server-01
CPU Usage: 75%
Memory Usage: 82%
```

This becomes very useful when generating logs:

```python
service = "nginx"
status = "running"

print(f"Service {service} is {status}")
```

---

# Lesson 6 — Getting Input

Sometimes an automation script needs information from the user.

Python provides:

```python
input()
```

Example:

```python
server = input("Enter server name: ")

print(f"Checking server {server}")
```

Running:

```text
Enter server name: prod-web-01

Checking server prod-web-01
```

Let's make it more DevOps-oriented.

Create:

```text
03_server_input.py
```

```python
server = input("Enter server hostname: ")
environment = input("Enter environment: ")
service = input("Enter service name: ")

print()
print("----- Server Information -----")
print(f"Server      : {server}")
print(f"Environment : {environment}")
print(f"Service     : {service}")
```

Run:

```powershell
python 03_server_input.py
```

Example:

```text
Enter server hostname: prod-app-01
Enter environment: production
Enter service name: nginx

----- Server Information -----
Server      : prod-app-01
Environment : production
Service     : nginx
```

---

# Important: `input()` Returns a String

Suppose:

```python
port = input("Enter port: ")
```

You enter:

```text
8080
```

You might think Python stores:

```python
8080
```

as an integer.

It doesn't.

It stores:

```python
"8080"
```

Check:

```python
port = input("Enter port: ")

print(type(port))
```

You'll see:

```text
<class 'str'>
```

Convert it:

```python
port = int(input("Enter port: "))
```

Now:

```python
print(type(port))
```

returns:

```text
<class 'int'>
```

This is called **type conversion**.

Common conversions:

```python
int("8080")
float("75.5")
str(8080)
```

---

# Lesson 7 — Your First DevOps Decision

Now we reach a very important Python feature:

```python
if
```

Imagine CPU usage is:

```python
cpu_usage = 85
```

We want:

```text
CPU < 80
     ↓
NORMAL

CPU >= 80
     ↓
WARNING
```

Python:

```python
cpu_usage = 85

if cpu_usage >= 80:
    print("WARNING: High CPU usage")
```

Output:

```text
WARNING: High CPU usage
```

Add `else`:

```python
cpu_usage = 60

if cpu_usage >= 80:
    print("WARNING: High CPU usage")
else:
    print("CPU usage is normal")
```

Output:

```text
CPU usage is normal
```

### The indentation is important

Python uses indentation:

```python
if cpu_usage >= 80:
    print("WARNING")
```

The spaces before `print()` tell Python:

> this statement belongs to the `if`.

This is incorrect:

```python
if cpu_usage >= 80:
print("WARNING")
```

---

# Comparison Operators

You'll use these frequently.

| Operator | Meaning       | Example         |
| -------- | ------------- | --------------- |
| `==`     | Equal         | `status == 200` |
| `!=`     | Not equal     | `status != 200` |
| `>`      | Greater       | `cpu > 80`      |
| `<`      | Less          | `cpu < 80`      |
| `>=`     | Greater/equal | `disk >= 90`    |
| `<=`     | Less/equal    | `cpu <= 70`     |

Be careful:

```python
=
```

means **assign a value**:

```python
environment = "production"
```

while:

```python
==
```

means **compare values**:

```python
if environment == "production":
    print("Production environment")
```

This distinction is extremely important.

---

# `if`, `elif`, `else`

Suppose:

```text
CPU < 70        → HEALTHY
CPU 70-89       → WARNING
CPU >= 90       → CRITICAL
```

Python:

```python
cpu_usage = 82

if cpu_usage >= 90:
    print("CRITICAL: CPU usage is very high")

elif cpu_usage >= 70:
    print("WARNING: CPU usage is high")

else:
    print("HEALTHY: CPU usage is normal")
```

Output:

```text
WARNING: CPU usage is high
```

Python checks from top to bottom.

```text
cpu = 82

Is CPU >= 90?
       ↓
      No

Is CPU >= 70?
       ↓
      Yes
       ↓
    WARNING
```

---

# First Hands-On DevOps Exercise

Create:

```text
04_cpu_monitor.py
```

Write:

```python
server = input("Enter server name: ")
cpu_usage = float(input("Enter CPU usage: "))

print()
print(f"Checking server: {server}")

if cpu_usage >= 90:
    print(f"CRITICAL: CPU usage is {cpu_usage}%")

elif cpu_usage >= 70:
    print(f"WARNING: CPU usage is {cpu_usage}%")

else:
    print(f"HEALTHY: CPU usage is {cpu_usage}%")
```

Test it three times.

### Test 1

```text
Enter server name: prod-web-01
Enter CPU usage: 45

Checking server: prod-web-01
HEALTHY: CPU usage is 45.0%
```

### Test 2

```text
Enter CPU usage: 78

WARNING: CPU usage is 78.0%
```

### Test 3

```text
Enter CPU usage: 95

CRITICAL: CPU usage is 95.0%
```

---

# Your First Assignment

Don't copy a solution yet.

Create:

```text
05_server_health.py
```

Ask the user for:

```text
Server name
CPU usage
Memory usage
Disk usage
```

Apply these rules:

```text
CPU >= 80       → WARNING
Memory >= 80    → WARNING
Disk >= 85      → WARNING
```

Expected output:

```text
Enter server: prod-app-01
Enter CPU usage: 45
Enter Memory usage: 82
Enter Disk usage: 91

========= SERVER HEALTH =========

Server : prod-app-01
CPU    : 45.0%
Memory : 82.0%
Disk   : 91.0%

CPU STATUS    : HEALTHY
MEMORY STATUS : WARNING
DISK STATUS   : WARNING
```

Try writing this yourself using only:

```python
print()
input()
variables
str
float
if
else
f-strings
```

Don't worry about making the code perfect. At this stage, repetition is actually useful.

### What you've learned so far

You can already understand this:

```python
server = input("Enter server: ")
cpu = float(input("Enter CPU usage: "))

if cpu >= 80:
    print(f"{server}: High CPU - {cpu}%")
else:
    print(f"{server}: CPU normal - {cpu}%")
```

That's the foundation of a real monitoring/automation script:

```text
Get data
   ↓
Store data
   ↓
Evaluate condition
   ↓
Take action
```

In the next Phase 1 lesson, we'll cover **strings → lists → tuples → sets → dictionaries**, with examples like server inventories, AWS instances and service lists. After that, loops will allow us to process **100 servers instead of writing code 100 times**.
