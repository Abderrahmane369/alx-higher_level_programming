#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t _size = PyList_Size(p);
    Py_ssize_t _alloctd = ((PyListObject *)p)->allocated;

    Py_ssize_t _;

    printf("[*] Size of the Python List = %zd\n", _size);
    printf("[*] Allocated = %zd\n", _alloctd);

    for (_ = 0; _ < _size; _++)
    {
        printf("Element %zd: %s", _, PyUnicdoe_AsUTF8(PyObject_Repr()))
    }
}