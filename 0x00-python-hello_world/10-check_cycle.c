#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p, *slow_p;

	if (list == NULL || list->next == NULL)
		return (0);

	slow_p = list->next;
	fast_p = list->next->next;

	while (slow_p && fast_p && fast_p->next)
	{
		if (fast_p == slow_p)
			return (1);

		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
	}

	return (0);
}
