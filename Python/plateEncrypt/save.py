

# TODO add ability to put metadata to front of frame showing time-data, also add file namin convention
def save_encypt(nonce, tag, ciphertext, frame_num, car_num):

    path = "../files"
    file_name = frame_num + "_" + car_num
    file_out = open(path + file_name + ".halo", "wb")
    [file_out.write(x) for x in (nonce, tag, ciphertext)]
    print(ciphertext + tag + nonce)


def save_frame(buf, out):

    for b in buf.frames:
        out.write(b)


