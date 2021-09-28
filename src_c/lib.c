#include <stdio.h>
#include <stdlib.h>


int count_space()
{
    int total = 0;
    int c;
    while ((c = getchar()) != EOF) {
        if (c == '\n' || c == '\t' || c == ' ') {
            total += 1;
        }
    }
    return total;
}

void replace_blanks_with_blank()
{
    int c;
    int was_blank = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            if (!was_blank) {
                putchar(' ');
                was_blank = 1;
            }
        } else {
            was_blank = 0;
            putchar(c);
        }
    }        

}

void view_tab_backspace_backslash()
{
    int c;
    while ((c = getchar()) != EOF) {
        if (c == '\t' || c == '\b' || c == '\\') {
            putchar('\\');
            if (c == '\t')
                putchar('t');
            else if (c == '\b')
                putchar('b');
            else if (c == '\\')
                putchar('\\');
        } else {
            putchar(c);
        }
    }
}

void print_word_per_line()
{
    int c;
    int out = 1;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (out == 0)
                putchar('\n');   
            out = 1;
        } else {
            putchar(c);
            out = 0;
        }
    }
}

void print_word_len_histogram()
{
    int c;
    int wl = 0;
    int out = 1;

    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (out == 0) {
                for (int i = 0; i < wl; i++) {
                    putchar('-');
                }
                wl = 0;
                putchar('\n');
            }
            out = 1;
        } else {
            wl++;
            out = 0;
        }
    }
}

void print_char_freq_histogram()
{
    int c;
    int chars[26];
    for (int i=0; i<26; i++) {
        chars[i] = 0;
    }
    
    while ((c = getchar()) != EOF) {
        if (c != ' ' && c != '\n' && c != '\t') {
            chars[c-97] += 1;
        }
    }

    for (int i=0; i<26; i++) {
        putchar(i+97);
        putchar(':');
        putchar(' ');
        for (int j=0; j<chars[i]; j++) {
            putchar('-');
        }
        putchar('\n');
    }
    
}
#define NUM_DIGIT 32
void binary_to_decimal()
{
    int c;
    int bin[NUM_DIGIT];
    int index = 0;
    int count = 1;
    int result = 0;

    for (int i=0; i<NUM_DIGIT; i++) {
        bin[i] = 0;
    }
    while ((c = getchar()) != '\n') {
        if (c == '1') 
            bin[index] = 1;
        index++;

        if (index-1 >= NUM_DIGIT) {
            printf("exceed num of digit %d\n", NUM_DIGIT);
            exit(1);
        }
    }
    for (int i = index-1; i>=0; i--) {
        result += bin[i] * count;
        count *= 2;    
    }

    if (bin[0] == 1)
        result -= count;
    printf("%d\n", result);
}

void decimal_to_binary()
{
    int dec[NUM_DIGIT];
    int bin[NUM_DIGIT];
    int c;
    int sign = 0;
    int result = 0;
    int i_bin = 0;
    int i_dec = 0;
    int count = 1;
    
    // read decimal
    while ((c = getchar()) != '\n') {
        if (c == '-')
            sign = 1;
        else 
            dec[i_dec++] = c-48;
    }
    // process decimal
    for (int i = i_dec-1; i>=0; i--) {
        result += count * dec[i];
        count *= 10;
    }
    // convert to binary
    while (result != 0) {
        if (result % 2 == 0) {
            bin[i_bin] = 0;
        } else {
            bin[i_bin] = 1;
            result -= 1;
        }
        if (result <= 1)
            bin[++i_bin] = result;
        result /= 2;
        i_bin += 1;
    }

    // output binary
    putchar(sign+48);
    for (int i=i_bin-1; i>=0; i--) {
        if (sign) {
            if (bin[i] == 0)
                putchar(1+48);
            else 
                putchar(48);
        } else {
            putchar(bin[i]+48);
        }
    }
}

void reverse_string()
{
    char current[100];
    int i = 0;
    int temp, c;

    while ((c = getchar()) != EOF) {
        if (c == '\n') {
            if (i >= 0) {
                for (int j=0; j<=(i-1)/2; j++) {
                    temp = current[j];
                    current[j] = current[i-1-j];
                    current[i-1-j] = temp;
                }
                current[i] = '\0';
                printf("%s\n", current);
                i = 0;            
            } 
        }
        else {
            current[i++] = c;
        }
    }
}

void strip_string()
{
    char buffer[100];
    int i = 0;
    int c = 0;
    int in = 0;
    int mark = 0;

    while ((c = getchar()) != EOF) {
        if (c == '\n'){
            if (i!=0) {
                buffer[mark+1] = '\0';
                printf("%s\n", buffer);
                i = c = in = mark = 0;
            }
        } else if (c != ' ' && c != '\t') { // string
            if (!in && (c == ' ' || c == '\t'))
                putchar(' ');
            in = 1;
            mark = i;
            buffer[i++] = c;
        } else if (in) {
            buffer[i++] = c;
        }

    }
}

