#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <errno.h>
#include <unistd.h>
#include <signal.h>

#define MAXDATASIZE 1024 // max buffer size
#define SERVER_PORT 2000


// compile with: gcc server.c -o server -std=gnu99

int listen_on(int port)
{

    int s = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in sa;
    sa.sin_family = AF_INET;          /* communicate using internet address */
    sa.sin_addr.s_addr = INADDR_ANY; /* accept all calls                   */
    sa.sin_port = htons(port); /* this is port number                */
    printf("%d\n", htons(port));
    int rc = bind(s, (struct sockaddr *)&sa, sizeof(sa)); /* bind address to socket   */
    if (rc == -1) { // Check for errors
        perror("bind");
        exit(1);
    }

    rc = listen(s, 5); /* listen for connections on a socket */
    if (rc == -1) { // Check for errors
        perror("listen");
        exit(1);
    }

    return s;
}


int accept_connection(int s) {


    /////////////////////////////////////////////
    // TODO: Implement in terms of 'accept'

    /////////////////////////////////////////////
    struct sockaddr_in ca;

    socklen_t l = sizeof(struct sockaddr_in);
    int client_s = accept(s, (struct sockaddr *)&ca, &l);
    printf("accept\n");
    return client_s;
}


void handle_request(int msgsock) {
    ///////////////////

      // This initial code reads a single message (and ignores it!)
    char buffer[MAXDATASIZE];
    int num_read = 0;
    memset(buffer, 0, MAXDATASIZE);
    //read a message from the client
    num_read = read(msgsock, buffer, MAXDATASIZE - 1);
    while (num_read) {
        printf("read a message %d bytes: %s\n", num_read, buffer);
        memset(buffer, 0, MAXDATASIZE);
        int message_length = sprintf(buffer, "Copy that!");
        write(msgsock, buffer, message_length);
        memset(buffer, 0, MAXDATASIZE);
        num_read = read(msgsock, buffer, MAXDATASIZE - 1);
    }
    // TODO: write a function to reply to all incoming messages
    // while the connection remains open

    ///////////////////


}


// handle request by forking a new process
void handle_fork(int msgsock) {

    //TODO: run this line inside a forked child process
    int pid = (int) fork();
    if (!pid) { // child code
        handle_request(msgsock);
        close(msgsock);
        printf("Finish communnication on socket %d", msgsock);
    } else { // parent code
        printf("Fork child thread %d for communication with socket %d\n", (int) pid);
    }

    // Be very careful to close all sockets used,
    // and exit any processes or threads which aren't used
      // Note that sockets open BEFORE a fork() are open in BOTH parent/child

    ///////////////////////////////////////////
}

/*
int sockets[10];

void signal_handler() {
    printf("----");
    close(sockets[0]);
    close(sockets[1]);
    exit(0);

}*/


int main(int argc, char *argv[]) {


    printf("\nThis is the server with pid %d listening on port %d\n", getpid(), SERVER_PORT);

    // setup the server to bind and listen on a port
    int s = listen_on(SERVER_PORT);
/*
    sockets[0] = s;
    signal(SIGINT, signal_handler);
*/


    while (1) { // forever

        int msgsock = accept_connection(s); // wait for a client to connect
/*
        sockets[1] = msgsock;
*/
        printf("Got connection from client!\n");

        // handle the request with a new process
        handle_fork(msgsock);
    }

    close(s);
    exit(0);
}

