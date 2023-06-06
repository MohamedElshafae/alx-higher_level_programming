#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head:the linkedlist
 * @number: data which insert in list
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *p = *head;

	temp = malloc(sizeof(listint_t));
	if (!temp)
		return (NULL);
	temp->n = number;
	if (!*head)
	{
		*head = temp;
		return (temp);
	}
	if (number < p->n)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}
	while (p)
	{
		if (!p->next)
		{
			p->next = temp;
			return (temp);
		}
		if (number <= p->next->n)
		{
			temp->next = p->next;
			p->next = temp;
			return (temp);
		}
		p = p->next;
	}
	return (NULL);
}