#define MAX 100000
void strip_comments()
{
    int c;
    char buffer[MAX];
    int i = 0;
    int slash_star_done = 0;

    c = getchar();
    while (c != EOF) {
        if (c == '/') {
            c = getchar();
            if (c == '/') { // // double slash
                while (c != '\n' && c != EOF) {
                    c = getchar();
                }
                if (c == '\n')
                    buffer[i++] = '\n';
            } else if (c == '*') { // /* slash star
                slash_star_done = 0;
                while (!slash_star_done) {
                    
                    while (c != '*') {
                        c = getchar();
                    }
                    if ((c = getchar()) == '/')
                        slash_star_done = 1;
                }
            } else {
                buffer[i++] = '/';
                buffer[i++] = c;
            }
        } else {
            buffer[i++] = c;
        }    
     
        c = getchar();
    }
    buffer[i] = '\0';
    printf("%s", buffer);
}  
#include <ctype.h>
#include <math.h>
void htoi(char* s)
{
    int result = 0;
    int i = 0;
    int limit = 0;
    while (s[i] != '\0') {
        i++;
    }
    if (i > 0) {
        if (i >= 1 && s[0] == '0' && (s[1] == 'x' || s[1] == 'X')) {
            limit = 1;
        }
        for (int j = i-1; j>=limit+1; j--){
            if (isdigit(s[j])) {
                result += pow(16, i-1-j) * (s[j]-48);
            } else {
                result += pow(16, i-1-j) * (tolower(s[j])-97+10);
            }
        }
        printf("%d\n", result);

    }
}

#include <string.h>



char * addBinary(char * a, char * b){
    int a_l = strlen(a), b_l = strlen(b), carry = 0;
    int longest = a_l > b_l ? a_l : b_l;
    int shortest = a_l > b_l ? b_l : a_l;
    char *sum = malloc(longest + 2);
    sum[longest + 1] = '\0';
    for (int i=0; i<shortest; i++) {
        sum[i] = '0' + (carry + a[a_l-1-i] - '0' + b[b_l-1-i] - '0') % 2;
        carry = (a[a_l-1-i] - '0' + b[b_l-1-i] - '0' + carry) / 2;
    }
    if (longest - shortest != 0) {
        if (longest == a_l) {
            for (int i=shortest; i<longest; i++) {
                sum[i] = '0' + (carry + a[a_l-1-i] - '0') % 2;
                carry = (a[a_l-1-i] - '0' + carry) / 2;
            }
        } else {
            for (int i=shortest; i<longest; i++) {
                sum[i] = '0' + (carry + b[b_l-1-i] - '0') % 2;
                carry = (b[b_l-1-i] - '0' + carry) / 2;
            }
        }
        if (carry) {
            sum[longest++] = '1';
        }
            
    } else if (carry) 
        sum[longest++] = '1';

    int temp;
    for (int i=0; i<longest/2; i++) {
        int temp = sum[i];
        sum[i] = sum[longest-1-i];
        sum[longest-1-i] = temp;
    }
    if (!carry) 
        sum[longest] = '\0';
    return sum;
}


int* buildArray(int* nums, int numsSize, int* returnSize) {
    returnSize = malloc(numsSize+1);
    for (int i=0; i<numsSize; i++) {
        returnSize[i] = nums[nums[i]];
    }
    returnSize[numsSize] = '\0';
    printf("%s\n", returnSize);
    return returnSize;
}


/* Given a sorted array of distinct integers and a target value, return the index if the target is found. 
 * If not, return the index where it would be if it were inserted in order.
 * Using binary search
*/

int searchInsert(int* nums, int numsSize, int target){
    int lower = 0, upper = numsSize-1, middle = upper/2;
    
    while (lower<upper) {
        if (target <= nums[middle]) {
            upper = middle;
        } else {
            lower = middle + 1;
        }
        middle = (lower + upper) / 2;
    }
    if (target > nums[numsSize-1])
        return middle+1;
    else
        return middle;
}


/*
   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
   An input string is valid if:
       Open brackets must be closed by the same type of brackets.
       Open brackets must be closed in the correct order.
*/

bool isValid(char * s){
    int l = strlen(s);
    if (l % 2 == 1)
        return false;

    char *stack = malloc(sizeof(char)*l);
    int stack_size = 0;
    for (int i=0; i<l; i++) {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
            stack[stack_size++] = s[i];
        else if (s[i] == ')' && stack_size > 0 && stack[stack_size-1] == '(')
            stack_size--;
        else if (s[i] == '}' && stack_size > 0 &&  stack[stack_size-1] == '{')
            stack_size--;
        else if (s[i] == ']' && stack_size > 0 &&  stack[stack_size-1] == '[')
            stack_size--;
        else {
            free(stack);
            return false;
        }
    }
    free(stack);
    if (stack_size==0)
        return true;
    else
        return false;
}


int main()
{
    int *return_size;
    int nums[6] = {5,0,1,2,3,4};
    buildArray(nums, 6, return_size);
    printf("%s\n", return_size);
    free(return_size);
}
