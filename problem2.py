'''
Python code to go through a file. Go to the next line every 5 words. Then put it all in a new file.
Written by Jessica Lam & Kevin Kye for CSE 201 HW4 Problem 2 Due on October 12, 2017
'''

file_str="testFile.txt" #reads this file
#file_str=input("Open what file: ")
input_file=open(file_str,"r")
word_count=line_count=0
str_words=""
output_file=open("outputFile.txt","w")
index_list = 0

for line in input_file: #goes through each line in the file
    #Seperates each word and puts them into a list.
    for word in line.split():
        word_count+=1
        # If the program read through 5 words in the list then...
        if word_count % 5 == 0:
            # From the index to the 5th word, print the words.
            for i in line.split()[index_list:word_count]:
                print(i + ' ' , end='', file = output_file)
            # Now the new index starts from the word count and now the program will continue until it reads 5 word again.
            index_list=word_count
            # New line
            print("\n", end= '' , file=output_file)
    #Need to account for the last line when the program doesn't read up to 5 words, then print the rest onto the last line.
    if word_count % 5 != 0:
        for i in line.split()[index_list:]:
            print(i + ' ', end = '', file = output_file)


input_file.close() #important to always close files
output_file.close()



