def birthdayCakeCandles(candles):
    sorted_candles = sorted(candles, reverse=True)
    counter = 0
    start = sorted_candles[0]
    for candle in sorted_candles:
        if candle == start:
            counter += 1
        else:
            break
    return counter