from Generator_Package.generator import generate_password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_mixed_case = input("Include mixed case letters? (y/n): ").lower() == 'y'

    generated_password = generate_password(
        length=password_length,
        use_special=include_special,
        use_numbers=include_numbers,
        use_mixed_case=include_mixed_case
    )

    print(f"Generated Password: {generated_password}")
