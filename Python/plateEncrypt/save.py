

def save_encypt(ciphertext, tag, nonce):

    file_out = open("encrypted.txt", "wb")
    [file_out.write(x) for x in (ciphertext, tag, nonce)]
    print(ciphertext + tag + nonce)
