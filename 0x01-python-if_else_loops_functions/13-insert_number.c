#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - node insert
 * @head: the head
 * @number: n
 * Return: The
*/

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *_current = *head, *_previous, *_newNode;
  
    while (_current)
    {
        if (number > _current->n)
             _previous = _current, _current = _current->next;
        else
            break;
    }

    _newNode = malloc(sizeof(listint_t));
    if (!_newNode)
        return (NULL);

    _newNode->n = number, _newNode->next = _current;

    if (*head)
        _previous->next = _newNode;

    if (_current == *head)
        *head = _newNode;
    
    return (_newNode);
}