CC=gcc
CFLAGS=-Wall -Wextra -Werror -pedantic -O2

all: microfetch

source.c: generate.py
	    python generate.py -q

microfetch: source.c
	    $(CC) $(CFLAGS) -o microfetch source.c

.PHONY:	all clean

clean:
		@rm microfetch source.c
