Your assignment is correct. More importantly, you've correctly used the concepts we wanted to practice: `input()`, variables, `int()`, f-strings, comparison operators, and `if/else`.

Your logic produces exactly the expected statuses:

```text
CPU    = 45  → 45 >= 80 → False → HEALTHY
Memory = 82  → 82 >= 80 → True  → WARNING
Disk   = 91  → 91 >= 85 → True  → WARNING
```

### 1. One improvement: Python variable naming

You wrote:

```python
Server_name
CPU_usage
Memory_usage
Disk_usage
```

This works, but Python convention uses **snake_case lowercase names**:

```python
server_name
cpu_usage
memory_usage
disk_usage
```

So prefer:

```python
server_name = input("Enter the Server name : ")
cpu_usage = int(input("Enter the CPU usage : "))
memory_usage = int(input("Enter the Memory usage : "))
disk_usage = int(input("Enter the Disk usage : "))
```

This will become especially important when your scripts grow larger.

### 2. `int()` was a good choice

You wrote:

```python
CPU_usage = int(input("Enter the CPU usage : "))
```

Remember what happens here.

First:

```python
input("Enter CPU usage: ")
```

If you enter:

```text
45
```

`input()` actually gives Python:

```python
"45"
```

That's a string.

Then:

```python
int("45")
```

converts it to:

```python
45
```

Now Python can perform:

```python
45 >= 80
```

Without the `int()` conversion, you'd eventually run into problems comparing the input with an integer threshold.

### 3. Your three independent `if` statements are correct

This is worth understanding.

You wrote:

```python
if cpu_usage >= 80:
    ...
else:
    ...

if memory_usage >= 80:
    ...
else:
    ...

if disk_usage >= 85:
    ...
else:
    ...
```

That's exactly what we want.

Python checks **all three independently**:

```text
                    Server Health
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       CPU Check      Memory Check    Disk Check
          │              │              │
       >= 80?          >= 80?         >= 85?
          │              │              │
      Yes / No        Yes / No       Yes / No
```

Don't change this into one large `if/elif/else`, because then Python might stop after one matching condition and skip other health checks.

### 4. Think like a DevOps engineer

Your current script is:

```text
User manually enters CPU
        ↓
Python stores CPU
        ↓
Python compares threshold
        ↓
Python reports health
```

Today:

```python
cpu_usage = int(input("Enter CPU usage: "))
```

Later we'll replace manual input with something like:

```python
cpu_usage = psutil.cpu_percent()
```

Then Python can collect the actual server CPU usage.

Eventually your script can become:

```text
Linux Server
     │
     ├── CPU ──────┐
     ├── Memory ───┤
     ├── Disk ─────┤
     └── Services ─┤
                   ↓
             Python Script
                   ↓
           Threshold Check
                   ↓
        ┌──────────┴─────────┐
        ↓                    ↓
     HEALTHY              WARNING
                             ↓
                         Send Alert
```

That's why these basic exercises matter.

---

# Phase 1 — Lesson 2: Collections

Now you're ready for one of the most important Python topics for DevOps:

**collections**.

We'll learn:

```text
List
Tuple
Set
Dictionary
```

Don't try to memorize definitions. Understand **what problem each one solves**.

---

## 1. Lists

Imagine you're managing five servers:

```text
prod-web-01
prod-web-02
prod-app-01
prod-app-02
prod-db-01
```

You could do:

```python
server1 = "prod-web-01"
server2 = "prod-web-02"
server3 = "prod-app-01"
server4 = "prod-app-02"
server5 = "prod-db-01"
```

This becomes terrible with 100 servers.

Instead:

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-app-02",
    "prod-db-01"
]
```

That's a **list**.

A list uses:

```text
[ ]
```

For example:

```python
ports = [80, 443, 8080, 9090]
```

or:

```python
services = ["nginx", "docker", "jenkins", "ssh"]
```

### Accessing list values

Python starts counting from **0**, not 1.

```python
servers = ["web-01", "app-01", "db-01"]
```

Think:

```text
Index       Value

  0         web-01
  1         app-01
  2         db-01
```

So:

```python
print(servers[0])
```

returns:

```text
web-01
```

And:

```python
print(servers[2])
```

returns:

```text
db-01
```

This is called **indexing**.

Try:

```python
services = ["nginx", "docker", "jenkins", "ssh"]

print(services[0])
print(services[1])
print(services[2])
```

---

## 2. Changing a list

Lists are **mutable**.

That simply means:

> We can change them after creating them.

For example:

```python
servers = ["web-01", "app-01"]

