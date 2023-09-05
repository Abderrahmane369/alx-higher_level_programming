#include "lists.h"

/**
 * check_cycle - check if
 * @list: the list
 * Return: Int
 */

int check_cycle(listint_t *list)
{
	listint_t *h = list, *j = h;

	if (list)
        h = h->next;

    while (h)
	{
		if (h == list)
			return (1);

		h = h->next;
	}

    while (h)
    {
        while (j)
        {
            if (j->next == h->next && j != h)
                return (0);
            j = j->next;
        }
        
        h = h->next;
    }



	return (0);
}
