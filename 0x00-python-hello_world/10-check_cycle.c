#include "lists.h"
/**
 * check_cycle - function that checkes wether there's a loop
 * @list: head of the linked list
 * Return: 0 if not 1 if there's a loop
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