servers.append("db-01")

print(servers)
```

Output:

```text
['web-01', 'app-01', 'db-01']
```

`append()` adds an item.

Remove one:

```python
servers.remove("app-01")
```

Now:

```text
['web-01', 'db-01']
```

Check number of servers:

```python
print(len(servers))
```

If there are two:

```text
2
```

You'll use `len()` constantly.

---

# 3. Tuple

A tuple looks similar:

```python
ports = (80, 443, 8080)
```

Notice:

```text
List
[80, 443, 8080]

Tuple
(80, 443, 8080)
```

The major beginner-level difference is:

**List → can change**

**Tuple → generally used when values shouldn't change**

For example:

```python
production_regions = (
    "ap-south-1",
    "us-east-1"
)
```

For now, that's enough. We'll encounter tuples naturally later.

---

# 4. Set

Suppose you have:

```python
servers = [
    "web-01",
    "web-01",
    "app-01",
    "app-01",
    "db-01"
]
```

But you only want unique server names.

Use a set:

```python
servers = {
    "web-01",
    "web-01",
    "app-01",
    "app-01",
    "db-01"
}

print(servers)
```

You'll get unique values.

Conceptually:

```text
Input

web-01
web-01
app-01
app-01
db-01

       ↓ SET

web-01
app-01
db-01
```

Sets become useful for things like comparing unique IP addresses, environments, regions, users, or resource IDs.

---

# 5. Dictionary — VERY IMPORTANT FOR DEVOPS

Spend extra attention here.

A dictionary stores:

```text
key → value
```

Your server has:

```text
hostname     → prod-app-01
environment  → production
cpu          → 45
memory       → 82
disk         → 91
```

Python:

```python
server = {
    "hostname": "prod-app-01",
    "environment": "production",
    "cpu": 45,
    "memory": 82,
    "disk": 91
}
```

Retrieve hostname:

```python
print(server["hostname"])
```

Output:

```text
prod-app-01
```

Retrieve memory:

```python
print(server["memory"])
```

Output:

```text
82
```

Now combine it with what you already know:

```python
if server["memory"] >= 80:
    print("WARNING: High memory usage")
else:
    print("Memory usage is healthy")
```

This is much closer to real DevOps automation.

---

# Why dictionaries matter so much

APIs commonly return JSON-like structures.

For example, imagine an AWS-related response:

```python
instance = {
    "instance_id": "i-123456",
    "instance_type": "t3.micro",
    "state": "running",
    "region": "ap-south-1"
}
```

You could access:

```python
print(instance["instance_id"])
print(instance["state"])
```

Later when we learn **JSON, REST APIs and Boto3**, this knowledge will be extremely useful.

---

# Your Assignment 2

Create:

```text
06_server_inventory.py
```

Create a list containing:

```text
prod-web-01
prod-web-02
prod-app-01
prod-db-01
```

Your program should print:

```text
========= SERVER INVENTORY =========

First Server : prod-web-01
Second Server: prod-web-02

Total Servers: 4
```

Then add:

```text
prod-monitoring-01
```

using:

```python
.append()
```

And print:

```text
Updated Total Servers: 5
```

### Part 2 — Dictionary

Create this dictionary yourself:

```text
hostname    = prod-app-01
environment = production
cpu         = 78
memory      = 85
disk        = 67
```

Print:

```text
========= SERVER DETAILS =========

Hostname    : prod-app-01
Environment : production
CPU         : 78%
Memory      : 85%
Disk        : 67%

========= HEALTH CHECK =========

CPU STATUS    : HEALTHY
MEMORY STATUS : WARNING
DISK STATUS   : HEALTHY
```

Rules:

```text
CPU >= 80       → WARNING
Memory >= 80    → WARNING
Disk >= 85      → WARNING
```

For this assignment, use:

```python
list
.append()
len()
dictionary
if/else
f-string
```

Good work. Your **list logic, dictionary creation, dictionary access, `len()`, `.append()`, and threshold conditions are correct**.

There is just one important mistake in the output labels.

### 1. Bug in Memory and Disk output

You currently have:

```python
if Dictionary_of_Servers['memory'] >= 80:
    print("CPU STATUS    : WARNING")
```

and:

```python
if Dictionary_of_Servers['disk'] >= 85:
    print("CPU STATUS    : WARNING")
```

The conditions are correct, but you're printing `CPU STATUS` for all three checks.

They should be:

```python
if Dictionary_of_Servers['memory'] >= 80:
    print("MEMORY STATUS : WARNING")
