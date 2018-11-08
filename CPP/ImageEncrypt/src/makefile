HDIR=../headers
CC=g++
CFLAGS=-I$(HDIR)

ODIR=obj
LDIR=../lib

# Enter .h files here
_DEPS=
DEPS = $(patsubst %$(HDIR)/%,$(_DEPS))

# Enter .o files here
_OBJ=
OBJ = $(patsubst %, $(ODIR)/%,$(_OBJ))

# Enter output name
ImageEncrypt: $(OBJ)
		$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~
