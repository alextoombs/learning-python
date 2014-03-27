def fizz_buzz(max_val=100):
    '''fizz_buzz is an implementation of a popular programming question.

       It is an illustration in the futility of a language without switch/case
       statements.

       Arguments:
       -- max_val: fizz_buzz runs from [0,max_val] (default: 100)
    '''
    for num in range(0, max_val):
        if num%5 == 0:
            if num%3 == 0:
                # In this case, num is evenly divisible by both 5 and 3.
                print('fizzbuzz!')
            else:
                print('fizz')
        elif num%3 == 0:
            print('buzz')
        else:
     	   print("num: {}".format(num))

if __name__ == '__main__':
    fizz_buzz()
