# Jumping statements - break     continue

# While printing output, break execution after reaching to 5 value
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)                  # 1  2  3  4  program exited
# print("Program exited!!!!!")


# While printing output, skip some values and continue with the rest of values
for i in range(1,10):
    if i==3 or i==5 or i==7:
        continue
    print(i)                    # 1  2  4  6  8  9  program exited
print("Program exited!!!!!")

