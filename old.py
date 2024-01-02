import sys

from cryptography.hazmat.primitives.serialization import pkcs12


def crack_password(file_path, guess, iterations):
    try:
        file = pkcs12.load_pkcs12(open(file_path, 'rb').read(), guess.encode('utf8'))
    except ValueError:
        file = None

    if file:
        print('Password cracked after {} attempts.'.format(str(iterations)))
        print("Password is: {}".format(guess))

        # Write the found key to key.txt
        with open('key.txt', 'a') as key_file:
            key_file.write(guess + '\n')

        return True
    else:
        return False

def run_brute_force(file_path):
    print('\nStarting Brute force...\n')

    iterations = 0
    for guess_num in range(1000, 10000):
        guess = str(guess_num)

        if crack_password(file_path, guess, iterations):
            return

        iterations += 1
        # Log progress every 20000 attempts
        if iterations % 20000 == 0:
            log_progress(iterations, guess)

    print('Key not found.\n')
    log_progress(iterations, guess)

def log_progress(iterations, guess):
    print('Progress: Attempt #{}, Latest guess: {}.'.format(iterations, guess))

def main():
    file_path = ""
    if len(sys.argv) > 2 and sys.argv[1] == "-p":
        file_path = sys.argv[2]
    else:
        print('Error: Please provide a valid path')
        sys.exit(0)

    run_brute_force(file_path)

if __name__ == "__main__":
    main()
