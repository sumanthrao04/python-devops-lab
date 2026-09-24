Correct. You have successfully understood the important pattern:

**List → Dictionary → `for` loop → `if/else` → health check.**

Your logic is correct. There are just a couple of coding-style improvements worth making.

### 1. `value` works, but `server` is better

You wrote:

```python
for value in Assignment_servers:
```

Python doesn't care what the variable is called, so this is valid.

But `server` explains what the variable represents:

```python
for server in assignment_servers:
```

Then:

```python
server["hostname"]
server["cpu"]
server["memory"]
server["disk"]
```

reads naturally.

This matters a lot once scripts become larger.

### 2. Use lowercase variable names

If your variable is:

```python
Assignment_servers
```

prefer:

```python
assignment_servers
```

Python normally uses `snake_case`:

```python
server_name
cpu_usage
assignment_servers
server_details
```

---

## Your loop is doing something important

Consider:

```python
for server in assignment_servers:
```

During the **first iteration**, `server` becomes:

```python
{
    "hostname": "prod-web-01",
    "cpu": 45,
    "memory": 60,
    "disk": 55
}
```

Therefore:

```python
server["hostname"]
```

returns:

```text
prod-web-01
```

and:

```python
server["cpu"]
```

returns:

```text
45
```

After your health checks finish, Python goes back to the loop.

During the **second iteration**, `server` becomes:

```python
{
    "hostname": "prod-web-02",
    "cpu": 85,
    "memory": 70,
    "disk": 65
}
```

The exact same code now checks the second server.

That's the heart of automation:

```text
                 assignment_servers
                         │
                         ▼
                     for loop
                         │
            ┌────────────┼────────────┐
            │            │            │
            ▼            ▼            ▼
         Server 1     Server 2     Server 3 ...
            │
            ▼
       Read metrics
            │
       ┌────┼────┐
       ▼    ▼    ▼
      CPU  MEM  DISK
       │    │    │
       ▼    ▼    ▼
     Check thresholds
            │
            ▼
     HEALTHY / WARNING
```

You no longer care whether there are 4 servers or 400 servers. The loop processes them.

---

# Phase 1 — Lesson 4: Functions

You're now ready for another **very important Python concept for DevOps automation**.

Look at your current code:

```python
if server["cpu"] >= 80:
    print("CPU STATUS : WARNING")
else:
    print("CPU STATUS : HEALTHY")

if server["memory"] >= 80:
    print("Memory STATUS : WARNING")
else:
    print("Memory STATUS : HEALTHY")

if server["disk"] >= 85:
    print("Disk STATUS : WARNING")
else:
    print("Disk STATUS : HEALTHY")
```

There is repetition.

Imagine a bigger script checking:

```text
CPU
Memory
Disk
Network
API
Database
Nginx
Docker
Jenkins
```

Your script could become hundreds of lines.

Functions help us organize and reuse logic.

---

## 1. What is a function?

A function is a reusable block of code that performs a particular task.

Basic syntax:

```python
def function_name():
    # code
```

Example:

```python
def greet():
    print("Hello DevOps")
```

Notice:

```python
def
```

means **define a function**.

But defining a function does **not** execute it.

You have to call it:

```python
greet()
```

Complete example:

```python
def greet():
    print("Hello DevOps")

greet()
```

Output:

```text
Hello DevOps
```

---

# 2. Why Functions?

Without a function:

```python
print("Checking server health")
print("Checking server health")
print("Checking server health")
```

With a function:

```python
def check_health():
    print("Checking server health")

check_health()
check_health()
check_health()
```

Think:

```text
             def check_health()
                    │
                    │
             Store the logic
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        Call 1    Call 2    Call 3
```

---

# 3. Function Parameters

Now let's make functions useful.

Suppose:

```python
def check_server(server):
    print(f"Checking server: {server}")
```

Call:

```python
check_server("prod-web-01")
```

Output:

```text
Checking server: prod-web-01
```

Call again:

```python
check_server("prod-db-01")
```

Output:

```text
Checking server: prod-db-01
```

The important part:

```python
def check_server(server):
```

`server` is a **parameter**.

When you call:

```python
check_server("prod-web-01")
```

`"prod-web-01"` is an **argument**.

Conceptually:

```text
check_server("prod-web-01")
             │
             │ argument
             ▼
         server parameter
             │
             ▼
print(f"Checking server: {server}")
```

---

# 4. Multiple Parameters

A function can receive multiple values.

```python
def server_info(hostname, cpu):
    print(f"Server : {hostname}")
    print(f"CPU    : {cpu}%")
```

Call:

```python
server_info("prod-web-01", 75)
```

Output:

```text
Server : prod-web-01
CPU    : 75%
```

---

