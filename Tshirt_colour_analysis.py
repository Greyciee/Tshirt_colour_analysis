from collections import Counter

# Combine all colours into one list
all_colours = [
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 
    'ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',
    'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
    'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE',
    'BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM',
    'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN',
    'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED',
    'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE'
]

# Count how often each colour appears
colour_count = Counter(all_colours)

""" QUESTION 1:

Find the most common colour (mean colour)"""
mean_colour = colour_count.most_common(1)[0][0]
print("Mean Colour:", mean_colour)


""" QUESTION 2:

 Most worn colour is the same as mean colour in this case"""
most_worn_colour = colour_count.most_common(1)[0][0]
print("Most Worn Colour:", most_worn_colour)


""" QUESTION 3:

Sort the colours and find the middle one( median)"""
sorted_colours = sorted(all_colours)
n = len(sorted_colours)
median_colour = sorted_colours[n // 2] if n % 2 == 1 else sorted_colours[(n // 2) - 1]
print("Median Colour:", median_colour)


"""QUESTION 4:

Calculate variance. This doesn't apply well to categorical data (colours), so it wii be skipped.
"""


""" QUESTION 5:
calculate the probability of choosing the colour red"""
probability_red = colour_count['RED'] / len(all_colours)
print("Probability of Red:", probability_red)


"""QUESTION 6:

 colors and frequencies in PostgreSQL database"""
import psycopg2


color_count = {
    'GREEN': 6,
    'YELLOW': 3,
    'BROWN': 5,
    'BLUE': 16,
    'PINK': 3,
    'ORANGE': 4,
    'CREAM': 2,
    'RED': 5,
    'WHITE': 13,
    'BLACK': 1
}

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="color_analysis",
    user="postgres",    
    password="utobuiro",  
    host="localhost"
)
cursor = conn.cursor()

# Insert data into the table
for color, freq in color_count.items():
    cursor.execute('''
        INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s)
        ON CONFLICT (color) DO UPDATE SET frequency = excluded.frequency
    ''', (color, freq))

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

"""QUESTION 7:


Recursive search algorithm"""
def recursive_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursive_search(arr, target, low, mid - 1)
        else:
            return recursive_search(arr, target, mid + 1, high)
    return -1

numbers = list(range(1, 11))  # List of numbers from 1 to 10
target_number = int(input("Enter a number to search: "))
index = recursive_search(numbers, target_number, 0, len(numbers) - 1)
print("Number found at index:", index if index != -1 else "not found")



"""QUESTION 8:

random 4 digits number of 0s and 1s """
import random

binary_number = ''.join(random.choices('01', k=4))
base10_number = int(binary_number, 2)
print("Random 4-digit binary number:", binary_number)
print("Base 10 equivalent:", base10_number)



"""QUESTION 9:

Sum of the first 50 Fibonacci numbers"""
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

print("Sum of first 50 Fibonacci numbers:", fibonacci_sum(50))
