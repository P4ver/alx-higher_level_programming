#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - function in C that checks if a
 *	singly linked list has a cycle in it,
 * @list: pntr to check,
 * Return: 0 if no cycle, 1 if there is a cycle,
 **/
int check_cycle(listint_t *list)
{
	listint_t *sl_w = list, *fs_t = list->next;

	if (list == NULL || list->next == NULL)
		return (0);
	while (fs_t != NULL && fs_t->next != NULL)
	{
		if (sl_w == fs_t)
			return (1);
		sl_w = sl_w->next;
		fs_t = fs_t->next->next;
	}
	return (0);
}
