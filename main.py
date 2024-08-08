import itertools

def generate_passwords(elements):
    all_passwords = set()
    
    for i in range(1, len(elements) + 1):
        for combination in itertools.permutations(elements, i):
            password = ''.join(combination)
            all_passwords.add(password)
    
    return sorted(all_passwords)

def main():
    print("I am a PasswordList Maker")
    input_data = input("Enter Info ("123" or "123, ahmed" : ")
    elements = [e.strip() for e in input_data.split(',')]

    passwords = generate_passwords(elements)
    
    with open('password_list.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    
    print("Done, the file name is : 'password_list.txt'.")

if __name__ == "__main__":
    main()