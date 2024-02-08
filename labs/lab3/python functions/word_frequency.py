def word_frequency(input_string):
    words = input_string.split()
    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1
    return frequency_dict

input_string = input("Enter a string: ")
result = word_frequency(input_string)
print("Word frequencies:", result)