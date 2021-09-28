
#include "queue.h"

#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>
#include <stdio.h>
#include <errno.h>
#include <assert.h>

#define handle_error_en(en, msg) \
        do { errno = en; perror(msg); exit(EXIT_FAILURE); } while (0)

#define handle_error(msg) \
        do { perror(msg); exit(EXIT_FAILURE); } while (0)

typedef struct QueueStruct {
    int front, rear, capacity, size;
    void **array;
    pthread_mutex_t lock;
    sem_t *not_full;
    sem_t *not_empty;
} Queue;


Queue *queue_alloc(int size) {
    void *array = malloc(size * sizeof(void*));
    Queue *queue = malloc(3 * sizeof(int) + sizeof(void**) + sizeof(pthread_mutex_t) + 2 * sizeof(sem_t*));
    queue->front = 0;
    queue->rear = 0;
    queue->capacity = size;
    queue->size = 0;
    queue->lock = (pthread_mutex_t)PTHREAD_MUTEX_INITIALIZER;
    queue->array = array;
    int num1 = sem_init(queue->not_full, 0, 1); // Put
    int num2 = sem_init(queue->not_empty, 0, 0); // Get
    printf("init: %d %d %d\n", num1, num2, errno);
    return queue;
}

void queue_free(Queue *queue) {
    free(queue->array);
    free(queue);
}

void queue_put(Queue *queue, void *item) {
    //printf("%d\n", queue->not_full)
    sem_wait(queue->not_full); // wait for a space
    //printf("===%d %d===\n", queue->front, queue->rear);
    pthread_mutex_lock(&queue->lock);
    queue->array[queue->rear] = item;
    queue->rear = (queue->rear + 1) % queue->capacity;
    queue->size += 1;
    printf("size:%d\n", queue->size);
    //printf("%d\n", queue->capacity);
    //printf("%d %d %d %d\n", queue->front, queue->rear, queue->size, queue->capacity_left);
    if (queue->size != queue->capacity)
        sem_post(queue->not_full);
    pthread_mutex_unlock(&queue->lock);
    sem_post(queue->not_empty);
}



void *queue_get(Queue *queue) {
    printf("%d %d--\n", (int)queue->not_empty, pthread_self());
    sem_wait(queue->not_empty);
    printf("%d-%d\n", queue->not_empty, pthread_self());
    pthread_mutex_lock(&queue->lock);
    printf("===%d %d %d %d===\n\n", queue->front, queue->rear, queue->size,pthread_self());
    void *item = queue->array[queue->front];
    queue->front = (queue->front + 1) % queue->capacity;
    //printf("---%d %d\n", queue->front, queue->rear);
    queue->size -= 1;
    if (queue->size != 0)
        sem_post(queue->not_empty);
    pthread_mutex_unlock(&queue->lock);
    sem_post(queue->not_full);
    return item;
}

