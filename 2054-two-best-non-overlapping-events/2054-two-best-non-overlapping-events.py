from typing import List
from bisect import bisect_left

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by their end time
        events.sort(key=lambda x: x[1])
        
        # Prepare to store the maximum value so far and initialize result
        max_value_so_far = 0
        max_result = 0
        
        # Create a sorted list of tuples (endTime, max_value_up_to_this_event)
        max_values = []
        
        for start, end, value in events:
            # Find the last event that ends before the current event's start time
            idx = bisect_left(max_values, (start,)) - 1
            
            # Calculate the sum of values if we include a non-overlapping previous event
            current_sum = value
            if idx >= 0:
                current_sum += max_values[idx][1]
            
            # Update the maximum result found so far
            max_result = max(max_result, current_sum)
            
            # Update the running max value up to this event
            max_value_so_far = max(max_value_so_far, value)
            max_values.append((end, max_value_so_far))
        
        return max_result
