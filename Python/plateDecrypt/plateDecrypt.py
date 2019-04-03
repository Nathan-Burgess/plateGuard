
import cv2
import read
import decrypt

def main():

    files = read.read_encrypted()

    decrypt.print_decrypt(files, "halohalohalohalo")
    path = input("Enter path")

    cap = cv2.VideoCapture(path)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # Set up output file
    out = cv2.VideoWriter('../Unencrypted/output.avi', fourcc, 30, (3840, 2160))


if __name__ == "__main__":
    main()
