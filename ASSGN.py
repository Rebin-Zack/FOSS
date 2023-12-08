#max area function receives height list as the parameter
# To traverse the list we use two pointers, right and left
#our major aim is to find the max area, is initially zero

def max_area(height):
    max_water = 0
    left_pointer, right_pointer = 0, len(height) - 1

    while left_pointer < right_pointer:
        height_left, height_right = height[left_pointer], height[right_pointer]
        width = right_pointer - left_pointer
        current_water = min(height_left, height_right) * width
        max_water = max(max_water, current_water)

        if height_left < height_right:
            left_pointer += 1
        else:
            right_pointer -= 1

    return f"Input: height = {height}\nOutput: {max_water}"

#main code
#we define the heights as a list
#max_area function is used, which returns the maximum area
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
result = max_area(height)
print(result)
