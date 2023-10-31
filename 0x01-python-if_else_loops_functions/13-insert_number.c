#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *fast = (*head)->next;
	listint_t *slow = (*head);
	listint_t *new;

	new = (listint_t *)malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		while (fast != NULL)
		{
			if (fast->n > number)
				break;
			slow = slow->next;
			fast = fast->next;
		}

		slow->next = new;
		new->next = fast;
	}
	return (new);
}
