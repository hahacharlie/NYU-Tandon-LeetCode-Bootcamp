'''
Problem: You are given a series of video clips from a sporting event that lasted time seconds. 
        These video clips can be overlapping with each other and have varying lengths.
        Each video clip is described by an array clips where clips[i] = [start_i, end_i] indicates that the ith clip started at start_i and ended at end_i.
        We can cut these clips into segments freely.
            For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
        Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. 
        If the task is impossible, return -1.
'''
class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:

        # Sort the clips by their start time
        clips.sort()
        
        # Use two pointers: end to track the end of the current interval we are covering and 
        # newEnd to track the farthest end we can reach with the current set of clips.
        end, newEnd, requiredClips = 0, 0, 0
        
        # iterator
        i = 0

        # Iterate through the sorted clips, and for each group of clips that start 
        # before or at the current end, update newEnd to be the maximum of the current newEnd 
        # and the clip's end time.
        while i < len(clips) and end < time:
        # While there are clips and the end of last selected clip is less than T
            while i < len(clips) and clips[i][0] <= end:
                # Extend the farthest reach within the current interval
                newEnd = max(newEnd, clips[i][1])
                i += 1
        
            if end == newEnd:
                return -1  # Cannot extend the coverage
            end = newEnd  # Extend the interval to the farthest reach
            requiredClips += 1  # One more clip is used
    
        return requiredClips if end >= time else -1