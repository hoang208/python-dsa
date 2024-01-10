'''
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
'''

'''
Can represent the sequence of cards as a list of numbers.
Turning over a specific card is equivalent to accessing the value of the number at the corresponding position the list.
'''

'''
Input
    cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
    query: A number, whose position in the array is to be determined. E.g. 7
Output
    position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)
Signature
    def locate_card(cards, query):
        pass
'''

'''
Test Case
    test = {
        'input': { 
            'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
            'query': 7
        },
        'output': 3
    }
The function can now be tested as follows.
    locate_card(**test['input']) == test['output']
'''

'''
Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:
    The number query occurs somewhere in the middle of the list cards.
    query is the first element in cards.
    query is the last element in cards.
    The list cards contains just one element, which is query.
    The list cards does not contain number query.
    The list cards is empty.
    The list cards contains repeating numbers.
    The number query occurs at more than one position in cards.
'''

tests = []

# query occurs in the middle
tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

# query is the first element
tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

# query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

# cards contains just one element, query
tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

# cards does not contain query 
tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

# cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

# query occurs multiple times
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})