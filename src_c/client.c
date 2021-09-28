#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <unistd.h>
#include <signal.h>

#include <errno.h>

#include <readline/readline.h>
#include <readline/history.h>


#define MAXDATASIZE 1024 // max buffer size
#define SERVER_PORT 2004

//compile with: gcc client.c -o client -std=gnu99 -lreadline

int client_socket(char *hostname)
{
    char port[20];
    struct addrinfo hints; // server address info
    struct addrinfo *their_addr = NULL; // connector's address information
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
    int c = connect(sockfd, their_addr->ai_addr, their_addr->ai_addrlen);

    if (c) {
        printf("ERROR %d: Cannot connect to the server", errno);
        exit(EXIT_FAILURE);
    }

    /////////////////////////

    //TODO:
    // 1) initialise socket using 'socket'
    // 2) initialise 'their_addrinfo' and use 'getaddrinfo' to lookup the IP from host name
    // 3) connect to remote host using 'connect'

    ///////////////////////////////

    return sockfd;
}

int sockfd;

/*
void signal_handler() {
    printf("----");
    close(sockfd);
    signal(SIGINT, signal_handler);
}
*/

int main(int argc, char *argv[])
{
    char buffer[MAXDATASIZE];

    if (argc != 2) {
        fprintf(stderr, "usage: client hostname\n");
        exit(1);
    }

    sockfd = client_socket(argv[1]);
/*
    signal(SIGINT, signal_handler);
*/

    int numbytes = 0;
    char *line;

    do {

        line = readline(">> ");
        while (strlen(line) == 0)
            line = readline(">> ");
        write(sockfd, line, strlen(line));

        numbytes = read(sockfd, buffer, MAXDATASIZE - 1);
        buffer[numbytes] = '\0';

        printf("server: %s\n", buffer);

    } while (numbytes > 0);

    free(line);
    close(sockfd);

    return 0;
}
