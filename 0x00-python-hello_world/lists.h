#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

typedef struct listLIS
{
	listint_t *node;
	struct listLIS *next;
} listLIS;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
listLIS *add_nodeLIS(listLIS **head, listint_t *node);
void free_listint(listint_t *head);
void free_listLIS(listLIS *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
