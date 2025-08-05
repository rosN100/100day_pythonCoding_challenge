# function with output
# def my_function():
#     result = 4*3
#     return result
# answer = my_function()
# print(answer)
# f_name = input("enter your first name\n")
# l_name = input("enter your last name\n")
# def format_name(f_name,l_name):
#     # f_name[0].upper()
#     # l_name[0].upper()
#     start =f_name.title()
#     end = l_name.title()
#     return start + " " + end
# full_name = format_name(f_name,l_name)
# print(full_name)

# def text(text):
#     return text+text
# def text_format(text):
#     return text.title()
# output = text_format(text("hello"))
# print(output)


def format_name(f_name,l_name):
    if f_name =="" and l_name =="":
        return "You did not provide valid input!"
    start =f_name.title()
    end = l_name.title()
    return start + " " + end
full_name = format_name(input("enter your first name\n"),input("enter your last name\n"))
print(f"full name is : {full_name}")
