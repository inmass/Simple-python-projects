import random
def yahtzee(result = [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]):
    reps = [result.count(1),result.count(2),result.count(3),result.count(4),result.count(5),result.count(6)]
    repsnum = [result.count(1)*1,result.count(2)*2,result.count(3)*3,result.count(4)*4,result.count(5)*5,result.count(6)*6]
    repeated= []
    for x in reps:
        if x > 1:
            repeated.append(x)
    if reps.count(1) == 5:
        score = max(result)
    elif len(repeated) == 1:
        score = repeated[0]*(reps.index(repeated[0])+1)
    else:
        score = max(repsnum)
    s = ", ".join(map(str,result))
    return f'Your result is {s}.\nYour score is {score}.'

print(yahtzee())
