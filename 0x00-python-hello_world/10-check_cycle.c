#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list:linkedList
 * Return:0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *cur = list, *n = list->next;

	if (list == NULL)
		return (0);

	while (cur && n->next)
	{
		cur = cur->next;
		n = cur->next->next;
		if (cur == n)
			return (1);
	}
	return (0);
}
