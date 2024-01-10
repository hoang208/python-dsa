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

'''
Solution
    Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:
        Create a variable position with the value 0.
        Check whether the number at index position in card equals query.
        If it does, position is the answer and can be returned from the function
        If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
        If the number was not found, return -1.
'''

def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

# Test
# for test in tests:
#     print (locate_card(**test['input']) == test['output'])

'''
At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. This is called a brute force approach.
It would be great if Bob could somehow guess the card at the first attempt, but with all the cards turned over it's simply impossible to guess the right card.
The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it.
In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list.
Then, we can simply repeat the process with each half. This technique is called binary search.
Here's how binary search can be applied to our problem:
    Find the middle element of the list.
    If it matches queried number, return the middle position as the answer.
    If it is less than the queried number, then search the first half of the list
    If it is greater than the queried number, then search the second half of the list
    If no more elements remain, return -1.
'''

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'

def locate_card2(cards, query):
    lo, hi = 0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

# Test
# for test in tests:
#     print (locate_card2(**test['input']) == test['output'])

'''
Generic Binary Search
Here is the general strategy behind binary search, which is applicable to a variety of problems:
    Come up with a condition to determine whether the answer lies before, after or at a given position
    Retrieve the midpoint and the middle element of the list.
    If it is the answer, return the middle position as the answer.
    If answer lies before it, repeat the search with the first half of the list
    If the answer lies after it, repeat the search with the second half of the list.
'''

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# We can now rewrite the locate_card function more succinctly using the binary_search function.
def locate_card3(cards, query):
    
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'
    
    return binary_search(0, len(cards) - 1, condition)

# Test
for test in tests:
    print (locate_card3(**test['input']) == test['output'])