# 5. Let's Convert Your CPU Logic Into a Function

Currently:

```python
if server["cpu"] >= 80:
    print("CPU STATUS : WARNING")
else:
    print("CPU STATUS : HEALTHY")
```

We could create:

```python
def check_cpu(cpu):
    if cpu >= 80:
        print("CPU STATUS : WARNING")
    else:
        print("CPU STATUS : HEALTHY")
```

Then:

```python
check_cpu(45)
check_cpu(85)
```

Output:

```text
CPU STATUS : HEALTHY
CPU STATUS : WARNING
```

Now the threshold logic exists in **one location**.

---

# 6. Understanding `return`

This is extremely important.

Instead of having the function print:

```python
def check_cpu(cpu):
    if cpu >= 80:
        print("WARNING")
    else:
        print("HEALTHY")
```

we can make it **return a value**:

```python
def check_cpu(cpu):
    if cpu >= 80:
        return "WARNING"
    else:
        return "HEALTHY"
```

Now:

```python
cpu_status = check_cpu(85)

print(cpu_status)
```

Output:

```text
WARNING
```

Think of a function as a machine:

```text
             INPUT
               │
               ▼
             CPU 85
               │
               ▼
        ┌──────────────┐
        │  check_cpu() │
        │              │
        │ cpu >= 80 ?  │
        └──────┬───────┘
               │
               ▼
             OUTPUT
               │
               ▼
           "WARNING"
```

---

# 7. `print()` vs `return`

This difference is extremely important.

### `print()`

```python
def check_cpu(cpu):
    print("WARNING")
```

This displays something.

### `return`

```python
def check_cpu(cpu):
    return "WARNING"
```

This sends the value back to whoever called the function.

Therefore:

```python
status = check_cpu(90)
```

becomes conceptually:

```python
status = "WARNING"
```

Now you can reuse `status`:

```python
print(status)
```

or:

```python
if status == "WARNING":
    print("Send alert")
```

That's why `return` becomes more powerful for real automation.

---

# 8. One Reusable Health Function

Look at something interesting.

Your CPU threshold:

```text
80
```

Memory threshold:

```text
80
```

Disk threshold:

```text
85
```

Instead of creating:

```python
check_cpu()
check_memory()
check_disk()
```

we can create **one generic function**:

```python
def check_health(usage, threshold):

    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"
```

Now:

```python
cpu_status = check_health(45, 80)
memory_status = check_health(85, 80)
disk_status = check_health(67, 85)
```

Results:

```text
cpu_status     → HEALTHY
memory_status  → WARNING
disk_status    → HEALTHY
```

This is a major improvement.

Instead of writing the same `if/else` three times, we wrote it **once**.

---

# Assignment 4 — Refactor Your Health Checker Using Functions

Use the same server data from Assignment 3.

Create:

```text
08_function_health_check.py
```

Create this function:

```python
def check_health(usage, threshold):
```

Inside it:

```text
usage >= threshold
        ↓
     WARNING

otherwise
        ↓
     HEALTHY
```

Then your loop should calculate:

```text
CPU status
Memory status
Disk status
```

by calling your function.

Your output should still look like:

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
```

But this time you **must not write** three separate blocks like:

```python
if cpu >= 80:
    ...
else:
    ...

if memory >= 80:
    ...
else:
    ...

if disk >= 85:
    ...
else:
    ...
```

The `if/else` threshold logic should exist **only once**, inside:

```python
def check_health(usage, threshold):
```

Then call that function from your loop.

This assignment is important because you're moving from simply writing working Python to writing **reusable automation code**.


Good attempt. You have understood the **main purpose of the assignment**: putting the health-check logic inside a reusable function and calling it for every server.

There are **two things to correct** and one important concept to understand before we continue.

## 1. Your `check_health()` function is correct

You wrote:

```python
def check_health(usage, threshold):
    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"
```

This is exactly what we wanted.

For example:

```python
check_health(45, 80)
```

Python evaluates:

```text
usage     = 45
threshold = 80

45 >= 80
   ↓
False
   ↓
HEALTHY
```

And:

```python
check_health(91, 85)
```

becomes:

```text
91 >= 85
   ↓
True
   ↓
WARNING
```

So you've understood **parameters + arguments + return values** correctly.

---

# 2. Thresholds need correction

You currently have:

```python
print(cpustatus(), check_health(server["cpu"], 85))
print(memorystatus(), check_health(server["memory"], 85))
print(diskstatus(), check_health(server["disk"], 85))
```

You're passing `85` for everything.

Our requirements were:

```text
CPU     >= 80 → WARNING
Memory  >= 80 → WARNING
Disk    >= 85 → WARNING
```

So it should be:

```python
print(cpustatus(), check_health(server["cpu"], 80))
print(memorystatus(), check_health(server["memory"], 80))
print(diskstatus(), check_health(server["disk"], 85))
```

This shows why the second parameter is useful.

Same function:

```python
check_health()
```

Different thresholds:

```text
                  check_health()
                        │
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
       CPU 45        Memory 85      Disk 67
       Limit 80      Limit 80       Limit 85
          ↓             ↓             ↓
       HEALTHY        WARNING        HEALTHY
