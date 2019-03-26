

# TODO add ability to put metadata to front of frame showing time-data, also add file namin convention
def save_encypt(ciphertext, tag, nonce):

    file_out = open("encrypted.txt", "wb")
    [file_out.write(x) for x in (ciphertext, tag, nonce)]
    print(ciphertext + tag + nonce)


def save_frame(buf, out):

    for b in buf.frames:
        out.write(b)
