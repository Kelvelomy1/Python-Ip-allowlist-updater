# Automating File Updates with a Python Security Algorithm

## Project Overview

In healthcare cybersecurity, protecting personal patient records requires strict access control. Access to restricted subnetworks is managed using an allow list stored in a text file (`allow_list.txt`), which records authorized employee IP addresses. When employees change roles or leave the organization, their IP addresses are placed on a separate `remove_list` and must be revoked promptly.

To eliminate manual errors and save time, I developed a Python algorithm that automatically reads the allow list, identifies any unauthorized IP addresses present on the remove list, removes them, and overwrites the file with the updated list of authorized addresses.

---

## Repository Structure

* `update_allow_list.py` — The main Python script that automates reading, filtering, and updating the IP allow list.
* `allow_list.txt` — Sample text file containing authorized and unauthorized IP addresses for testing.
* `README.md` — Project documentation and technical breakdown of the Python methods used.

---

## Complete Python Algorithm

```python
# Define the file name and the list of IP addresses to revoke
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Step 1: Open and read the initial allow list file
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Step 2: Convert the string of IP addresses into a list
ip_addresses = ip_addresses.split()

# Step 3: Iterate through the remove list and revoke matching IP addresses
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Step 4: Convert the updated list back into a string separated by newlines
ip_addresses = "\n".join(ip_addresses)

# Step 5: Overwrite the original allow list file with the revised string
with open(import_file, "w") as file:
    file.write(ip_addresses)

# Step 6: Verify the updated file contents
with open(import_file, "r") as file:
    text = file.read()
print(text)
```

---

## Step-by-Step Code Breakdown & Technical Explanations

### 1. Opening and Reading the Allow List (`with`, `open()`, and `.read()`)

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    ip_addresses = file.read()
```

* **`import_file` variable:** Stores the string `"allow_list.txt"` so the file name can be referenced cleanly throughout the script.
* **`with` statement:** Acts as a context manager that handles system resources safely. Once Python finishes executing the indented code inside the `with` block, it automatically closes the file, preventing memory leaks or file corruption.
* **`open()` function:** Takes two arguments here—the file name (`import_file`) and the mode (`"r"`). The `"r"` argument opens the file in **read-only mode**, allowing the program to inspect its contents without accidentally altering them. The `as file` clause assigns the opened file object to the temporary variable `file`.
* **`.read()` method:** Called on the `file` object to extract the entire contents of `allow_list.txt` as a single continuous string, which is then stored in the `ip_addresses` variable.

---

### 2. Converting the String into a List (`.split()`)

```python
ip_addresses = ip_addresses.split()
```

* **`.split()` method:** Because strings are immutable and cannot easily have individual IP addresses deleted from them, `.split()` converts the `ip_addresses` string into a Python **list**. By default, `.split()` separates the string wherever whitespace (spaces, tabs, or newlines) occurs, turning each individual IP address into a distinct list element. The resulting list is reassigned back to `ip_addresses`.

---

### 3. Checking and Removing Unauthorized IPs (`for`, `if`, and `.remove()`)

```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```

* **`for` loop:** Repeats a block of code for every item in a sequence. Here, `for element in remove_list:` iterates through each IP address in `remove_list` one by one, temporarily assigning the current IP address to the loop variable `element`.
* **`if` statement:** Evaluates a condition (`element in ip_addresses`) before executing the code beneath it. Checking whether the IP exists in `ip_addresses` first is a critical safeguard—if `.remove()` is called on an item that is not in the list, Python will raise a `ValueError` and crash the script.
* **`.remove()` method:** Deletes the first matching occurrence of `element` directly from the `ip_addresses` list. Because `allow_list.txt` contains unique IP addresses, removing the match ensures that unauthorized access is revoked.

---

### 4. Reformatting and Overwriting the File (`.join()`, `.write()`, and `print()`)

```python
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)

with open(import_file, "r") as file:
    text = file.read()
print(text)
```

* **`.join()` method:** Functions as the reverse of `.split()`. Because files can only be written using string data, `"\n".join(ip_addresses)` combines every IP address in the updated list back into a single string, inserting a newline character (`\n`) between each address so they appear on separate lines.
* **`open(import_file, "w")`:** Reopens `allow_list.txt` using the `"w"` (**write**) mode. Unlike read mode, write mode erases the existing contents of the file so it can be replaced with fresh data.
* **`.write()` method:** Takes the reformatted `ip_addresses` string and writes it directly into `allow_list.txt`, permanently saving the updated access list.
* **`print()` function:** Displays output directly to the console. Re-reading the file into `text` and calling `print(text)` provides immediate visual confirmation that the revoked IP addresses are gone and the file formatting remains intact.

---

## Summary

This project demonstrates how Python automates routine cybersecurity access-control tasks. By combining `with` and `open()` for safe file handling, `.read()` and `.split()` to parse raw text into a structured list, a `for` loop with an `if` check and `.remove()` to filter out unauthorized IP addresses, and `.join()` with `.write()` to update the file, the algorithm reliably maintains network security while eliminating manual administrative overhead.