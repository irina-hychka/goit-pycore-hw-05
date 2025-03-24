def caching_fibonacci():
    """
    A function that calculates Fibonacci numbers using cash.

    Returns:
        function: A function that calculates Fibonacci numbers.
    """
    # Create an empty dictionary to store computed Fibonacci numbers
    cache = {}

    def fibonacci(n):
        """
        Calcaulates Fibonacci numbers recursively and stores previously
        computed values in a dictionary (cache) to optimize performance.
        
        Params:
            n (int): must be a positive integer.

        Returns:
            int: The Fibonacci number.

        Raises:
            ValueError: If n is not an integer.
        """
        # Ensure n is an integer
        if not isinstance(n, int):
            raise ValueError("The number must be an integer!")

        # Check if zero or less: no calculations needed
        if n <= 0:
            return 0
        
        # Check if equals to one: no calculations needed
        if n == 1:
            return 1
        
        # Check if the result is already cached
        if n in cache:
            return cache[n]
        
        # Calculate and store in cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n] 

    return fibonacci


# Usage:
if __name__ == "__main__":
    fib = caching_fibonacci()

    # Expected Output: 55
    print(fib(10))
    # Expected Output: 610
    print(fib(15))