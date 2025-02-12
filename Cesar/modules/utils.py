from cesar import encrypt, decrypt

# Function to Check if key is valid
def check_key(key):
    if key in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
               '19', '20', '21', '22', '23', '24', '25']:
        return False
    else:
        return True

# Function to return the object file
def openfile(filename):
    try:
        with open(filename) as f:
            file = f.readlines()
            return  file
    except FileNotFoundError:
        print("File not foun error!")

# Function to encrypt and save file in another txt file
def encrypt_file (filename, new_file_name='file.txt'):
    for line in filename:
        try:
            with open(new_file_name, 'a') as f:
                f.write(f"{encrypt(line)}\n")
        except FileNotFoundError:
            continue

