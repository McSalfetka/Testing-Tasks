n1, m1, n2, m2 = map(int, input().split())
print(n1, m1, n2, m2)

stroke1 = "1"
stroke2 = "1"

first1 = 1
first2 = 1
last1 = m1
last2 = m2
end1 = False
end2 = False

while not end1 or not end2:
    if last1 != 1:
        if first1 + (m1-1) > n1:
            first1 = first1 + (m1-1) - n1
        else:
            first1 += m1 - 1
        if last1 + (m1-1) > n1:
            last1 = last1 + (m1-1) - n1
        else:
            last1 += m1 - 1
        stroke1 += str(first1)
    else:
        end1 = True
    if last2 != 1:
        if first2 + (m2-1) > n2:
            first2 = first2 + (m2-1) - n2
        else:
            first2 += m2 - 1
        if last2 + (m2-1) > n2:
            last2 = last2 + (m2-1) - n2
        else:
            last2 += m2 - 1
        stroke2 += str(first2)
    else:
        end2 = True

print(stroke1 + stroke2)
