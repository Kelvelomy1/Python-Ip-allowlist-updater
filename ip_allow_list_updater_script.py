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