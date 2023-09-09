#include "lists.h"
#include <stdio.h>

/**
 * node - eza
 * @h: zae
 * @_: eza
 * Return: eza
 */

listint_t *node(listint_t *h, int _)
{
	listint_t *n = h;
	int c = 0;

	if (c == _)
		return (n);

	while (c != _)
	{
		n = n->next;
		c++;
	}

	return (n);
}

/**
 * is_palindrome - eza
 * @head: ezaeza
 * Return: eaz
 */

int is_palindrome(listint_t **head)
{
	listint_t *_h = *head;
	size_t _hlen = 0;
	size_t _;

	while (_h)
		_hlen++, _h = _h->next;

	_h = *head;

	for (_ = 0; _hlen / 2 >= _; _++)
	{
		if (node(_h, _hlen - 1 - _)->n != node(_h, _))
			return (0);
	}

	return (1);
}
