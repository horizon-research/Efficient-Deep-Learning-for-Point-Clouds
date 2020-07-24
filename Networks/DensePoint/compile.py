import os

os.system("pwd")

print ("Making directory for compiling: ")
os.system ("mkdir -p build")
print ("Done!")

print("Compiling pointnet2.so for DensePoint: ")
os.system ("cd build; cmake ..; make")
print ("Done!")

print ("Copying pointnet2.so for baseline version: ")
os.system ("cp -r utils/_ext/ utils-baseline/")
print ("Done!")
