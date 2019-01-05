import time

def main(password):
    pwLenth = 1
    hasWordDict = True
    if hasWordDict == True:
        wordDict = getDict()
    # print(wordDict)
    getWord(password, wordDict)


def getDict():
    wordDict = []
    with open('wordDict.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()
    for text in content:
        text = text.split('\n')[0]
        wordDict.append(text)
    return wordDict

def getWord(password, wordDict):
    startTime = time.time()
    guess = False
    while guess == False:
        guessWord = ''
        guessLenth = len(password)
        for i in range(guessLenth):
            guessWord = guessWord + wordDict[i]
        for i in range(guessLenth):
            guessWord = guessWord



                                    guessWord = i1 + i2 + i3 + i4 + i5 + i6 + i7
                                    checkTime = time.time()
                                    countTime = float(checkTime - startTime)
                                    countTimeStr = transfer_time(countTime)
                                    print('Checking the word: {}, time waste: {}'.format(guessWord, countTimeStr), end='\r')
                                    if guessWord == password:
                                        guessWord = i1 + i2 + i3 + i4 + i5 + i6 + i7
                                        checkTime = time.time()
                                        countTime = float(checkTime - startTime)
                                        countTimeStr = transfer_time(countTime)
                                        print('The answer is {}, time waste: {}'.format(guessWord, countTimeStr))
                                        guess = True
                                        return guess


def transfer_time(seconds):
    if seconds > 60:
        caculate_time_m = seconds // 60
        if caculate_time_m > 60:
            caculate_time_h = caculate_time_m // 60
            caculate_time_m = caculate_time_m % 60
            caculate_time_s = seconds % 60
            caculate_time = '{:.0f}h{:.0f}m{:.2f}s'.format(caculate_time_h, caculate_time_m, caculate_time_s)
            return caculate_time
        else:
            caculate_time_s = seconds % 60
            caculate_time = '{:.0f}m{:.1f}s'.format(caculate_time_m, caculate_time_s)
    else:
        caculate_time = '{:.2f}s'.format(seconds)
    return caculate_time


if __name__ == '__main__':
    password = '10000000000000'
    main(password)