#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *p;
	p = *head;

	if (!head || !*head)
		return (1);

	int arr[2000] = {0};
	int len;

	len = 0;
	while (p)
	{
		len++;
		p = p->next;
	}
	int i, flag;

	flag = 1;
	i = 0;

	p = *head;
	while (p)
	{
		arr[i] = p->n;
		p = p->next;
		i++;
	}
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
