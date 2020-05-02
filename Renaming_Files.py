import os

os.chdir("E:\\Coding_Projects\\Renaming\\New folder\\")

print(os.getcwd())

def main():
    i=1
    path = "E:\\Coding_Projects\\Renaming\\New folder\\"
    print(len(os.listdir()))
    l=(len(os.listdir()))
    # Print all the current file names
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            dest = ("Image"+str(i)+".jpg")
            source = filename
            dest =  dest
            os.rename(source, dest)
        i+=1

if __name__ == '__main__':
   main()
