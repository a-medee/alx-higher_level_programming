#include "lists.h"
#include <python3.4m/Python.h>
#include <python3.4m/listobject.h>
#include <python3.4m/object.h>

/**
 * print_python_list_info - prints some basic info about Python
 * list
 * @p: a Pyobject type element
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *o = (PyListObject *) p;
	Py_ssize_t i;

	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", o->allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		printf("Element %ld: ", i);
		printf("%s\n", o->ob_item[i]->ob_type->tp_name);
	}
}
