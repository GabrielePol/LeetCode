#Problem 1491- Average Salary excluding the minimum and Maximum Salary
"""
You're given an array of unique integers salary where salary[i] is the
salary of the i^th employee.
Return the average salary of employees excluding the minimum and maximum
salary. Answers within 10^-5 of the actual answer will be accepted.
"""
class Solution:
    def average(self, salary: List[int]) -> float:
        maximum_salary=max(salary)
        minimum_salary=min(salary)
        total_salary=0
        counter=0
        for i in range(len(salary)):
            if salary[i]==maximum_salary or salary[i]==minimum_salary:
                pass
            else:
                total_salary+=salary[i]
                counter+=1
        return float(total_salary/counter)
```