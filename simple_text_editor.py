file_name = input(
    'Enter the file name to open or create (with .txt extension): ')
try:
    with open(file_name, 'a+') as f:
        f.seek(0)
        read_lines = f.readlines()
        for line in read_lines:
            print(line)
        user_inputs = input(
            "Enter your text(type 'SAVE' on a new line to save and exit): ")
        content = []
        while True:
            if "SAVE" in user_inputs:
                break
            line = input(">")
            if line == "SAVE":
                f.writelines(user_inputs)
                print("Thanks for quick note!!!")
                break
            content.append(line + '\n')
except OSError as e:
    print("Error has occurred:  {e}")
