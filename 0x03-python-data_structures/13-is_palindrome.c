#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);
	listint_t *p = *head;
	int len = 0;

	while (p)
	{
		len++;
		p = p->next;
	}
	int arr[len], i = 0;

	p = *head;
	while (p)
	{
		arr[i] = p->n;
		p = p->next;
		i++;
	}
	int flag = 1;

	for (i = 0; i < len / 2 ; i++)
	{
		if (arr[i] != arr[len - i - 1])
		{
			flag = 0;
			break;
		}
		flag = 1;
	}
	return (flag);
}
