wrong_address = [
    '555 Fulton St, Unit 520, San Francisco, California',
    '555 Fulton St, Unit 510, San Francisco, California',
    '555 Culton St, Unit 510, Winters, California']

ans =  '555 Culton St, Unit 510, San Francisco'.split(', ')
print(ans)

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

for address in wrong_address:
    address = address.split(', ')
    print(address)
    compare_score = 0
    for index, value in enumerate(ans):
        if value == address[index]:
            compare_score +=1
    print(compare_score)

    
