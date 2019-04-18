
import cv2
import read
import decrypt
import save
import datetime


def main():
    key = input("Enter Plate#:").upper()
    key = (key * 16)[0:16]

    files = read.read_encrypted()

    hits = decrypt.print_decrypt(files, key)
    # path = input("Enter path")
    path = '../20190401/0000/output.avi'
    cap = cv2.VideoCapture(path)
    frame_nums = []

    plate_found = False

    for h in hits:
        frame_nums.append(h['frame'])
        # print(h["frame"])
    # frame_nums.sort()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('../Unencrypted/output.avi', fourcc, 30, (3840, 2160))

    # Counter for number of frames
    j = 0
    # Return boolean to ensure reading in frames
    ret = True

    # Loops through while video is reading in
    while ret:
        # Initialize buffer object
        # Read in frames
        print("Read in frames...")
        for i in range(300):
            ret, frame = cap.read()
            if ret is True:
                z = i+j
                if z in frame_nums:
                    if not plate_found:
                        plate_found = True
                        timestamp = z / 30
                        print("Plate found at " + str(datetime.timedelta(seconds=timestamp)))
                    # print("decrypting at frame" + str(z))
                    data_d = give_data(hits, z)
                    new_frame = decrypt.decrypt_frame(data_d, frame)
                    save.save_frame(new_frame, out)
                else:
                    save.save_frame(frame, out)
            else:
                break
        print("Finding Plates...")

        j += 300
        print("Saving Buffer...")
        # save.save_frame(buff, out)

    cap.release()
    out.release()


def give_data(hits, num):
    for h in hits:
        if num == h['frame']:
            return h


if __name__ == "__main__":
    main()
