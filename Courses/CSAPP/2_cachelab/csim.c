// Copy from https://github.com/ftlc/cachelab/blob/master/csim.c

#include "cachelab.h"
#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>

typedef unsigned long long mem_64;

typedef struct{
    mem_64 tag;
    char* block;
    int valid;
    // Cycles since used (for eviction)
    int age;
} Line;

typedef struct{
    Line* lines;
} Set;

typedef struct {
    int E;
    mem_64 B;
    mem_64 S;
    int b;
    int s;
    int tag_size;

    int hits;
    int misses;
    int evicts;

    Set* sets;
} Cache;

Line line_build(int B) {
    Line line;
    line.block = (char*) calloc(B, sizeof(char));
    line.valid = 0;

    return line;
}

Set set_build(int E, int B) {
    Set set;
    set.lines = (Line*) calloc(E, sizeof(Line));

    int i;
    Line* lines = set.lines;
    for (i = 0; i < E; i++) {
        lines[i] = line_build(B);
    }
    return set;
}

Cache* cache_build(int s, int E, int b){
    // why a pointer here?
    Cache* cache = (Cache*) calloc(1, sizeof(Cache));
    cache->E = E;
    cache->b = b;
    cache->s = s;

    cache->hits = 0;
    cache->misses = 0;
    cache->evicts = 0;

    cache->S = 2 << s;
    cache->B = 2 << b;
    //? t should be m-s-b?
    cache->tag_size = (sizeof(mem_64)*8) - (s+b);

    int S = cache->S;
    int B = cache->B;

    cache->sets = (Set*) calloc(S, sizeof(Set));
    Set* sets = cache->sets;

    int i;
    for (i = 0; i < S; i++) {
        sets[i] = set_build(E, B)
    }

    return cache;
}

// The parameter B is unnecessary
void line_free(Line line, int B){
    char* block = line.block;
    free(block);
    return;
}

void set_free(Set set, int E, int B) {
    Line* lines = set.lines;
    int i;
    for (i = 0; i < E; i++) {
        line_free(lines[i], B)
    }
    free(lines);
}

void cache_free(Cache* cache){
    Set* sets = cache->sets;
    int S = cache->S;
    int E = cache->E;
    int B = cache->B;

    int i;
    for (i = 0; i < E; i++) {
        set_free(sets[i], E, B);
    }

    free(sets);
    free(cache);
    return;
}


Line* set_search(Set* set, mem_64 tag, int E) {
    int i;
    Line* line = NULL;
    for (i = 0; i < E; i++) {
        line = &(set->lines[i]);
        if (line->valid && line->tag == tag){
            return line;
        }
    }
    return NULL;
}

void increase_age(Set* search_set, int E){
    int i;
    for (i = 0; i < E; i++) {
        Line* current_line = &(search_set->lines[i]);
        current_line->age++;
    }
}

void cache_hit(Cache* cache, Set* search_set, Line* found_line, int E) {
    increase_age(search_set, E);
    found_line->age = 0;
    cache->hits++;
    return;
}

void cache_miss(Cache* cache, Set* search_set, int E, mem_64 tag){
    cache->misses++;
    Line* oldest_line = NULL;
    increase_age(search_set, E); // a common line in both case

    int i;
    for (i = 0; i < E; i++) {
        Line* current_line = &(search_set->lines[i]);
        if (!current_line->valid){
            current_line->valid = 1;
            current_line->tag = tag;
            current_line->age = 0;
            return;
        }

        if(current_line->age > oldest_line->age 
                || oldest_line == NULL) {
            oldest_line = current_line;
        }
    }
    
    oldest_line->tag = tag;
    oldest_line->age = 0;
    cache->evicts++;
    return;
}

void cache_search(Cache* cache, mem_64 address){
    int b = cache->b;
    int s = cache->s;
    int E = cache->E;
    int tag_size = cache->tag_size;

    int set_number = (address >> b) & ~(~0 << s);
    mem_64 tag = (address >> (s+b)) & ~(~0 << tag_size);

    Set* search_set = &(cache->sets[set_number]);
    Line* found_line = set_search(search_set, tag, E);

    if (found_line) {
        cache_hit(cache, search_set, found_line, E);
        return;
    }

    cache_miss(cache, search_set, E, tag);
    return;
}

int v = 0;

int main()
{
    int s;
    int E;
    int b;
    char* t;
    FILE* trace;

    char flag = getopt(argc, argv, "s:E:b:t:v");
    do {
        switch(flag){
            case 's':
                s = atoi(optarg);
                break;
            case 'E':
                E = atoi(optarg);
                break;
            case 'b':
                b = atoi(optarg);
                break;
            case 't':
                t = optarg;
                break;
            case 'v':
                v = 1;
                break;
            default:
                printf("Please Enter Arguments for the Cache\n");
                return -1;
        } 
    } while ((flag = getopt(argc, argv, "s:E:b:t:v")) != -1);

    if (s == 0 || E == 0 || b == 0 || t == NULL) {
        printf("Please provide valid arguments");
        return -1;
    }

    Cache* cache = cache_build(s, E, b);

    trace = fopen(t, "r");
    if (trace) {
        char instruction;
        mem_64 addr;
        int size;

        while(fscanf(trace, " %c %llx,%d", &instruction, &addr, &size) == 3){
            switch(instruction) {
                case 'L' : case 'S':
                    cache_search(cache, address);
                    break;
                case 'M':
                    cache_search(cache, address);
                    cache_search(cache, address);
                    break;
                default:
                    break;
            }
        }
    } else {
        printf("Please provide a trace file\n");
    }

    printSummary(cache->hits, cache->misses, cache->evicts);

    fclose(trace);
    cache_free(cache);

    return 0;
}
