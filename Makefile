export CFLAGS =   -march=native -O3

# The following conditional statement appends "-std=gnu99" to CFLAGS when the
# compiler does not define __STDC_VERSION__.  The idea is that many older
# compilers are able to compile standard C when given that option.
# This hack seems to work for all versions of gcc, clang and icc.
CVERSION = $(shell $(CC) -dM -E - < /dev/null | grep __STDC_VERSION__)
ifeq ($(CVERSION),)
CFLAGS := $(CFLAGS) -std=gnu99
endif

default: bin/ransac

lib: lib/libransac.so

bin/ransac: c/ransac.c c/*.c
	mkdir -p bin
	$(CC) $(CFLAGS) $< -lm -o $@

lib/libransac.so: c/ransac.c c/*.c
	mkdir -p lib
	$(CC) $(CFLAGS) -fPIC -shared -o $@ $<

clean:
	rm -rf bin
	rm -rf lib
