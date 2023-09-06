#include "lists.h"

/**
 * check_cycle - check if
 * @list: the list
 * Return: Int
 */

int check_cycle(listint_t *list)
{
        listint_t *h = list;
        listLIS *lIs = NULL, *head_lIs;

        while (h)
        {
                while (lIs)
                {
                        if (h == lIs->node)
                                return (1);

                        lIs = lIs->next;
                }
                add_nodeLIS(&head_lIs, h);

                lIs = head_lIs;

                h = h->next;
        }

        return (0);
}
