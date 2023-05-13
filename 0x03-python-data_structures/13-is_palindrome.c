#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
 * is_palindrome - function in C that checks if
 * a singly linked list is a palindrome.
 * @head: a head to our linked list
 *
 * Return: 1 if the list pointed to by head is a palindrome
 * 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	size_t size = 0, i = 0, _size = 0, size_cp;
	listint_t *before, *after;

	if (head)
	{
		size_cp = size = listint_len(*head) - 1;

		if (size == 0)
			return (1);

		while (i != size_cp / 2)
		{
			before = get_nodeint_at_index(*head, i++);
			after = get_nodeint_at_index(*head, size--);

			if (!before && !after)
				break;
			if (before->n == after->n)
			{
				_size++;
			}
			else
				break;
		}
		if (_size == size_cp / 2)
			return (1);
		else
			return (0);
	}

	return (1);
}

/**
 * get_nodeint_at_index -  a function that returns the nth node of a
 * listint_t linked list.
 * @head: a pointer to the first element of our linked list
 * @index: is the index of the node, starting at 0
 *
 * Return: if the node does not exist, return NULL, the node otherwise
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i, size = (unsigned int)listint_len(head);
	listint_t *firstnode = head, *node_to_be_returned;

	if (head && (index <= size))
	{
		for (i = 0; i < index; i++)
		{
			head = head->next;
		}
		node_to_be_returned = head;
		head = firstnode;
		return (node_to_be_returned);
	}

	return (NULL);
}

/**
 * listint_len - return the number of elements in a linked list
 * @h: a type listint_t variable whose elements are  to be counted
 *
 * Return: a type size_t value
 */

size_t listint_len(const listint_t *h)
{
	size_t count = 0;

	while (h)
	{
		count++;
		h = h->next;
	}
	return (count);
}
