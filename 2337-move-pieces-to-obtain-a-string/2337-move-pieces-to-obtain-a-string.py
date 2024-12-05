class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Step 1: Remove '_' and check if the sequence of 'L' and 'R' matches
        start_filtered = ''.join([c for c in start if c != '_'])
        target_filtered = ''.join([c for c in target if c != '_'])
        
        if start_filtered != target_filtered:
            return False
        
        # Step 2: Check movement constraints for 'L' and 'R'
        start_pos, target_pos = 0, 0
        n = len(start)
        
        while start_pos < n and target_pos < n:
            # Skip '_' in start
            while start_pos < n and start[start_pos] == '_':
                start_pos += 1
            # Skip '_' in target
            while target_pos < n and target[target_pos] == '_':
                target_pos += 1
            
            # If one of them is exhausted, the strings must be aligned
            if start_pos == n or target_pos == n:
                return start_pos == target_pos
            
            # Validate positions of 'L' and 'R'
            if start[start_pos] != target[target_pos]:
                return False
            if start[start_pos] == 'L' and start_pos < target_pos:
                return False
            if start[start_pos] == 'R' and start_pos > target_pos:
                return False
            
            # Move both pointers
            start_pos += 1
            target_pos += 1
        
        return True
