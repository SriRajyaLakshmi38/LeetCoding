class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_pos, target_pos = 0, 0
        
        while start_pos < n or target_pos < n:
            # Skip '_' in start
            while start_pos < n and start[start_pos] == '_':
                start_pos += 1
            # Skip '_' in target
            while target_pos < n and target[target_pos] == '_':
                target_pos += 1
            
            # If one pointer reaches the end, both should
            if start_pos == n or target_pos == n:
                return start_pos == target_pos
            
            # Check if the pieces match at current positions
            if start[start_pos] != target[target_pos]:
                return False
            
            # Check movement constraints
            if start[start_pos] == 'L' and start_pos < target_pos:
                return False
            if start[start_pos] == 'R' and start_pos > target_pos:
                return False
            
            # Move both pointers to the next character
            start_pos += 1
            target_pos += 1
        
        return True
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        start_pos, target_pos = 0, 0
        
        while start_pos < n or target_pos < n:
            # Skip '_' in start
            while start_pos < n and start[start_pos] == '_':
                start_pos += 1
            # Skip '_' in target
            while target_pos < n and target[target_pos] == '_':
                target_pos += 1
            
            # If one pointer reaches the end, both should
            if start_pos == n or target_pos == n:
                return start_pos == target_pos
            
            # Check if the pieces match at current positions
            if start[start_pos] != target[target_pos]:
                return False
            
            # Check movement constraints
            if start[start_pos] == 'L' and start_pos < target_pos:
                return False
            if start[start_pos] == 'R' and start_pos > target_pos:
                return False
            
            # Move both pointers to the next character
            start_pos += 1
            target_pos += 1
        
        return True
