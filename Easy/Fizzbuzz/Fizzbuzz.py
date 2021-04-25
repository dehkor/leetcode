class FizzBuzz:
    def fizzbuzz(num: int):
        if num%3 == 0 and num%5 == 0: return "Fizzbuzz"
        if num%3 != 0 and num%5 != 0: return num
        if num%3 == 0: return "Fizz"
        return "Buzz"
        

    if __name__ == "__main__":
        num = input("Enter number: ")
        for i in range(1,int(num)+1):
            print(fizzbuzz(i))
