CC=gcc
CFLAGS=-Wall -Wextra -Werror -pedantic -O2 -s

all: microfetch

source.c: generate.py
	python generate.py

microfetch: source.c
	$(CC) $(CFLAGS) -o microfetch source.c

.PHONY:	all clean

clean:
	@rm microfetch source.c
