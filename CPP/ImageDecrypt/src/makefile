HDIR1=/usr/local/include
HDIR2=../headers
HDIR3=../../sharedHeaders
CC=g++
CFLAGS=-I$(HDIR2) -I$(HDIR3) -std=c++11

ODIR=obj
LDIR=../lib

LIBS=-lopencv_core -lopencv_highgui -lopencv_videoio

# Enter .h files here
_DEPS= Receive.h
DEPS = $(patsubst %,$(HDIR2)/%,$(_DEPS))

# Enter .o files here
_OBJ= Receive.o
OBJ = $(patsubst %, $(ODIR)/%,$(_OBJ))

$(ODIR)/%.o: %.cpp $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

# Enter output name
ImageDecrypt: ImageDecrypt.cpp $(OBJ)
		$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~
	rm ImageDecrypt
