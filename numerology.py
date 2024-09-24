def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def find_lucky_moments():
    happy_hours = list(map(int, input().split()))
    happy_minutes = list(map(int, input().split()))

    lucky_moments = []

    for hour in happy_hours:
        for minute in happy_minutes:
            if sum_of_digits(hour)!= sum_of_digits(minute):
                lucky_moments.append(f"{hour:02d}:{minute:02d}")

    lucky_moments.sort()

    for moment in lucky_moments:
        print(moment)

find_lucky_moments()

