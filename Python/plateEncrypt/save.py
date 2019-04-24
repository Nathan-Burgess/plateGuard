

def save_encypt(nonce, tag, ciphertext, frame_num, car_num, path):
    path = "../20190401/0000/"
    file_name = str(frame_num).zfill(5) + "_" + str(car_num)
    file_out = open(path + file_name + ".wfc", "wb")
    [file_out.write(x) for x in (nonce, tag, ciphertext)]


def save_frame(buf, out):

    for b in buf.frames:
        out.write(b)
