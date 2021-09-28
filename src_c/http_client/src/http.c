#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <netdb.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#include <errno.h>
#include "http.h"

#define BUF_SIZE 1024
#define QUERY "GET /%s HTTP/1.0\r\nHost: %s\r\nUser-Agent: getter\r\n\r\n"

int bind_socket(char* hostname, int hostport) {
    char port[20];
    struct addrinfo hints;
    struct addrinfo *their_addr = NULL;
    int sockfd;

    int n = snprintf(port, 20, "%d", hostport); // Make a string out of the port number
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
        perror("ERROR: cannot connect to the server");
        exit(EXIT_FAILURE);
    }

    return sockfd;
}


void send_query(Buffer *query_buffer, int sockfd, char *host, char *page) {
    int total = strlen(QUERY)+strlen(page)+strlen(host);
    query_buffer->data = malloc(total);
    sprintf(query_buffer->data, QUERY, page, host);
    query_buffer->length = total;
    //printf("%s\n",query_buffer->data);
    //printf("total %d %d", total, strlen(query_buffer->data)); 
    int num_write = write(sockfd, query_buffer->data, query_buffer->length); 
    if (num_write == -1) {
        perror("ERROR: WRITE fails");
        exit(EXIT_FAILURE);
    }
    free(query_buffer->data);
    free(query_buffer);
}


void recv_response(Buffer *recv_buffer, int sockfd) {
    int num_bytes = 0;
    do {

        recv_buffer->data = realloc(recv_buffer->data, recv_buffer->length+BUF_SIZE);
        num_bytes = read(sockfd, recv_buffer->data+recv_buffer->length, BUF_SIZE);
        recv_buffer->length = recv_buffer->length + num_bytes;

    } while (num_bytes > 0);




//    int byte_left = 0;
//    // header
//    size_t num_read = recv(sockfd, recv_buffer->data, BUF_SIZE, 0);
//    num_read = strlen(recv_buffer->data);
//    printf("%d %d %d\n", byte_left, num_read, strlen(recv_buffer->data));
//    if (num_read == -1) {
//        printf("ERROR %d: cannot read from fd\n", errno);
//        exit(EXIT_FAILURE);
//    }
//    recv_buffer->length = num_read;
//    // how much bytes for header
//    char* len_pos = strstr(recv_buffer->data, "Content-Length:");
//    if (len_pos != NULL) {
//        byte_left = strtol(len_pos+strlen("Content-Length:"), NULL, 10); 
//        if (byte_left != 0)
//            recv_buffer->data = realloc(recv_buffer->data, num_read + byte_left);
//    }
//    printf("%d %d\n", byte_left, num_read);
//    printf("%s\n", recv_buffer->data);
//    // content
//    while (byte_left && num_read) {
//        num_read = recv(sockfd, recv_buffer->data+recv_buffer->length, byte_left, 0);
//        if (num_read == -1) {
//            printf("ERROR %d: cannot read from fd\n", errno);
//            exit(EXIT_FAILURE);
//        }
//        recv_buffer->length = recv_buffer->length + num_read;
//        byte_left -= num_read;
//       printf("%d %d\n", byte_left, num_read);
//    }

}


Buffer* http_query(char *host, char *page, int port) {
    int sockfd;
    Buffer *query_buffer = malloc(sizeof(char*) + sizeof(size_t));
    query_buffer->data = NULL;
    Buffer *recv_buffer = malloc(sizeof(char*) + sizeof(size_t));
    recv_buffer->data = NULL;
    recv_buffer->length = 0;
    //create tcp socket
    sockfd = bind_socket(host, port);
    //send query 

    send_query(query_buffer, sockfd, host, page);
    //printf("%s\n", query_buffer->data);
    //recv response

    recv_response(recv_buffer, sockfd);
    close(sockfd);
    return recv_buffer;
}

// split http content from the response string
char* http_get_content(Buffer *response) {

    char* header_end = strstr(response->data, "\r\n\r\n");

    if (header_end) {
        return header_end + 4;
    }
    else {
        return response->data;
    }
}


Buffer *http_url(const char *url) {
    char host[BUF_SIZE];
    strncpy(host, url, BUF_SIZE);

    char *page = strstr(host, "/");
    if (page) {
        page[0] = '\0';

        ++page;
        return http_query(host, page, 80);
    }
    else {

        fprintf(stderr, "could not split url into host/page %s\n", url);
        return NULL;
    }
}

