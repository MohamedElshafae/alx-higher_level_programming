#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list:linkedList
 * Return:0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p = list;
	int flag = 1;

	if (list == NULL)
		return (0);
	p = p->next;
	while (p != list)
	{
		if (!p)
		{
			flag = 0;
			break;
		}
		p = p->next;
	}
	return (flag);
}
