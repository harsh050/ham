import hashlib
def crackHash(hash_to_crack):
    try:
        with open('path/to/passwords.txt', 'r') as passfile:
            for password in passfile:
                password = password.strip()  # Remove any newline characters
                # Code to check the password
                print(password)  # Example placeholder
    except FileNotFoundError:
        print("Password file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example call
crackHash('a9046c73e00331af68917d3804f70655')
