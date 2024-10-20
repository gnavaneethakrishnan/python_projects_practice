import os


def is_valid_filename(filename):
    if not filename.endswith('.txt'):
        return False
    if '..' in filename or '/' in filename or '\\' in filename:
        return False
    return True


def read_file(name):
    if not is_valid_filename(name):
        print("Invalid file name")
        return []
    try:
        with open(name, 'r') as f:
            read_lines = f.readlines()
            for line in read_lines:
                print(line, end="")
            return read_lines

    except FileNotFoundError:
        print("Creating a new file")
        with open(name, 'w'):
            pass
        return []
    except OSError as e:
        print(f"Error has occurred:  {e}")
        return []


def write_to_file(name, content, mode):
    if not is_valid_filename(name):
        print("Invalid file name")
    try:
        with open(name, mode) as f:
            f.writelines(content)
            print(f"{name} is save..!!!")
    except OSError as e:
        print(f"Error has occurred: {e}")


def write_or_append(name):
    new_content = []
    while True:
        line = input()
        if line == "SAVE":
            print("Do you want to overwrite existing content or append to it")
            print("1. overwrite")
            print("2. append")
            try:
                user_choice = int(
                    input("Enter the corresponding number: ").strip())
                if user_choice not in [1, 2]:
                    print("Invalid Choice. Please enter 1 or 2")
                    continue
                mode = 'w' if user_choice == 1 else 'a+'
                write_to_file(name, new_content, mode)
                break
            except ValueError:
                print("Invalid input. Please enter a number")
            except OSError as e:
                print("Error has occurred:  {e}")

        new_content.append(line + '\n')


def find_and_replace(file_name):
    lines = read_file(file_name)
    if not lines:
        print("The file is empty or does not exist")
        return
    word = input("find: ").strip()
    while True:
        if not word:
            print("The find word cannot be empty. Please enter a valid word")
            continue
        replacement = (input("replace: ")).strip()
        break
    lines = [line.replace(word, replacement) for line in lines]
    write_to_file(file_name, lines, 'w')


def main():
    file_name = input(
        'Enter the file name to open or create (with .txt extension): ')
    if not is_valid_filename(file_name):
        print("Invalid file name")
        return
    read_file(file_name)
    print("Enter your text(type 'SAVE' on a new line to save and exit): ")
    write_or_append(file_name)
    find_and_replace(file_name)


if __name__ == "__main__":
    main()
