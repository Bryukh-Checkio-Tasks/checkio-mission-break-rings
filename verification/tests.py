"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [4, 6]],
            "answer": 3
        },
        {
            "input": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
            "answer": 3
        },
        {
            "input": [[5, 6], [4, 5], [3, 4], [3, 5], [3, 6]],
            "answer": 2
        },
        {
            "input": [[8, 9], [1, 9], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [8, 7]],
            "answer": 5
        },
    ],
    "Extra": [
        {
            "input": [[8, 7], [1, 9], [2, 7], [3, 6], [1, 7], [5, 7], [3, 4], [9, 5], [9, 6], [3, 5]],
            "answer": 3
        },
        {
            "input": [[3, 4], [1, 6], [1, 2], [9, 5], [2, 5], [9, 2], [8, 3], [2, 4], [8, 4], [1, 3], [8, 1], [1, 7], [6, 7]],
            "answer": 6
        },
        {
            "input": [[5, 7], [9, 4], [1, 2], [9, 5], [1, 3], [9, 3], [9, 6], [1, 5], [2, 3], [3, 7], [9, 7], [8, 6], [3, 4]],
            "answer": 5
        },
        {
            "input": [[1, 9], [1, 2], [8, 5], [4, 6], [5, 6], [8, 1], [3, 4], [2, 6], [9, 6], [8, 4], [8, 3], [5, 7], [9, 7], [2, 3], [1, 7]],
            "answer": 5
        },
        {
            "input": [[1, 3], [3, 4], [3, 5], [4, 6], [6, 7], [8, 3], [8, 1], [2, 6], [8, 4], [9, 5], [4, 5], [1, 7]],
            "answer": 5
        },
        {
            "input": [[9, 5], [5, 6], [2, 6], [4, 5], [8, 2], [1, 3], [1, 4], [9, 4], [1, 2], [9, 2], [8, 7], [8, 3], [8, 6], [2, 3], [8, 9]],
            "answer": 5
        },
        {
            "input": [[9, 7], [9, 6], [8, 5], [8, 3], [8, 9], [5, 7], [4, 5], [8, 4], [1, 7], [9, 4], [1, 5], [2, 5], [4, 6], [8, 2], [1, 2], [2, 4], [8, 7], [8, 1]],
            "answer": 5
        },
        {
            "input": [[3, 4], [5, 6], [2, 7], [1, 5], [2, 6], [8, 4], [1, 7], [4, 5], [9, 5], [2, 3], [8, 2], [2, 4], [9, 6], [5, 7], [3, 6], [1, 3]],
            "answer": 5
        },
        {
            "input": [[2, 5], [3, 7], [5, 6], [6, 7], [9, 6], [8, 9], [9, 7], [1, 4], [1, 9], [9, 5], [2, 4], [2, 6], [2, 3], [9, 2], [3, 6], [4, 5], [1, 2]],
            "answer": 5
        },
        {
            "input": [[1, 4], [4, 7], [9, 3], [8, 2], [4, 6], [3, 4], [2, 3], [8, 9], [5, 7], [9, 5]],
            "answer": 4
        },
        {
            "input": [[1, 3], [8, 4], [4, 6], [3, 7], [8, 2], [1, 2], [8, 9], [4, 5], [8, 1], [1, 9], [1, 7], [1, 6], [2, 5], [9, 6], [2, 4], [9, 2]],
            "answer": 5
        },
        {
            "input": [[9, 7], [9, 4], [9, 3], [2, 6], [2, 5], [3, 7], [4, 6], [1, 3], [1, 4], [8, 9], [3, 5], [5, 7]],
            "answer": 5
        },
        {
            "input": [[1, 4], [4, 7], [9, 2], [2, 6], [5, 6], [8, 1], [3, 7], [9, 3], [3, 6], [8, 6], [1, 7], [2, 4], [1, 9], [8, 3], [9, 6]],
            "answer": 5
        },
        {
            "input": [[1, 2], [3, 7], [2, 3], [3, 5], [1, 4], [2, 5], [9, 3], [5, 7], [1, 9], [8, 4], [1, 3], [2, 6], [9, 4]],
            "answer": 5
        },
        {
            "input": [[4, 6], [2, 5], [1, 6], [6, 7], [2, 6], [8, 7], [2, 4], [4, 7], [9, 3], [3, 7], [8, 3], [2, 7], [9, 6], [4, 5]],
            "answer": 5
        },
    ]
}
