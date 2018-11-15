HDIR1=/usr/local/include/opencv4
HDIR2=../headers
CC=g++
CFLAGS=-I$(HDIR1) -I$(HDIR2) -std=c++11

ODIR=obj
LDIR=/usr/local/lib

LIBS=-lopencv_core -lopencv_highgui -lopencv_videoio

# Enter .h files here
_DEPS=
DEPS = $(patsubst %$(HDIR)/%,$(_DEPS))

# Enter .o files here
_OBJ=
OBJ = $(patsubst %, $(ODIR)/%,$(_OBJ))

# Enter output name
ImageEncrypt: $(OBJ)
		$(CC) ImageEncrypt.cpp -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~
