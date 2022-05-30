""" Complete the solution so that it reverses the string passed into it. """

def solution(string):
  result = ""
  for index in reversed(range(len(string))):
    result += str(string[index])
  return result

print(solution("Hello World"))
