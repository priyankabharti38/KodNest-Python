original_scores=[]
for i in range(3):
    score=int(input())
    original_scores.append(score)

replacement_score=int(input())
additional_score=int(input())
alias_score=original_scores
alias_score[0]=replacement_score
alias_score.append(additional_score)
print(f"Original Score:{original_scores}")
print(f"alias Score:{alias_score}")
print(f"reference:{original_scores is alias_score}")