```

---

# 3. You don't need these three functions

You created:

```python
def cpustatus():
    return "CPU STATUS    : "

def memorystatus():
    return "MEMORY STATUS : "

def diskstatus():
    return "DISK STATUS   : "
```

Technically, they work.

But they don't provide much benefit because each function simply returns fixed text.

For example:

```python
def cpustatus():
    return "CPU STATUS : "
```

Calling:

```python
cpustatus()
```

will **always** return:

```text
CPU STATUS :
```

There's no calculation or reusable behavior happening.

You can simply write:

```python
print("CPU STATUS    :", check_health(server["cpu"], 80))
print("MEMORY STATUS :", check_health(server["memory"], 80))
print("DISK STATUS   :", check_health(server["disk"], 85))
```

That's cleaner.

This is an important programming lesson:

> Don't create a function just because you can. Create one when it encapsulates useful/reusable behavior.

---

# Cleaner version of your solution

Your program can be simplified to:

```python
def check_health(usage, threshold):
    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"


print("========= MULTI SERVER HEALTH CHECK =========")

for server in Assignment_servers:

    print(f"Server : {server['hostname']}")
    print(f"CPU    : {server['cpu']}%")
    print(f"Memory : {server['memory']}%")
    print(f"Disk   : {server['disk']}%")

    print()

    print("CPU STATUS    :", check_health(server["cpu"], 80))
    print("MEMORY STATUS :", check_health(server["memory"], 80))
    print("DISK STATUS   :", check_health(server["disk"], 85))

    print()
    print("--------------------------------------------")
```

Notice how much cleaner it is.

---

# 4. Very Important: Understand What Happens During This Call

Take this:

```python
check_health(server["memory"], 80)
```

Suppose the current server is:

```python
server = {
    "hostname": "prod-app-01",
    "cpu": 65,
    "memory": 88,
    "disk": 70
}
```

First Python evaluates:

```python
server["memory"]
```

which gives:

```text
88
```

So effectively the call becomes:

```python
check_health(88, 80)
```

Python enters:

```python
def check_health(usage, threshold):
```

and assigns:

```text
usage     = 88
threshold = 80
```

Then:

```python
if usage >= threshold:
```

becomes:

```text
88 >= 80
```

which is `True`.

Therefore:

```python
return "WARNING"
```

So this:

```python
print("MEMORY STATUS :", check_health(server["memory"], 80))
```

effectively becomes:

```python
print("MEMORY STATUS :", "WARNING")
```

Output:

```text
MEMORY STATUS : WARNING
```

Understanding this flow is more important than memorizing the syntax.

---

# 5. Small Improvement to the Function

You currently have:

```python
return("WARNING")
```

That's valid Python.

But normally we'd write:

```python
return "WARNING"
```

because `return` doesn't require parentheses.

So:

```python
def check_health(usage, threshold):
    if usage >= threshold:
        return "WARNING"
    else:
        return "HEALTHY"
```

is preferred.

---

# What You've Learned So Far

You've already covered a surprisingly useful foundation:

```text
Python Fundamentals
       │
       ├── Variables
       ├── str / int / float / bool
       ├── input()
       ├── f-strings
       ├── if / elif / else
       │
       ├── Collections
       │     ├── List
       │     ├── Tuple
       │     ├── Set
       │     └── Dictionary
       │
       ├── Loops
       │     ├── for
       │     ├── range()
       │     ├── while
       │     ├── break
       │     └── continue
       │
       └── Functions
             ├── def
             ├── parameters
             ├── arguments
             └── return
```

And you're already combining them:

```text
List of servers
      ↓
for loop
      ↓
Dictionary for each server
      ↓
Extract CPU/Memory/Disk
      ↓
Function
      ↓
if/else threshold check
      ↓
return status
      ↓
Print result
```

That's a solid base.

## Next: Phase 1 — Lesson 5

Next we'll cover **modules, imports, and exception handling**.

Exception handling is particularly important for DevOps because real automation fails:

```text
Server unreachable
File doesn't exist
API returns 500
Invalid JSON
AWS authentication fails
Command fails
User enters invalid data
```

Instead of letting your Python script crash, we'll learn:

```python
try:
    # operation

except:
    # handle failure
```

We'll build a small **safe DevOps health-check script** where invalid CPU/memory/disk input doesn't crash the program.
