import sys

from cryptography.hazmat.primitives.serialization import pkcs12


class BruteforceCracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.iterations = 0

    def crack_password(self, guess: str):
        try:
            file = pkcs12.load_pkcs12(open(self.file_path, 'rb').read(), guess.encode('utf8'))
        except ValueError:
            file = None

        if file:
            print('Password cracked after {} attempts.'.format(str(self.iterations)))
            print("Password is: {}".format(guess))

            # Write the found key to key.txt
            with open('key.txt', 'a') as key_file:
                key_file.write(guess + '\n')

            return True
        else:
            return False

    def run_brute_force(self):
        print('\nStarting Brute force...\n')

        for guess_num in range(1000, 200000000):
            guess = str(guess_num)

            if self.crack_password(guess):
                return

            self.iterations += 1
            # Log progress every 20000 attempts
            if self.iterations % 20000 == 0:
                self.log_progress(guess)

        print('Key not found.\n')
        self.log_progress(guess)

    def log_progress(self, guess):
        print('Progress: Attempt #{}, Latest guess: {}.'.format(self.iterations, guess))


def main():
    file_path = ""
    if len(sys.argv) > 2 and sys.argv[1] == "-p":
        file_path = sys.argv[2]
    else:
        print('Error: Please provide a valid path')
        sys.exit(0)

    cracker = BruteforceCracker(file_path)
    cracker.run_brute_force()


if __name__ == "__main__":
    main()
