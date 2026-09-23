# Phase 1 — Lesson 3: Loops for DevOps

Now we'll learn one of the most important concepts for automation: **loops**.

The basic idea is simple:

> A loop allows Python to repeat an operation automatically.

For DevOps, this is extremely useful because we frequently work with multiple servers, containers, pods, files, users, AWS resources, logs, etc.

---

## 1. Why Do We Need Loops?

Suppose you have four servers:

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]
```

Without a loop:

```python
print(servers[0])
print(servers[1])
print(servers[2])
print(servers[3])
```

With a loop:

```python
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

This becomes extremely valuable when there are 10, 100, or 1,000 resources.

---

# 2. Understanding `for`

Look carefully at:

```python
for server in servers:
    print(server)
```

There are two different variables here:

```text
servers → Complete list
server  → One item from the list
```

Python essentially performs:

```text
servers
   │
   ├── prod-web-01
   │        ↓
   │   server = "prod-web-01"
   │        ↓
   │     print()
   │
   ├── prod-web-02
   │        ↓
   │   server = "prod-web-02"
   │        ↓
   │     print()
   │
   ├── prod-app-01
   │        ↓
   │   server = "prod-app-01"
   │        ↓
   │     print()
   │
   └── prod-db-01
            ↓
       server = "prod-db-01"
            ↓
          print()
```

The variable name `server` isn't special.

This works:

```python
for x in servers:
    print(x)
```

But:

```python
for server in servers:
```

is easier to understand.

Good variable names matter.

---

# 3. DevOps Example

Try:

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-app-01",
    "prod-db-01"
]

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

We can perform multiple operations:

```python
for server in servers:
    print(f"Connecting to {server}")
    print(f"Checking health of {server}")
    print("Health check completed")
    print()
```

The indentation tells Python which statements belong to the loop.

---

# 4. Loop + `if`

This is where it gets more useful.

Suppose:

```python
cpu_usage = [45, 82, 65, 91]
```

We can check every value:

```python
for cpu in cpu_usage:

    if cpu >= 80:
        print(f"CPU {cpu}% : WARNING")
    else:
        print(f"CPU {cpu}% : HEALTHY")
```

Output:

```text
CPU 45% : HEALTHY
CPU 82% : WARNING
CPU 65% : HEALTHY
CPU 91% : WARNING
```

Notice what we're doing:

```text
List
 ↓
Loop
 ↓
Take one value
 ↓
if/else
 ↓
Make decision
 ↓
Next value
```

This pattern is fundamental to automation.

---

# 5. `range()`

Sometimes you don't have a list. You simply want something to run multiple times.

Example:

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

Important:

```python
range(5)
```

means:

```text
0
1
2
3
4
```

It stops **before 5**.

---

## Starting From 1

Use:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

Think:

```text
range(start, stop)
```

The `stop` value isn't included.

For example:

```python
range(1, 5)
```

produces:

```text
1
2
3
4
```

---

# 6. `range()` With Step

You can also provide:

```text
range(start, stop, step)
```

Example:

```python
for number in range(0, 11, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
10
```

Here:

```text
start = 0
stop  = 11
step  = 2
```

---

# 7. Looping Through a Dictionary

You already created:

```python
server_details = {
    "hostname": "prod-app-01",
    "environment": "production",
    "cpu": 78,
    "memory": 85,
    "disk": 67
}
```

You can loop through it.

### Keys

```python
for key in server_details:
    print(key)
```

Output:

```text
hostname
environment
cpu
memory
disk
```

---

## Values

Use:

```python
for value in server_details.values():
    print(value)
```

Output:

```text
prod-app-01
production
78
85
67
```

---

## Keys + Values

This is the most useful:

```python
for key, value in server_details.items():
    print(f"{key} : {value}")
```

Output:

```text
hostname : prod-app-01
environment : production
cpu : 78
memory : 85
disk : 67
```

Remember:

```python
.items()
```

gives us:

```text
key + value
```

---

# 8. Very Important: List of Dictionaries

Now we're going to combine the concepts you've learned.

Instead of having one server:

```python
server = {
    "hostname": "web-01",
    "cpu": 45
}
```

we can have multiple servers:

```python
servers = [
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
```

Look at the structure:

```text
servers
   │
   │ LIST
   │
   ├── Dictionary
   │      hostname → prod-web-01
   │      cpu      → 45
   │
   ├── Dictionary
   │      hostname → prod-web-02
   │      cpu      → 82
   │
   └── Dictionary
          hostname → prod-app-01
          cpu      → 91
```

This structure is extremely important.

You'll see similar structures when working with JSON, REST APIs, AWS Boto3, Kubernetes APIs, monitoring APIs, etc.

---

