student_scores={
  "harry":81,
  "ron":78,
  "drave":62
};
student_grades={}
for score in student_scores:
  x=student_scores[score]
  if x>=91 and x<=100:
    student_grades[score]="Outstanding"
  elif x>=81 and x<90:
    student_grades[score]="Exceeds Expectation"
  elif x>=71 and x<=80:
    student_grades[score]="Acceptable"
  else:
    student_grades[score]="Fail"
print(student_grades)
    
