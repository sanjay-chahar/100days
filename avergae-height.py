## Average Height

# Instructions

#You are going to write a program that calculates the average student height from a List of heights.

#e.g. `student_heights = [180, 124, 165, 173, 189, 169, 146]`

#The average height can be calculated by adding all the heights together and dividing by the total number of heights.

#e.g.

#180 + 124 + 165 + 173 + 189 + 169 + 146 = **1146**

#There are a total of **7** heights in `student_heights`

#1146 ÷ 7 = **163.71428571428572**

#Average height rounded to the nearest whole number = **164**

#Important** You should not use the `sum()` or `len()` functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input 156 178 165 187


#In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
#example input 180 124 165 173 189 169 146

# Example Output 163.17


#e.g. When you hit **run**, this is what should happen:
loop_counter = 0
total_height = 0
heights = input("Please enter height = " ).split()
print(heights)
for height in heights:
    counter = 1
    theight = int(height)
    #print(height)
    #print(type(height))
    total_height += theight
    loop_counter += counter
    #print(loop_counter)
    #print(total_height)
    avergae_height = round(total_height / loop_counter ,2)
print(f"Total height is {total_height}")
print(f"average total height is {avergae_height}")


