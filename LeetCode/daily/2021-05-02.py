"""
https://leetcode.com/submissions/detail/488571033/?from=explore&item_id=3729
"""
"""
97 / 97 test cases passed.
Status: Accepted
Runtime: 1684 ms
Memory Usage: 19.3 MB
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda c: c[1])
        currentDuration = []
        currentTotalTime = 0
        for course in courses:
            if course[0] > course[1]:
                continue
            deadline = currentTotalTime + course[0]
            if deadline <= course[1]:
                currentTotalTime = deadline
                currentDuration.append(course[0])
                continue
            cMax = max(currentDuration)
            if course[0] < cMax:
                currentTotalTime += course[0] - cMax
                currentDuration.remove(cMax)
                currentDuration.append(course[0])
        return len(currentDuration)
      
