#include <stdio.h>
#include <Python.h>

/**
 * print_bytes_info - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_bytes_info(PyObject *p)
{
	char *byte_string;
	long int byte_size, i, limit;

	printf("[.] Bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)(p))->ob_size;
	byte_string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", byte_size);
	printf("  trying string: %s\n", byte_string);

	if (byte_size >= 10)
		limit = 10;
	else
		limit = byte_size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	{
		if (byte_string[i] >= 0)
			printf(" %02x", byte_string[i]);
		else
			printf(" %02x", 256 + byte_string[i]);
	}

	printf("\n");
}

/**
 * print_list_info - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_list_info(PyObject *p)
{
	long int list_size, i;
	PyListObject *list;
	PyObject *element;

	list_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((element)->ob_type)->tp_name);
		if (PyBytes_Check(element))
			print_bytes_info(element);
	}
}
