#include "lists.h"

/**
 * check_cycle - check if
 * @list: the list
 * Return: Int
 */

int check_cycle(listint_t *list)
{
	listint_t *h = list;
    listint_t *_PURE_ = NULL, *_Phead_;

    while (h)
    {
        
        while (_PURE_)
        {
            if (h == _PURE_) 
                return (1);
            
            _PURE_ = _PURE_->next;
        }

        h = h->next;
    }

	return (0); 
}
 