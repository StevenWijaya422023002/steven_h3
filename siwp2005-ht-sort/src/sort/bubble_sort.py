class BubbleSort:
    @staticmethod
    def bubble_sort(data):
        for i in range(len(data)-1,-1,-1):
            for j in range(i):
                if data[j]>data[j+1]:
                    temp = data[j]
                    data[j]=data[j+1]
                    data[j+1]=temp


