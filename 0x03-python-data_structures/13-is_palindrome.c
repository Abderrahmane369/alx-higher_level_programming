#include "lists.h"
#include <stdio.h>

listint_t *node(listint_t *h, int _)
{
    listint_t *n = h;
    int c = 0;

    if (c == _)
        return (n);

    while (_ != c)
    {
        n = n->next;
        c++;
    }

    return (n);
}

int is_palindrome(listint_t **head)
{
    listint_t *_h = *head;
    size_t _hlen = 0;
    size_t _;

    while (_h)
        _hlen++, _h = _h->next;

    _h = *head; 

    for (_ = 0; _ <= _hlen / 2; _++)
    {
        if (node(_h, _)->n != node(_h, _hlen - 1 - _)->n)
            return (0);
    }

    return (1);
}
