import logging
logging.basicConfig(filename= "String_task.log", level= logging.INFO, format= '%(asctime)s %(levelname)s %(name)s %(message)s')

class string_task:

    def reverse_str(self, input):
        """This function tries to reverse the input string"""
        try:
            return input[-1::-1]

        except Exception as e:
            logging.info(e)
            print(e)

    def vowel_filter_str(self,input):
        try:
            i =0
            c = 0
            fstr = " "
            l1 = []
            l = list(input)
            while i < len(input) - c:
                if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u' or l[i] == 'A' or l[
                    i] == 'E' or l[i] == 'I' or l[i] == 'O' or l[i] == 'U':
                    l1.append(l[i])
                    l.pop(i)
                    i = i - 1
                    c = c + 1
                i = i + 1

            # print("The list without vowels is", l)
            # print("The list with vowels is", l1)

            for j in range(len(l)):
                fstr = fstr + l[j]

            print("The string without vowels is :")
            print()
            return (fstr)

        except Exception as e:
            logging.info(e)
            print(e)

    def lenth_str(self,input):
        try:
            i, c = 0, 0
            #print("Please input the string for which you want to check its length")
            #s = input()
            l = list(input)
            while l != []:
                l.pop(i)
                c = c + 1
            i = i + 1

            print("The length of this string is", c)

        except Exception as e:
            logging.info(e)
            print(e)


str_input = string_task()
#print(str_input.reverse_str("This is a test"))
#print(str_input.vowel_filter_str("This is a test input to filter the vowels from the given string input"))
str_input.lenth_str("This is a test input to check the lenth of string input")