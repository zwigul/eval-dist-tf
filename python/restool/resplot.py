import numpy as np
import matplotlib.pyplot as plt
import csv
import itertools

MEM_CAP = 33451913216
DISK_BW = 120586240
NET_BW = 5368709120

CDNM_PATH = '/Users/wb/Workspace/tf-exp/inception/resmon/00016/dumbo021-cdnm.csv'
GPU_PATH = '/Users/wb/Workspace/tf-exp/inception/resmon/00016/dumbo021-gpu.csv'

ps_list = ['dumbo010', 'dumbo011', 'dumbo014', 'dumbo017', 'dumbo019']

worker_list = ['dumbo020', 'dumbo021', 'dumbo022', 'dumbo023', 'dumbo024', 'dumbo025', 'dumbo026', 'dumbo027', 'dumbo028', 'dumbo029', 'dumbo030', 'dumbo031', 'dumbo032', 'dumbo033']

def genArr(dictReader, key):
    for row in dictReader:
        yield row[key]

def init(exp_id=None):
    global path_prefix
    global data
    data = {}
    path_prefix = '/Users/wb/Workspace/tf-exp/inception/resmon/' + exp_id + '/'
    plt.figure()
    plt.ylim(ymax=1)

def load(nodes=None):

    if nodes == None:
        node_list = worker_list
    else:
        node_list = nodes.split(",")
    num_nodes = len(node_list)

    for node in node_list:

        cdnm_path = path_prefix + node + '-cdnm.csv'
        with open(cdnm_path) as cdnmfile:
            reader = csv.DictReader(itertools.islice(cdnmfile, 6, None))
            time_cnt = 0
            for row in reader:
                time_cnt += 1
                for key in row:

                    if key not in data:
                        data[key] = []

                    val = float(row[key])
                    if key == 'usr':
                        val /= 100
                    elif key == 'read':
                        val /= DISK_BW
                    elif key == 'writ':
                        val /= DISK_BW
                    elif key == 'recv':
                        val /= NET_BW
                    elif key == 'send':
                        val /= NET_BW
                    elif key == 'used':
                        val /= MEM_CAP
                    
                    if len(data[key]) < time_cnt:
                        data[key].append(val)
                    else:
                        data[key][time_cnt - 1] += val

        if node in ps_list:
            continue
        gpu_path = path_prefix + node + '-gpu.csv'
        with open(gpu_path) as gpufile:
            reader = csv.DictReader(itertools.islice(gpufile, 1, None), fieldnames=['gpu', 'gmem'], skipinitialspace=True)
            fnameIter = itertools.cycle(['gpu1', 'gmem1', 'gpu2', 'gmem2'])
            time_cnt = 0
            for row in reader:
                for value in row.values():
                    key = fnameIter.next()
                    if key not in data:
                        data[key] = []

                    if key == 'gpu1':
                        time_cnt += 1

                    val = float(value.strip("%")) / 100

                    if len(data[key]) < time_cnt:
                        data[key].append(val)
                    else:
                        data[key][time_cnt - 1] += val

    for key in data.keys():
        for i in range(len(data[key])):
            data[key][i] /= num_nodes
    # plt.plot(list(genArr(reader, 'send')))


def plot(fields=None):
    # plt.figure()
    plt.title(path_prefix)
    field_list = fields.split(",")
    for field in field_list:
        plt.plot(data[field], label=field)

def show():
    plt.legend()
    plt.show()

# plt.plot(data['gpu1'][400:600])
# plt.plot(data['gmem1'][400:600])
# plt.plot(data['used'][400:600])
# plt.plot(data['recv'][400:600])
# plt.plot(data['send'][400:600])
# plt.plot(data['usr'][400:600])
# plt.plot(data['gmem1'])
