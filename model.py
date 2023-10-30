# This is where we could possibly place out functions when comparing the users input with the correct answer.
def processform(form):
  # correct_ans = [('Q1','c'),('Q2','c'),('Q3','b'),('Q4','a'),('Q5','a')]
  correct_ans = {"Q1": "c","Q2": "c","Q3": "b","Q4": "a","Q5": "a"}
  score = 0
  for question in correct_ans:
    if form[question] == correct_ans[question]:
      score += 10

  result1 = "You scored " + str(score) + " points!"
  # print correct answers
  result2 = ""
  # print your answers
  result3 = ""

  for i in correct_ans:
    curr = i + ")" + correct_ans[i]
    result2 += curr + " "

  for i in form:
    curr = i + ")" + form[i]
    result3 += curr + " "
  
  return result1, result2, result3