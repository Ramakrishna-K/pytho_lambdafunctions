# ✨ 1. Lambda Functions (Anonymous Functions)

# A lambda function is a small anonymous function defined using the lambda keyword. It's used for short, simple operations.

# traditional function

# def square(x):
#     return x*x

# # Lambda function

# square_lambda = lambda x:x*x
# print(square_lambda(5))

# # More uses:
# add = lambda a, b: a + b
# print(add(3, 4))  # Output: 7

# # With map() or filter()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, nums))
# print(squared)  # Output: [1, 4, 9, 16]


# # 🔁 2. Recursive Functions
# # A recursive function is a function that calls itself. Commonly used in problems like factorial, Fibonacci, etc.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))  # Output: 120


# # 🔁 3. Nested Functions
# # You can define one function inside another function. Inner functions can only be used inside the outer function.

# def outer():
#     def inner():
#         print("Inside inner function")
#     print("Inside outer function")
#     inner()

# outer()

# # 🧠 4. Higher-Order Functions
# # A higher-order function is a function that:

# # takes another function as an argument

# # OR returns a function
# # 📌 Example 1: Taking a Function as an Argument
# def apply_function(f, x):
#     return f(x)

# def square(n):
#     return n * n

# print(apply_function(square, 6))  # Output: 36

# 📌 Example 2: Returning a Function
def outer_function():
    def inner_function():
        return "Hello from inner function!"
    return inner_function

greet = outer_function()
print(greet())  # Output: Hello from inner function!



