#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include "lists.h"

/**
 * palindrom - main
 * @head: head
 * Return: 0 if it is not a palindrome, else 1
*/

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head));
}

/**
 * aux_palind - main
 * @head: head
 * @end: end
*/

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
