import unittest

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is")
    print_list(arr)
    merge_sort(arr)
    print("Sorted array is")
    print_list(arr)

class TestMergeSort(unittest.TestCase):

    def test_positive_cases(self):
        self.assertEqual(merge_sort([12, 11, 13, 5, 6, 7]), [5, 6, 7, 11, 12, 13])
        self.assertEqual(merge_sort([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sort([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])

    def test_negative_cases(self):
        with self.assertRaises(TypeError):
            merge_sort(123)
            merge_sort("123")
            merge_sort([1, 2, 3, "4", 5, 6])

    def test_performance_cases(self):
        large_array = list(range(10000, 0, -1))
        sorted_large_array = list(range(1, 10001))
        self.assertEqual(merge_sort(large_array), sorted_large_array)

    def test_boundary_cases(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([1, 2]), [1, 2])

    def test_idepotency(self):
        arr = [12, 11, 13, 5, 6, 7]
        self.assertEqual(merge_sort(arr), [5, 6, 7, 11, 12, 13])
        self.assertEqual(merge_sort(arr), [5, 6, 7, 11, 12, 13])

if __name__ == "__main__":
    unittest.main()