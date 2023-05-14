from bisection import bisection
from broken_lines import broken_lines
from fibonacci import fibonacci
from golden_section import golden_section
from tangent import tangent
from newton import newton
from init import func

print("------Результат метода деления отрезка пополам------")
print(bisection(), func(bisection()))
print("------Результат метода золотого сечения------")
print(golden_section(), func(golden_section()))
print("------Результат метода Фиббоначи------")
print(fibonacci(), func(fibonacci()))
print("------Результат метода ломаных------")
print(broken_lines(), func(broken_lines()))
print("------Результат метода касательных------")
print(tangent(), func(tangent()))
print("------Результат метода Ньютона------")
print(newton(), func(newton()))
