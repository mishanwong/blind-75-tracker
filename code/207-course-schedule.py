from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        white = set(graph.keys())
        grey = set()
        black = set()
        def dfs(course, grey, black):
            grey.add(course)
            for prereq in graph[course]:
                if prereq in black:
                    continue
                if prereq in grey:
                    return False

                if not dfs(prereq, grey, black):
                    return False

            grey.remove(course)
            black.add(course)
            return True
        while white:
            course = white.pop()

            if not dfs(course, grey, black):
                return False
        return True
        
            