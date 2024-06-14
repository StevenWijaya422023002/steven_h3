class QuickSort:
    @staticmethod
    def quick_sort(data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return QuickSort.quick_sort(left) + middle + QuickSort.quick_sort(right)
