#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * node_int - function adding node,
 * @head: pntr to head,
 * @n: integer,
 * Return: return an elemznt address,
 */
listint_t *node_int(listint_t **head, const int n)
{
	listint_t *nwnd;

	nwnd = malloc(sizeof(listint_t));
	if (nwnd == NULL)
		return (NULL);
	nwnd->n = n;
	nwnd->next = *head;
	*head = nwnd;
	return (nwnd);
}
/**
 * is_palindrome - function in C that checks if a singly linked list,
 * @head: pntr to head,
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome,
 */
int is_palindrome(listint_t **head)
{
	listint_t *rvrs = NULL, *sl_w = *head, *f_st = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (f_st != NULL && f_st->next != NULL)
	{
		node_int(&rvrs, sl_w->n);
		sl_w = sl_w->next;
		f_st = f_st->next->next;
	}
	if (f_st != NULL)
		sl_w = sl_w->next;
	while (sl_w != NULL)
	{
		if (sl_w->n != rvrs->n)
		{
			free_listint(rvrs);
			return (0);
		}
		sl_w = sl_w->next;
		rvrs = rvrs->next;
	}
	free_listint(rvrs);
	return (1);
}
