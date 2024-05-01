# File System - System Design Interview Question (Pseudocode)

# You are asked to design a file system that allows you to create new paths and associate them with different values.

# The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters.
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

# Implement the FileSystem class:

# bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true.
# Returns false if the path already exists or its parent path doesn't exist.

# int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.



# Requirements:
#   - File system
#   - File paths are lowercase letters, concatenated with "/".

# Methods
# createPath(path: str, value: int): Must be able to create a new path and associate a retrievable value with it.
#   - Returns True if new path is created (and value becomes associated with that path)
#   - Returns False if path already exists or parent path doesn't exist.

# get(path: str): Must be able to retrieve the value associated with path.


# createPath and get both have similar error handling:
#   - get: return -1 whenever we can't traverse deep enough into the folder structure (based on the filepath given).
#   - createPath: return True if filepath can be added, False if 1) it already exists or 2) the parent path doesn't exist.
#       - For 2nd case, we need to check that all of the path BEFORE the final one already exist.

class FileSystem:
    def __init__(self):
        self.files = {} # Paths will be nested in this data structure, somewhat like a trie (tree-like structure).


    def createPath(self, path: str, value: int):
        # Add the path.
        paths = path.split("/") # Split each path by "/". We can avoid using these in the actual data structure.
        fileLevel = self.files

        for i, path in enumerate(paths):
            if i == len(paths) - 1: # Final elem of path.
                if path in fileLevel:
                    return False
                else:
                    fileLevel[path] = {"*": value}
                    return True


    def get(self, path: str):
        # Retrieve the value from the specified path.

        paths = path.split("/") # Split each path by "/". We can avoid using these in the actual data structure.

        fileLevel = self.files

        for path in paths:
            if path:
                # print("path", path)
                if path not in fileLevel:
                    return -1
                fileLevel = fileLevel[path]


        if "*" in fileLevel:
            return fileLevel["*"]
        else:
            return -1

# fileSystem = FileSystem()
# print(fileSystem.createPath("/a", 1)) # return true
# print(fileSystem.get("/a")) # return 1


# Input:
# ["FileSystem","createPath","createPath","get","createPath","get"]
# [[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
# Output:
# [null,true,true,2,false,-1]
# Explanation:
fileSystem = FileSystem()
print(fileSystem.createPath("/leet", 1)) # return true
print(fileSystem.createPath("/leet/code", 2)) # return true
print(fileSystem.get("/leet/code")) # return 2
print(fileSystem.createPath("/c/d", 1)) # return false because the parent path "/c" doesn't exist.
print(fileSystem.get("/c")) # return -1 because this path doesn't exist.