class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        frequency_dict = {}
    
        # Loop through each character in the string
        for char in s1:
            # If the character is already in the dictionary, increment its count
            if char in frequency_dict:
                frequency_dict[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
            else:
                frequency_dict[char] = 1
        print(frequency_dict)
        i = 0 
        j = len(s1) - 1
        window_frequency = {}
        #dq = deque()
        #dq.append(s2[i])
        #while(j < len(s1)):
            #dq.append(s2[j])
        for char in s2[i:j+1]:
            if char in window_frequency:
                window_frequency[char] += 1
            else:
                window_frequency[char] = 1
        #j = len(s1)
        #print(window_frequency)
        while( j < len(s2) ):
            
            if window_frequency == frequency_dict:
                print("window",window_frequency )
                print("frequency_dict", frequency_dict)
                
                return True
                
            else:
                #print("i = ", str(i) + "s[i] = ", str(s2[i]))
                #print(window_frequency)
                #if s2[i] in window_frequency:
                window_frequency[s2[i]] -= 1

                    
                if window_frequency[s2[i]] == 0:
                    del window_frequency[s2[i]]
                i = i + 1
                j = j + 1
                if j >= len(s2):
                    break
                if s2[j] in window_frequency:
                    window_frequency[s2[j]] += 1
                else:
                    window_frequency[s2[j]] = 1
                #print("j = ", str(j) + "s[j] = ", str(s2[j]))
                #print(window_frequency)
               
        return False
                