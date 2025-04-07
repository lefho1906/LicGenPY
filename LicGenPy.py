#get_computer_id

import platform
import uuid
import os

def get_computer_id():
    # Get the computer's hardware and software information
    node = platform.node()  # Hostname
    system = platform.system()
    machine = platform.machine()
    processor = platform.processor()

    # Concatenate the information to create a unique identifier
    computer_id = f"{node}-{system}-{machine}-{processor}"

    # Generate a UUID based on the identifier
    unique_id = str(uuid.uuid3(uuid.NAMESPACE_OID, computer_id))

    return unique_id

# Get and print the computer ID
computer_id = get_computer_id()
print("Computer ID:", computer_id)
print("Computer Name:", platform.node())

# Define the file path
file_path = "C:\\ProgramData\\<projeto>\\scripts\\"+platform.node()+"_licensepy.txt"

# Write the computer ID to the file
with open(file_path, "w") as file:
    file.write(computer_id+"_"+platform.node())

print(f"Computer ID has been written to {file_path}")