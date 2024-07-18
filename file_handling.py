def main():
 try:
        with open("my_file.txt","w") as file:
         file.write("I am yunis\n")
         file.write("am pursuing python programming\n")
         file. write("my contact is 562345098\n")

        with open("my_file.txt", "r") as file:
          contents = file.read()
        print("Contents of my_file.txt:")
        print(contents) 

        with open("my_file.txt", "a") as file:
            file.write("learning from plp academy\n")
            file.write("specializing with python\n")
            file.write("cohort 2\n")

        with open("my_file.txt", "r") as file:
         contents = file.read()
        print("Updated contents of my_file.txt:")
        print(contents)

 except FileNotFoundError:
        print("File not found error occurred.")

 except PermissionError:
        print("Permission error occurred. Check file permissions.")

 except Exception as e:
        print("An error occurred:", str(e))

 finally:
        print("Execution completed.")
         
if __name__ == "__main__":
                 main()