export CFLAGS =   -march=native -O3

# The following conditional statement appends "-std=gnu99" to CFLAGS when the
# compiler does not define __STDC_VERSION__.  The idea is that many older
# compilers are able to compile standard C when given that option.
# This hack seems to work for all versions of gcc, clang and icc.
CVERSION = $(shell $(CC) -dM -E - < /dev/null | grep __STDC_VERSION__)
ifeq ($(CVERSION),)
CFLAGS := $(CFLAGS) -std=gnu99
endif

BINDIR = bin
LIBDIR = lib

default: $(BINDIR) $(BINDIR)/ransac $(LIBDIR) $(LIBDIR)/libransac.so

$(BINDIR)/ransac: c/ransac.c c/fail.c c/xmalloc.c c/xfopen.c c/homographies.c c/ransac_cases.c c/parsenumbers.c c/random.c
	$(CC) $(CFLAGS) $< -lm -o $@

$(LIBDIR)/libransac.so: c/ransac.c c/fail.c c/xmalloc.c c/xfopen.c c/homographies.c c/ransac_cases.c c/parsenumbers.c c/random.c
	$(CC) $(CFLAGS) -shared -o $@ $<

$(BINDIR):
	mkdir -p $(BINDIR)

$(LIBDIR):
	mkdir -p $(LIBDIR)

clean:
	rm -rf bin
	rm -rf lib
