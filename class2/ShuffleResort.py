import random

students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace']

# 功能1：随机抽取一名幸运学生
lucky_student = random.choice(students)
print(f"幸运学生: {lucky_student}")

# 功能2：随机打乱学生名单顺序
random.shuffle(students)
print("随机排序后的名单:")
for student in students:
    print(student)