#include <stdio.h>
#define MAXLINE 100 // 100 chars in a single line

int get_line(char line[], int maxline);
void copy(char to[], char from[]);


int main()
{
    int len; // current line length
    int max; // longest line saved length
    char line[MAXLINE]; // current line 
    char longest[MAXLINE]; // longest line saved until now

    max = 0;
    while ((len = get_line(line, MAXLINE)) > 0) {
        if (len > max) {
            max = len;
            copy(longest, line);
        }
    }
    if (max > 0)
    {   
        int i = 0;
        printf("longest line with len %d: %s\n", max, longest);
    }
    return 0;
}


/* getline: read a line into s, return its length */
int get_line(char s[], int lim)
{
    int c;
    int i;

    for (i = 0; i < lim - 1 && ((c = getchar()) != EOF) && c != '\n'; i++) {
        s[i] = c;
    }

    s[i] = '\0';
    return i;
}

/* copy copy 'from' to 'to', assume 'to' is big enough */
void copy(char to[], char from[])
{
    int i = 0;
    while ((to[i] = from[i]) != '\0') {
        i++;
    }
}









