import math


def UpdateStd(OldMean, OldStd, NewMean, NewDataValue, n, A):
    oldvariance = OldStd**2
    newVariance = (
        (n - 1) * oldvariance + (NewDataValue - OldMean) * (NewDataValue - NewMean)
    ) / n
    NewStd = math.sqrt(newVariance)
    return NewStd


def UpdateMean(OldMean, NewDataValue, n, A):
    datasum = OldMean * n + NewDataValue
    NewMean = datasum / (n + 1)
    return NewMean


def UpdateMedian(OldMedian, NewDataValue, n, A):  # if array is not sorted
    A.append(NewDataValue)
    A.sort()
    n += 1
    if n % 2 == 1:
        # If the number of elements is odd, the median is the middle element
        new_median = A[n // 2]
    else:
        # If the number of elements is even, the median is the average of the two middle elements
        new_median = (A[n // 2 - 1] + A[n // 2]) / 2.0
    return new_median


def UpdateMedian1(OldMedian, NewDataValue, n, A):  # if array issorted
    from bisect import insort

    # Insert the new value into the sorted list A
    insort(A, NewDataValue)
    n += 1
    if n % 2 == 1:
        # If the number of elements is odd, the median is the middle element
        new_median = A[n // 2]
    else:
        # If the number of elements is even, the median is the average of the two middle elements
        new_median = (A[n // 2 - 1] + A[n // 2]) / 2.0

    return new_median
