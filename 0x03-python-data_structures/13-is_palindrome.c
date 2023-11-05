#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;
	listint_t *prev = NULL, *current = dup, *next = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	dup = prev;
	while (dup && temp)
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	if (!dup)
		return (1);
	return (0);
}
