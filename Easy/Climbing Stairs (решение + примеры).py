class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        print(f"ways[1] = {ways[1]}")
        print(f"ways[2] = {ways[2]}")

        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]
            print(f"ways[{i}] = ways[{i-1}] + ways[{i-2} = {ways[i-1]} + {ways[i-2]} = {ways[i]}]")

        print(f"Результат для n = {n}: {ways[n]} способов.")
        print("-" * 40)

        return ways[n]

# Вывод в консоль.
solution = Solution()

print("Пример 1: n = 2")
result1 = solution.climbStairs(2)
print(f"Ответ: {result1}\n")

print("Пример 2: n = 3")
result2 = solution.climbStairs(3)
print(f"Ответ: {result2}\n")

print("Пример 3: n = 4")
result3 = solution.climbStairs(4)
print(f"Ответ: {result3}\n")

print("Пример 4: n = 5")
result4 = solution.climbStairs(5)
print(f"Ответ: {result4}\n")
