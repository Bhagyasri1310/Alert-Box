import pyautogui
num = int(input("Enter a number to divide 123 "))
if num == 0:
    pyautogui.alert("Alert!!! Division with zero is not possible")
else:
    print(f'The value is {123/num}')