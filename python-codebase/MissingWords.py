def missingWords(s, t):
    latest, s_words, t_words = -1, s.split(), t.split()
    length = len(s_words)
    for x in t_words:
        flag, i = 0, latest + 1
        '''
        while loop runs from the latest value stored till the end
        this avoids checking of substrings till the latest index already handled like in case of:
            s: some random string string string some
            t: some string random string
        used while loop as using a for loop with the range function times out
        '''
        while i < length:
            if x == s_words[i]:
                s_words[i] = ''
                flag = 1
                latest = i
                break
            i += 1
        # if flag is ever 0, it means that there is an order mismatch. No further processing needs to be done
        if flag == 0:
            break
    # removing all the empty strings and return the list
    return filter(None, s_words)


s_t_list = [('I am using HackerRank to improve programming', 'am HackerRank to improve'),
            ('I love programming', 'programming'),
            ('I like cheese', 'like'),
            ('some random string string string some', 'some string random string')]

for s_part, t_part in s_t_list:
    missing = missingWords(s_part, t_part)
    print missing
