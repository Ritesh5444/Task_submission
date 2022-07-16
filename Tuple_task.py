import logging
logging.basicConfig(filename= "Tuple_task.log",level= logging.INFO, format= '%(asctime)s %(levelname) %(name) %(message)s')

class tuple_task:

    def extract_tuple(self,input):
        """This function extracts all the tuple entities"""
        try:
            for i in input:
                if type(i) == tuple:
                    for j in i:
                        print(j)
        except Exception as e:
            logging.info(e)
            print(e)

input_tuple = tuple_task()
l= [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), {'K1' : 'sudh', 'k2':'ineuron', 'k3': 'kumar', 3:6, 7:8}, ['ineuron', 'data science']]
input_tuple.extract_tuple(l)