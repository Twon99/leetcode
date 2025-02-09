class NumberContainers(object):

    def __init__(self):
        self.index_to_number = {}  # Maps index to number
        self.number_to_indices = defaultdict(set)  # Maps number to a set of indices
        self.min_heap = defaultdict(list)  # Min-heap to keep track of smallest index per number

    def change(self, index, number):
        """
        :type index: int
        :type number: int
        :rtype: None
        """
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
        # Remove index from old number's set
            self.number_to_indices[old_number].discard(index)
        # Clean up if the set is empty
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        # Update index to the new number
        self.index_to_number[index] = number
        # Add index to the new number's set
        self.number_to_indices[number].add(index)
        # Push index into the min-heap for number
        heapq.heappush(self.min_heap[number], index)
    def find(self, number):
        """
        :type number: int
        :rtype: int
        """
        if number not in self.number_to_indices:
            return -1

        # Remove stale indices from heap (if they were removed from number_to_indices)
        while self.min_heap[number] and self.min_heap[number][0] not in self.number_to_indices[number]:
            heapq.heappop(self.min_heap[number])

        # Return the smallest valid index or -1 if none exist
        return self.min_heap[number][0] if self.min_heap[number] else -1
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)