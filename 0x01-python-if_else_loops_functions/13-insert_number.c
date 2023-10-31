#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of the node
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp = *head;
    listint_t *new;

    new = (listint_t *)malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (*head == NULL || new->n < (*head)->n)
    {
        new->next = *head;
        *head = new;
        return (*head);
    }

    while (tmp->next != NULL && new->n > tmp->next->n)
        tmp = tmp->next;

    new->next = tmp->next;
    tmp->next = new;

    return (new);
}
