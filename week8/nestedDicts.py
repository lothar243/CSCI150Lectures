students_to_scores = {
    'bob': [90, 100, 78],
    'angela': [90, 95, 83],
    'francis': [71, 72, 76]
}


for student, scores in students_to_scores.items():
    print("{:10}".format(student), end=" ")
    for score in scores:
        print("{:5}".format(score), end=" ")
    print("Average: {:5.2f}".format(sum(scores)/len(scores)), end=" ")
    print()
