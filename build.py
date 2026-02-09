import os

os.makedirs("dist", exist_ok=True)

with open("dist/output.txt", "w") as f:
    f.write("Hello CI Pipeline - Build Successful")
