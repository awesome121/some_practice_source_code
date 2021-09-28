/*
 * Chat client using TCP socket
 *
 * Auther: Changxing Gong
 *
 * Compile with: gcc chat_client.c -o chat_client -lpthread -lreadline
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <errno.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <pthread.h>
#include <errno.h>
#include <readline/readline.h>
#include <readline/history.h>

#define INET_LEN 4
#define MAX_DATA_SIZE 1024 
#define SERVER_PORT 2005

int bind_socket(char* hostname) {
    char port[20];
    struct addrinfo hints;
    struct addrinfo *their_addr = NULL;
    int sockfd;

    int n = snprintf(port, 20, "%d", SERVER_PORT); // Make a string out of the port number
    if ((n < 0) || (n >= 20))
    {
        printf("ERROR: Malformed Port\n");
        exit(EXIT_FAILURE);
    }
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    memset(&hints, 0, sizeof(struct addrinfo));
    hints.ai_family = AF_INET;
    hints.ai_socktype = SOCK_STREAM;

    getaddrinfo(hostname, port, &hints, &their_addr);
    if (connect(sockfd, their_addr->ai_addr, their_addr->ai_addrlen)) {
        printf("ERROR %d: cannot connect to the server", errno);
        exit(EXIT_FAILURE);
    }

    return sockfd;
}

void recv_msg(int *sockfd) {
    char recv_buffer[INET_LEN+MAX_DATA_SIZE] = {0};
    int numbytes;
    do {
        numbytes = read(*sockfd, recv_buffer, INET_LEN+MAX_DATA_SIZE - 1);
        recv_buffer[numbytes] = '\0';
        printf("server: (%d) %s\n", numbytes, &recv_buffer[INET_LEN]);
        memset(recv_buffer, 0, INET_LEN+MAX_DATA_SIZE);
    } while (numbytes);
}

void send_msg(int *sockfd) {
    char* send_buffer;
    while (1) {
        send_buffer = readline(">> ");
        while (strlen(send_buffer) == 0)
            send_buffer = readline(">> ");
        write(*sockfd, send_buffer, strlen(send_buffer));
    }
    free(send_buffer);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: client hostname\n");
        exit(EXIT_FAILURE);
    }

    int sockfd = bind_socket(argv[1]);
    pthread_t recv_t, send_t;

    pthread_create(&recv_t, NULL, &recv_msg, &sockfd);
    pthread_create(&send_t, NULL, &send_msg, &sockfd);

    pthread_join(recv_t, NULL);
    pthread_join(send_t, NULL);
    close(sockfd);
    return 0;
}



