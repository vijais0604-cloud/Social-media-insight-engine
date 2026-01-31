def detect_crisis(prev, current):
    if prev == 0:
        return False, 0
    increase = ((current - prev) / prev) * 100
    return increase > 200, round(increase, 2)
