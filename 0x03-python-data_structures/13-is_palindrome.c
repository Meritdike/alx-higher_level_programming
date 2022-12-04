#include "lists.h"

listint_t *check_palindrome(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * check_palindrome - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *check_palindrome(listint_t **head)
{
    listint_t *node = *head, *next, *prev = NULL;

    while (node)
    {
        next = node->next;
        node->next = prev;
        prev = node;
        node = next;
    }

    *head = prev;
    return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
    listint_t *start, *rev, *mid;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    start = *head;
    while (start)
    {
        size++;
        start = start->next;
    }

    start = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        start = start->next;

    if ((size % 2) == 0 && start->n != start->next->n)
        return (0);

    start = start->next->next;
    rev = check_palindrome(&start);
    mid = rev;

    start = *head;
    while (rev)
    {
        if (start->n != rev->n)
            return (0);
        start = start->next;
        rev = rev->next;
    }
    check_palindrome(&mid);

    return (1);
}
