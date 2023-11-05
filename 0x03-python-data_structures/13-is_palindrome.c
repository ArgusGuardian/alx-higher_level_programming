#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - function check list if it's palindrome
 *@head: head of the list to check
 *Return: 1 if it's a palindrome 0 if it's not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int counter = 0;
	int *arr, i = 0, j;

	if (head == NULL && *head == NULL)
		return (1);

	while (current != NULL)
	{
		counter++;
		current = current->next;
	}

	arr = malloc(counter * sizeof(int));
	current = *head;
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0, j = counter - 1; i != j && i < counter / 2; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	return (1);
}
