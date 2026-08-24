monkey_submissions = [5, 3, 5, 2, 8, 3, 10, 2, 8, 12]
monkey_submissions.sort()
monkey_submissions=set(monkey_submissions)
print(monkey_submissions)
monkey_submissions=list(monkey_submissions)
print(monkey_submissions[0])
print(monkey_submissions[-1])
print('Most suspicious monkey ate:',monkey_submissions[-1],' bananas')
if monkey_submissions[-1]>10:
    print('🚨 Cheating detected')
print('Professor Banana is watching!')