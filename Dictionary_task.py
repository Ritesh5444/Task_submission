import logging
logging.basicConfig(filename="Tuple_task.log", level=logging.INFO,format='%(asctime)s (levelname)s %(name)s %(message)s')


class dict_task:

    def extract_dict(self, input):
        """This function tries to extract all the dictionary element"""
        try:
            for i in input:
                if type(i) == dict:
                    return (i.items())

        except Exception as e:
            logging.info(e)
            print(e)

    def key_count(self,input):
        try:
            for i in input:
                if type(i) == dict:
                    print("The number of keys in dictionary is")
                    return (len(i.keys()))
                    #print("The number of keys in dictionary is", len(i.keys()))
        except Exception as e:
            logging.info(e)
            print(e)






l= [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), {'K1' : 'sudh', 'k2':'ineuron', 'k3': 'kumar', 3:6, 7:8}, ['ineuron', 'data science']]
input_dict = dict_task()
#print(input_dict.extract_dict(l))
print(input_dict.key_count(l))