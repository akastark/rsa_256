
from math import gcd, pow, fmod


class RSAClass:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.n = 0
        self.totient = 0
        self.d = 0
        self.private_key = 0
        self.message = 0
        self.encrypted_message = 0
        self.decrypted_message = 0

    def get_n(self):
        return self.n

    def get_d(self):
        return self.d

    def get_totient(self):
        return self.totient

    def set_message(self, message):
        self.message = message

    def get_encrypted_message(self):
        return self.encrypt_message

    def set_encrypted_message(self, message):
        self.encrypt_message = message

    def get_decrypted_message(self):
        return self.decrypt_message

    def set_decrypted_message(self, message):
        self.decrypt_message = message

    def calculate_n(self):
        self.n = self.p*self.q

    def calculate_totient(self):
        self.totient = (self.p - 1)*(self.q - 1)


    def calculate_d(self, k):
        self.d = (1 + (k*self.totient))/self.e

    def generate_private_key(self):
        d = 0

        while((d*self.e)%self.totient) != 1:
            d += 1

        self.private_key = d



    #encrypt a defined message
    def encrypt_message(self):
        en = pow(self.message, self.e)
        encrypted_message = en % self.n

        self.set_encrypted_message(encrypted_message)


    #decrypt an encrypted message
    def decrypt_message(self):

        self.calculate_d(2)
        decrypted_message = pow(self.get_encrypted_message(), self.get_d())
        decrypted_message = fmod(decrypted_message, self.n)

        self.set_decrypted_message(decrypted_message)




def main():

    p = 3
    q = 7
    e = 5


    RSA = RSAClass(p, q, e)
    RSA.set_message("teste")
    RSA.calculate_totient()
    RSA.calculate_n()

    RSA.encrypt_message()

    print(RSA.get_encrypted_message(RSA.message.encode()))

    RSA.decrypt_message()

    print(RSA.get_decrypted_message())

    print(RSA.get_n())
    print(RSA.get_totient())
    print(RSA.get_d())


if __name__ == "__main__":
    main()