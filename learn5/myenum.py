from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 
'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

# value属性则是自动赋给成员的int常量，默认从1开始计数。
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


from enum import unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


# 既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量
for name, member in Weekday.__members__.items():
	print(name, '=>',member)