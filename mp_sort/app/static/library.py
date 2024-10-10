# flake8: noqa
from org.transcrypt.stubs.browser import document, window, console  # type: ignore
import random


def gen_random_int(number, seed):
    """
    This function generates a list of random integers, from 0 to 100.
    """

    # set the seed
    random.seed(seed)

    # create an empty list
    array = []

    # loop through the number of times given
    for i in range(number):
        array.append(random.randint(0, 100))

    return array


def array_to_string(array: list[int]) -> str:
    """
    Convert the list of integers into a string.
    """
    return ", ".join(str(x) for x in array) + "."


def string_to_array(string: str) -> list[int]:
    """
    Convert the string into a list of integers.
    """
    return list(  # finally convert it to a list
        # map over the list of strings and convert them to integers
        map(
            int,
            # remove the last character which is a period
            string[:-1]
            .split(", ")
        )
    )


def quick_sort(array: list[int]) -> tuple[list[int], int, int]:
    """
    This function sorts the list of integers using quick sort.
    """
    swaps = 0
    comparisons = 0

    def partition(array: list[int], low: int, high: int) -> int:
        nonlocal swaps, comparisons
        i = low - 1
        pivot = array[high]
        for j in range(low, high):
            comparisons += 1
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                swaps += 1
        array[i + 1], array[high] = array[high], array[i + 1]
        swaps += 1
        return i + 1

    def quick_sort_helper(array: list[int], low: int, high: int) -> None:
        nonlocal swaps, comparisons
        if low < high:
            pi = partition(array, low, high)
            quick_sort_helper(array, low, pi - 1)
            quick_sort_helper(array, pi + 1, high)

    quick_sort_helper(array, 0, len(array) - 1)
    return array, swaps, comparisons


def bubble_sort(array: list[int]) -> tuple[list[int], int, int]:
    """
    This function sorts the list of integers using bubble sort.
    """
    swaps = 0
    comparisons = 0
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return array, swaps, comparisons


def insertion_sort(array: list[int]) -> tuple[list[int], int, int]:
    """
    This function sorts the list of integers using insertion sort.
    """
    swaps = 0
    comparisons = 0
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            swaps += 1
            comparisons += 2
        array[j + 1] = key
    return array, swaps, comparisons


def pogo_sort(array: list[int]) -> tuple[list[int], int, int]:
    """
    This function sorts the list of integers using pogo sort.
    This is a joke algorithm and should not be used in production.
    """
    swaps = 0
    comparisons = 0
    n = len(array)

    def is_sorted(array: list[int]) -> bool:
        comparisons += n - 1
        return all(array[i] <= array[i + 1] for i in range(n - 1))

    while not is_sorted(array):
        # pick two random indices and swap them
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        # if left index is greater than right index, swap them
        comparisons += 1
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]
            swaps += 1

    return array, swaps, comparisons


def generate():
    number = 10
    seed = 200

    # call gen_random_int() with the given number and seed
    # store it to the variable array

    array = gen_random_int(number, seed)

    console.log(array)

    # convert the items into one single string
    # the number should be separated by a comma
    # and a full stop should end the string.

    array_str = array_to_string(array)

    # This line is to placed the string into the HTML
    # under div section with the id called "generate"
    document.getElementById("generate").innerHTML = array_str  # type: ignore


ALGO_MAP = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Pogo Sort": pogo_sort
}


def sortnumber1():
    '''	This function is used in Exercise 1.
            The function is called when the sort button is clicked.

            You need to do the following:
            - get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
            - create a list of integers from the string of numbers
            - call your sort function, either bubble sort or insertion sort
            - create a string of the sorted numbers and store it in array_str
    '''

    unsafe_generated_number_list_str = document.getElementById(
        "generate").innerHTML

    assert isinstance(unsafe_generated_number_list_str, str)

    generated_number_list = string_to_array(unsafe_generated_number_list_str)

    sorted_generated_number_list, _ = bubble_sort(generated_number_list)

    array_str = array_to_string(sorted_generated_number_list)

    document.getElementById("sorted").innerHTML = array_str

    # Lets have fun and benchmark each algorithm

    _sort_results = list(map(
        lambda x: (x, ALGO_MAP[x](string_to_array(
            unsafe_generated_number_list_str))),
        ALGO_MAP.keys()
    ))

    document.getElementById("benchmark").innerHTML = ''.join(map(
        lambda x: f"<tr class='benchmark-item'><td>{x[0]}</td><td><label>Swaps</label><div class='numbers'>{x[1][1]}</div></td><td><label>Comparisons</label><div class='numbers'>{x[1][2]}</div></td></tr>",
        _sort_results
    ))


def sortnumber2():
    '''	This function is used in Exercise 2.
            The function is called when the sort button is clicked.

            You need to do the following:
            - Get the numbers from a string variable "value".
            - Split the string using comma as the separator and convert them to 
                    a list of numbers
            - call your sort function, either bubble sort or insertion sort
            - create a string of the sorted numbers and store it in array_str
    '''
    # The following line get the value of the text input called "numbers"
    value = document.getElementsByName("numbers")[0].value

    # Throw alert and stop if nothing in the text input
    if value == "":
        window.alert("Your textbox is empty")
        return

    # Your code should start from here
    # store the final string to the variable array_str

    number_list = list(  # finally convert it to a list
        # map over the list of strings and convert them to integers
        map(
            int,
            value
            .split(",")
        )
    )

    sorted_generated_number_list, _ = bubble_sort(number_list)

    array_str = array_to_string(sorted_generated_number_list)

    document.getElementById("sorted").innerHTML = array_str
