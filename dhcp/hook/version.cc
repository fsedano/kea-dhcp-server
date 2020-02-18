#include <hooks/hooks.h>

#include <stdio.h>

extern "C" {
int version() {
	FILE *pf = fopen("/tmp/fran.log", "a");
	fprintf(pf, "Init\n");
	fclose(pf);
    return (KEA_HOOKS_VERSION);
}
}