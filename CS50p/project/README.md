# Passwords Generator
#### Video Demo:  https://youtu.be/OnsFcNs_RUk
#### Description:
My CS50P Final Project is a password generator. It generates how many passwords you want and how long you want it to be. Minimum length should be 8 characters to prevent user of having a weak password.

O meu projeto final de CS50P é um gerador de senhas. Ele gera quantas senhas o usuário quiser e quão longo o mesmo preferir. A quantidade mínima de caracteres deve ser 8, para previnir o usuário de ter uma senha fraca.

## project.py:
    def main(): It takes all functions. Loops over the generate function to generate more than one password, and prints all passwords generated.

    def get_amount(): It asks user to input how many passwords does them want to generate. Using a while loop and try and except it reprompts if input is not a positive integer.

    def get_length(): It asks user to input the length of each password. Using a while loop and try and except it reprompts if input less than 8, to guarantee a strong password.

    def get_chars(): A list with every ASCII alphanumeric and symbol character.

    def generate(n, l): It generates user's amount of passwords, input's X characters each using the random module. Using a for loop for the amount of passwords, creating a variable for passwords, and then another for loop for the length of each password, generating a random character (using the list of get_chars() function) and adding to the variable passwords.

## test_project.py:
    def test_get_chars(): It tests list of characters.

## requirements.txt:
    It lists extra libraries I used, in this case, the random module.

