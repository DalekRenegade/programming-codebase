def computeParameterValue(sources):
    source_count = len(sources)
    param_count = len(sources[0])
    param_order, param_dict = [], {}
    for source in sources:
        for parameter in source.split():
            param_val = parameter.split(':')
            param, val = param_val[0].strip(), param_val[1].strip()
            if param not in param_dict:
                param_order.append(param)
            param_dict[param] = val
    return [param_dict[p] for p in param_order]


source_list1 = ['P1:x P2:y P5:z', 'P1:b P5:a P3:w']
source_list2 = ['P1:a P3:b P5:x', 'P1:b P2:q P5:x']
print computeParameterValue(source_list1)
print computeParameterValue(source_list2)
