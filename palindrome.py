def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    return input_str == input_str[::-1]

while True:
    choice = input("Enter '1' to check, '2' to quit: ")
    
    if choice == '2':
        print("Goodbye!")
        break
    
    input_str = input("Enter a number or a string: ")
    
    if is_palindrome(input_str):
        print(f'"{input_str}" is a palindrome!')
    else:
        print(f'"{input_str}" is not a palindrome.')
