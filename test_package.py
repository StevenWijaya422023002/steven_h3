import siwp2005_steven_wijaya_sorting.bubble_sort as bubble_sort
import siwp2005_steven_wijaya_sorting.insertion_sort as insertion_sort
import siwp2005_steven_wijaya_sorting.quick_sort as quick_sort

data = [1, 6, 8, 4, 12, 34, 2]

sorted_data_bubble = bubble_sort.bubble_sort(data)
print("Bubble Sort:", sorted_data_bubble)

sorted_data_insertion = insertion_sort.insertion_sort(data)
print("Insertion Sort:", sorted_data_insertion)

sorted_data_quick = quick_sort.quick_sort(data)
print("Quick Sort:", sorted_data_quick)


