class Solution(object):
    def fizzBuzz(self, n):
        i=1
        answer=[]
        while i <= n:
            answer.append(i)
            i += 1
        for i in range(n):
            if answer[i]%3==0 and answer[i]%5==0 :
                answer[i]="FizzBuzz"
            elif answer[i]%3==0 :
                answer[i]="Fizz"
            elif answer[i]%5==0 :
                answer[i]="Buzz"
            else:
                answer[i]=str(i+1)
        return answer