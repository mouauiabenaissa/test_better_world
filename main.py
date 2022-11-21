# ***************************************************** TEST BETTER WOLRD ***************************************************
# The following function checks if a string is a regular chain
# Time complexity: O(n)
# Memory complexity: O(1)
def test_chain(chain):
    flag = True
    cnt = 0
    for i in range(len(chain)):
        if chain[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            flag = False
    return flag


print(test_chain("(())()"))

# The following function finds the longest regular subchain
# Time complexity: O(n)
# Memory complexity: O(n)


def find_wellformed_subchain(chain):
    a = 0
    s = [-1]
    for i, c in enumerate(chain):
        if c == '(':
            s.append(i)
        elif len(s) > 1:
            s.pop()
            n = i - s[-1]
            if a < n:
                a = n
        else:
            s[0] = i
    return a


print(find_wellformed_subchain("(()))(()())"))

''' 

QUESTION 3 :
We can write the function test_chain() as a parallel algorithm
We will divide the string into multiple substrings and solve it independently for each substring
Then we will combine the results to find the final answer.
We should save two values for each substring after of the processing:
1- The minimum nesting depth achieved relative to the start of the string.
2- The total gain or loss in nesting depth across the whole string.

We will compute the answer after concatenation of the substrings using the following pseudo-code:

minNest = 0
totGain = 0
for p in chunkResults
  minNest = min(minNest, totGain + p.minNest)
  totGain += p.totGain
return new ChunkResult(minNest, totGain)

'''
