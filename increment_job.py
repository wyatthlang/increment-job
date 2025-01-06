import os
import uuid
import subprocess
import random

def writeAndCommitRandomUUID():
  # Define the file name
  file_name = "README.md"

  try:
    # Step 1: Clear or create the file
    open(file_name, "w").close()  # This erases any existing content
    print(f"File '{file_name}' has been cleared or created.")

    # Step 2: Generate a random UUID and write it to the file
    random_uuid = str(uuid.uuid4())
    with open(file_name, "w") as file:
        file.write(random_uuid)
    print(f"File '{file_name}' created and written successfully.")

    # Step 3: Read and verify the content
    with open(file_name, "r") as file:
        content = file.read()
    print(f"Content of the file: {content.strip()}")

    # Step 4: Add the file to Git, commit it, and push it to the remote repository
    commit_message = random_uuid

    subprocess.run(["git", "add", file_name], check=True)
    subprocess.run(["git", "commit", "-m", commit_message], check=True)
    subprocess.run(["git", "push"], check=True)
    print(f"File '{file_name}' committed and pushed to the remote repository.")

  except Exception as e:
    print(f"An error occurred: {e}")


random_integer = random.randint(1, 20)
print(f"Writing and committing {random_integer} random UUIDs to git repo")

for i in range(random_integer):
  writeAndCommitRandomUUID()