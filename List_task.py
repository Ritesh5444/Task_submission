import logging
logging.basicConfig(filename= "List_task.log", level = logging.INFO, format= '%(asctime)s %(levelname)s %(name)s %(message)s')

class list1:

    def extract_list(self, input):
        """This functions extracts the list values from an input"""
        logging.info("We are in extract list block")
        try:
            for i in input:
                if type(i) == list:
                    for j in i:
                        print(j)
        except Exception as e:
            logging.exception(e)
            print(e)
            print("Please give valid input")

    def extract_ineuron(self,input):
        """This function tries to extract ineuron word from the input"""
        try:
            for i in input:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if j == 'ineuron':
                            print(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if k == 'ineuron':
                            print(k)
                        if v == 'ineuron':
                            print(v)
        except Exception as e:
            logging.exception(e)
            print(e)
            print("No ineuron found in the given block")

    def flat_list(self,input):
        """Try to unwrap all the collection inside collection and create a flat list"""
        logging.info("we are creating a flat list from given input")
        try:
            l1 = []
            for i in input:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        l1.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        print(v)
                        l1.append(k)
                        l1.append(v)
            return(l1)

        except Exception as e:
            logging.info(e)
            print(e)

    def append_list(self,input,a):
        """This is a custom function created to append values to a list"""
        try:
            jlist = ['None']
            for i in range(1):
                jlist[i] = a
            print("The appended list is")
            return input + jlist

        except Exception as e:
            logging.info(e)
            print(e)

    def extend_list(self, input,a):
        """This is a custom function to extend values to a list"""
        try:
            # jlist = ['None']
            if type(a) == list:
                #print("The appended list is"" " "List checking")
                return input + a
            if type(a) == tuple:
                len1 = len(a)
                x = ['None']
                x = x * len1
                for i in range(len1):
                    x[i] = a[i]
                #print("The appended list is"" " "Tuple checking")
                return input + x
            if type(a) == set:
                s1 = list(a)
                #print("The appended list is"" " "Set checking")
                return input + s1
            if type(a) == dict:
                b = list(a.keys())
                # print(b)
                #print("The appended list is"" " "dictionary checking")
                return input + b
            if type(a) != list or type(a) != tuple or type(a) != set or type(a) != dict:
                print("Enter valid input")

        except Exception as e:
            logging.info(e)
            print(e)

    def pop_list(self, input, index):
        try:
            a = len(input)
            l1 = ['None']
            l1 = l1 * (a - 1)
            b = 0
            for i in range(a):
                if i == index:
                    b = 1
                if i != index:
                    l1[i - b] = input[i]
            print("The result after doing pop up is")
            return l1

        except Exception as e:
            logging.info(e)
            print(e)

l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7), {'K1' : 'sudh', 'k2':'ineuron', 'k3': 'kumar', 3:6, 7:8},['ineuron', 'data science']]
list_input = list1()
#list_input.extract_list(l)
#list_input.extract_ineuron(l)
#print(list_input.flat_list(l))

#print(list_input.append_list(l,45))
#print(list_input.extend_list(l, ['apple']))
print(list_input.pop_list(l,3))