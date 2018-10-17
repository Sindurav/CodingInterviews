# Write the regular expression
# in the blank space below
from os import environ
from re import compile
from re import match

regularExpression = "^([a-z]{1,6}_?)([a-z]?[a-z]?[a-z]?[a-z]?)@hackerrank.com$"

pattern = compile(regularExpression)

query = int(input())
result = ['False'] * query

for i in range(query):
    someString = input()

    if pattern.match(someString):
        result[i] = 'True'

print(result)