# 9. Loop Through Multiple Servers

Now:

```python
servers = [
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

for server in servers:
    print(server["hostname"])
```

Output:

```text
prod-web-01
prod-web-02
prod-app-01
```

Why?

First iteration:

```python
server = {
    "hostname": "prod-web-01",
    "cpu": 45
}
```

Therefore:

```python
server["hostname"]
```

is:

```text
prod-web-01
```

Second iteration:

```python
server = {
    "hostname": "prod-web-02",
    "cpu": 82
}
```

And so on.

---

# 10. Add Health-Check Logic

Now combine:

* list
* dictionary
* loop
* condition

```python
servers = [
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

for server in servers:

    print(f"Server: {server['hostname']}")
    print(f"CPU   : {server['cpu']}%")

    if server["cpu"] >= 80:
        print("Status: WARNING")
    else:
        print("Status: HEALTHY")

    print()
```

Output:

```text
Server: prod-web-01
CPU   : 45%
Status: HEALTHY

Server: prod-web-02
CPU   : 82%
Status: WARNING

Server: prod-app-01
CPU   : 91%
Status: WARNING
```

You have now moved from checking **one server** to checking **multiple servers automatically**.

---

# 11. `continue`

Sometimes we want to skip something.

Imagine:

```python
servers = [
    "prod-web-01",
    "maintenance-server",
    "prod-app-01"
]
```

We don't want to check the maintenance server.

```python
for server in servers:

    if server == "maintenance-server":
        continue

    print(f"Checking {server}")
```

Output:

```text
Checking prod-web-01
Checking prod-app-01
```

Think:

```text
continue
   ↓
Skip current iteration
   ↓
Move to next item
```

---

# 12. `break`

`break` completely stops the loop.

```python
servers = [
    "prod-web-01",
    "prod-web-02",
    "prod-db-01",
    "prod-app-01"
]

for server in servers:

    if server == "prod-db-01":
        break

    print(f"Checking {server}")
```

Output:

```text
Checking prod-web-01
Checking prod-web-02
```

Once Python finds:

```text
prod-db-01
```

it stops.

Difference:

```text
continue
    ↓
Skip this item
    ↓
Continue loop


break
    ↓
Stop entire loop
```

---

# 13. `while` Loop

There's another type of loop:

```python
while
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

Output:

```text
1
2
3
4
5
```

Execution:

```text
count = 1

1 <= 5 → True → print 1
count becomes 2

2 <= 5 → True → print 2
count becomes 3

...

6 <= 5 → False

STOP
```

Be careful with `while`.

This is dangerous:

```python
count = 1

while count <= 5:
    print(count)
```

`count` never changes.

So Python keeps running:

```text
1
1
1
1
1
1
1
...
```

That's called an **infinite loop**.

For DevOps automation, you'll generally use `for` much more frequently when iterating over known collections.

---

# Assignment 3 — Multi-Server Health Checker

Now build something more interesting.

Create:

```text
07_multi_server_health.py
```

Create this data:

```python
servers = [
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
```

Don't modify this data.

Your job is to use **one `for` loop** to process all four servers.

Rules:

```text
CPU >= 80       → WARNING
Memory >= 80    → WARNING
Disk >= 85      → WARNING
```

Expected output:

```text
========= MULTI SERVER HEALTH CHECK =========

Server : prod-web-01
CPU    : 45%
Memory : 60%
Disk   : 55%

CPU STATUS    : HEALTHY
MEMORY STATUS : HEALTHY
DISK STATUS   : HEALTHY

--------------------------------------------

Server : prod-web-02
CPU    : 85%
Memory : 70%
Disk   : 65%

CPU STATUS    : WARNING
MEMORY STATUS : HEALTHY
DISK STATUS   : HEALTHY

--------------------------------------------

Server : prod-app-01
CPU    : 65%
Memory : 88%
Disk   : 70%

CPU STATUS    : HEALTHY
MEMORY STATUS : WARNING
DISK STATUS   : HEALTHY

--------------------------------------------

Server : prod-db-01
CPU    : 55%
Memory : 65%
Disk   : 92%

CPU STATUS    : HEALTHY
MEMORY STATUS : HEALTHY
DISK STATUS   : WARNING

--------------------------------------------
```

### Restrictions

Try solving it using only what you've learned:

```text
List
Dictionary
for loop
if/else
f-string
print()
```

The main thing I want you to figure out yourself is:

```python
for ????? in servers:
```

and then how to access:

```text
hostname
cpu
memory
disk
```

from the current dictionary.

Don't use functions yet.

Send me your **code and output**. After reviewing it, we'll move to **functions**, which will allow us to stop repeating the CPU/Memory/Disk health-check logic and start structuring the code like a proper automation script.
