import json
import numpy as np
import math

pointnet_ops = ['RealDiv', 'Slice', 'Sub', 'Sum', 'GatherNd', 'ThreeInterpolate', 'Relu', 'Max', 'Add', 'QueryBallPoint', 'Tile', 'Mul', 'GatherPoint', 'GatherV2', 'Transpose', 'BiasAdd', 'ConcatV2', 'Reciprocal', 'ThreeNN', 'Maximum', 'Cast', 'SquaredDifference', 'RandomUniformInt', 'MaxPool', 'Mean', 'Less', 'FusedBatchNorm', 'MatMul', 'Rsqrt', 'Conv2D', 'other']


def parse_timeline(fn):

    with open(fn) as f:
        data = json.load(f)
        main_pid = None
        pid2name = {}
        op_cat = {}
        for item in data["traceEvents"]:
        # print(item)
            if "ts" not in item:
                # print(item["args"]["name"])
                pid2name[item["pid"]] = item["args"]["name"]
                if "all Compute" in item["args"]["name"]:
                    main_pid = item["pid"]

            else:
                if item["pid"] == main_pid:
                    if item["ph"] == 'X' and item["cat"] == "Op" and "dur" in item:
                        if item["name"] not in op_cat:
                            op_cat[item["name"]] = item["dur"]
                        else:
                            op_cat[item["name"]] += item["dur"]
                            
        return op_cat


def dict2list(ops, ops_name):
    new_ops = {}

    for i in ops:
        if i not in ops_name:
            if "other" in new_ops:
                new_ops["other"] += ops[i]
            else:
                new_ops["other"] = ops[i]

        else:
            new_ops[i] = ops[i]

    ls = [0 for i in range(len(ops_name))]
    for i in range(len(ops_name)):
        if ops_name[i] in new_ops:
            ls[i] = new_ops[ops_name[i]]
        else:
            ls[i] = 0

    return ls


