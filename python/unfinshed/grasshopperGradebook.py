# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python

def get_grade(s1, s2, s3):
    # Code her
    # e
    avg_score = sum([s1, s2, s3]) / 3
    score = ''

    if (90 <= avg_score and avg_score <= 100):
        score = 'A'
    elif (80 <= avg_score and avg_score < 90):
        score = 'B'
    elif (70 <= avg_score and avg_score < 80):
        score = 'C'
    elif (60 <= avg_score and avg_score < 70):
        score = 'D'
    elif (0 <= avg_score and avg_score < 60):
        score = 'F'
    else:
        score = 'Error'
    return score
