# Python pickle module is used for serializing and de-serializing python object structures.
# The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) is called
# pickling or serialization or flattening or marshalling. We can convert the byte stream (generated through pickling)
# back into python objects by a process called as unpickling
import pickle


def fun1():
    mylist = ['a', 'b', 'c', 'd']
    with open('datafile.pickle', 'wb') as fh:
        pickle.dump(mylist, fh)
    pickle_off = open("datafile.pickle", "rb")
    emp = pickle.load(pickle_off)
    return emp


def fun2():
    emp_id = {1: "Zack", 2: "53050", 3: "IT", 4: "38", 5: "Flipkart"}
    pickling_on = open("EmpID.pickle", "wb")
    pickle.dump(emp_id, pickling_on)
    pickling_on.close()
    pickle_off = open("EmpID.pickle", 'rb')
    emp_id = pickle.load(pickle_off)
    return emp_id


if __name__ == '__main__':
    print(fun1())
    print(fun2())
