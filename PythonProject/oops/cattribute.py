class ObjectCounter:
    num_instances = 0
    def __init__(self):
        ObjectCounter.num_instances += 1


if __name__=="__main__":
    ObjectCounter()

    ObjectCounter()

    ObjectCounter()

    ObjectCounter()

    print(ObjectCounter.num_instances)

    counter = ObjectCounter()
    print(counter.num_instances)



