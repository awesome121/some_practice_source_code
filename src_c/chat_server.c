/*
 * Chat server using TCP socket
 *
 * Auther: Changxing Gong
 *
 * Compile with: gcc chat_server.c -o chat_server -lpthread
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

#define INADDR_LEN 4
#define MAX_DATA_SIZE 1024
#define MAX_QUEUE_SIZE 10
#define SERVER_PORT 2005

int conn_sockfd_addr[MAX_QUEUE_SIZE*2] = {0}; // (socketfd, addr) pair
int i_thread = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER; // public lock across all threads

int bind_socket(int port);
void handle_client(int *conn);
void broadcast_msg(const char *msg);
void clean_thread(int *sock);
//--------------------------------------------------------------

int bind_socket(int port) {
    int server = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);

    if (bind(server, (struct sockaddr *) &server_addr, sizeof(server_addr))) {
        printf("Bind socket failed\n");
        exit(EXIT_FAILURE);
    }
    return server;
}


void handle_client(int *sock) {
    int num;
    char buffer[INADDR_LEN+MAX_DATA_SIZE] = {0}; // buffer = 4 bytes addr + data
    buffer[0] = (*(sock+1) >> 24) + 1; // ip address
    buffer[1] = (*(sock+1) >> 16) & 0xff + 1;
    buffer[2] = (*(sock+1) >> 8) & 0xff + 1;
    buffer[3] = (*(sock+1)) & 0xff + 1;
    num = read(*sock, &buffer[INADDR_LEN], MAX_DATA_SIZE-1);
    buffer[INADDR_LEN+num] = '\0';
    while (num) {
        fprintf(stderr, "%d\n", num);
        printf("%x: %s\n", *sock, &buffer[INADDR_LEN]);
        pthread_mutex_lock(&lock);
        broadcast_msg(buffer);
        pthread_mutex_unlock(&lock);
        memset(&buffer[INADDR_LEN], 0, MAX_DATA_SIZE);
        num = read(*sock, &buffer[INADDR_LEN], MAX_DATA_SIZE);
    }
    printf("Client %d is down", *sock);
    close(*sock);
    pthread_mutex_lock(&lock);
    clean_thread(sock);
    pthread_mutex_unlock(&lock);
}

void broadcast_msg(const char *buffer) {
    size_t msg_l = strlen(&buffer[INADDR_LEN]); // msg excluding '\0'
    for (int i=0; i<MAX_QUEUE_SIZE*2; i+=2) {
        if (conn_sockfd_addr[i] != 0)
        {printf("broadcast: %s\n", &buffer[INADDR_LEN]);
            write(conn_sockfd_addr[i], buffer, INADDR_LEN+msg_l);
        }
    }
}

int get_next_thread_loc() {
    for (int i=0; i<MAX_QUEUE_SIZE*2; i+=2) {
        if (conn_sockfd_addr[i] == 0)
            return i;
    }
}

void clean_thread(int *sock) {
    *(sock) = 0;
    *(sock+1) = 0;
}

int main(int argc, char *argv[]) {
    int server = bind_socket(SERVER_PORT);
    if (listen(server, MAX_QUEUE_SIZE)) {
        printf("Listen failed\n");
        exit(EXIT_FAILURE);
    } else
        printf("Start listening...\n");

    while (1) {
        struct sockaddr_in client_addr;
        socklen_t sock_len = sizeof(struct sockaddr_in);

        int client = accept(server, (struct sockaddr *) &client_addr, &sock_len);
        conn_sockfd_addr[i_thread] = client;
        conn_sockfd_addr[i_thread+1] = client_addr.sin_addr.s_addr;
        printf("New connection: %x\n", client_addr.sin_addr.s_addr);
        pthread_t id;
        pthread_create(&id, NULL, handle_client, &conn_sockfd_addr[i_thread]);
        i_thread = get_next_thread_loc();
    }

    close(server);
    exit(EXIT_SUCCESS);
}




















