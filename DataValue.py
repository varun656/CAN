import can
import pickle
import codecs

data = pickle.load( open("random_data.p","rb"))
#print(data[99])

for i in range(10):
    msg = codecs.encode(data[i],'hex')
    print(msg)

msg = codecs.encode(data[999],'hex')
#print(msg)