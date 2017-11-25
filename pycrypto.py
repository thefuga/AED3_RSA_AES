from Crypto.PublicKey import RSA
import gmpy2

public_key = RSA.importKey("""-----BEGIN PUBLIC KEY-----
MEEwDQYJKoZIhvcNAQEBBQADMAAwLQImDlsTjeFVTgo4BAs9/Ex5xUU6iWNoBDY8
J7tuuv7INMmMOgYoIFUCAwEAAQ==
-----END PUBLIC KEY-----""")
n = int(public_key.n)
e = int(public_key.e)
p = 1332830227949273521465367319234277279439624789
q = 1371293089587387292180481293784036793076837889
d = int(gmpy2.invert(e,(p-1)*(q-1)))
private_key = RSA.construct((n, e, d))

private_key_file = open('private.pem', 'wb')
private_key_file.write(private_key.exportKey())
private_key_file.close()


##Utilizado apenas para propósito de testes!!!

cipher = open('key.cipher', 'rb')
encrypted_message = cipher.read()
cipher.close()
decrypted_message = private_key.decrypt(encrypted_message)
print(decrypted_message)
signature = private_key.sign(decrypted_message, '')
public_key.verify(decrypted_message, signature)
secret = public_key.encrypt(decrypted_message, '')
print(secret)
print(private_key.decrypt(secret))