else:
    print("MEMORY STATUS : HEALTHY")

if Dictionary_of_Servers['disk'] >= 85:
    print("DISK STATUS   : WARNING")
else:
    print("DISK STATUS   : HEALTHY")
```

This is a good example of a real automation problem: **the logic can be correct while the reported information is wrong**.

In production, misleading output can be just as problematic as incorrect logic.

---

### 2. Improve the variable name

You used:

```python
Dictionary_of_Servers
```

Python convention would be:

```python
server_details
```

So instead of:

```python
Dictionary_of_Servers["cpu"]
```

I'd recommend:

```python
server_details["cpu"]
```

It's shorter, cleaner, and follows Python's normal `snake_case` convention.

---

## Cleaned-up version of your code

You don't need to rewrite everything, but compare this with yours:

```python
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
```

Expected result:

```text
========= SERVER INVENTORY =========

First Server  : prod-web-01
Second Server : prod-web-02
Total Servers : 4
Updated Total Servers : 5

========= SERVER DETAILS =========

Hostname    : prod-app-01
Environment : production
CPU         : 78%
Memory      : 85%
Disk        : 67%

========= HEALTH CHECK =========

CPU STATUS    : HEALTHY
MEMORY STATUS : WARNING
DISK STATUS   : HEALTHY
```

---

# Important Concept Check

Before moving forward, make sure this difference is clear.

### List

```python
servers = [
    "web-01",
    "app-01",
    "db-01"
]
```

We access values using an **index**:

```python
servers[0]
servers[1]
servers[2]
```

Think:

```text
          LIST

Index     Value
-----     -----
  0       web-01
  1       app-01
  2       db-01
```

### Dictionary

```python
server = {
    "hostname": "web-01",
    "cpu": 78,
    "memory": 85
}
```

We access values using a **key**:

```python
server["hostname"]
server["cpu"]
server["memory"]
```

Think:

```text
          DICTIONARY

Key             Value
-------------   -------
hostname   →    web-01
cpu        →    78
memory     →    85
```

This distinction becomes very important in DevOps because you'll eventually encounter structures like:

```python
servers = [
    {
        "hostname": "web-01",
        "cpu": 45
    },
    {
        "hostname": "web-02",
        "cpu": 87
    },
    {
        "hostname": "app-01",
        "cpu": 72
    }
]
```

Notice what happened:

```text
LIST
 │
 ├── Dictionary → web-01
 │
 ├── Dictionary → web-02
 │
 └── Dictionary → app-01
```

That's a very common structure when dealing with **AWS APIs, Kubernetes APIs, JSON, monitoring APIs, configuration data, and automation scripts**.

---

# Phase 1 — Next Topic: Loops

Now we reach one of the most useful concepts for DevOps automation.

Consider your current list:

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]
```

You could write:

```python
print(servers[0])
print(servers[1])
print(servers[2])
print(servers[3])
```

That's manageable for four servers.

But imagine you have:

```text
500 EC2 instances
```

You obviously don't want:

```python
print(servers[0])
print(servers[1])
print(servers[2])
...
print(servers[499])
```

This is where **loops** come in.

## `for` loop

We can write:

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]

for server in servers:
    print(server)
```

Output:

```text
prod-web-01
prod-web-02
prod-app-01
prod-db-01
```

Read this line as English:

```python
for server in servers:
```

means:

> For each `server` inside `servers`, perform the following action.

Internally:

```text
servers
   │
   ├── prod-web-01 ──→ server ──→ print()
   │
   ├── prod-web-02 ──→ server ──→ print()
   │
   ├── prod-app-01 ──→ server ──→ print()
   │
   └── prod-db-01 ──→ server ──→ print()
```

### DevOps example

Instead of:

```python
print(f"Checking {servers[0]}")
print(f"Checking {servers[1]}")
print(f"Checking {servers[2]}")
```

we can write:

```python
for server in servers:
    print(f"Checking server: {server}")
```

Output:

```text
Checking server: prod-web-01
Checking server: prod-web-02
Checking server: prod-app-01
Checking server: prod-db-01
```

This simple concept eventually allows you to do things like:

```text
Get all EC2 instances
        ↓
for each instance
        ↓
Check instance state
        ↓
Check tags
        ↓
Check age
        ↓
Generate report
```

That's where Python starts becoming a real **DevOps automation language**.

Next, we'll learn `for`, `range()`, `while`, `break`, `continue`, and then combine **loops + lists + dictionaries** to build a multi-server health checker.
