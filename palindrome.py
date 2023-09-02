def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    return input_str == input_str[::-1]

while True:
    choice = input("Enter '1' to check a number, '2' for a string, or '3' to quit: ")
    
    if choice == '3':
        print("Goodbye!")
        break
    
    input_str = input("Enter a number or a string: ")
    
    if choice == '1':
        if input_str.isdigit() and is_palindrome(input_str):
            print(f"{input_str} is a palindrome!")
        else:
            print(f"{input_str} is not a palindrome.")
    
    elif choice == '2':
        if is_palindrome(input_str):
            print(f'"{input_str}" is a palindrome!')
        else:
            print(f'"{input_str}" is not a palindrome.')
    
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
