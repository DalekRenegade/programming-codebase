def totalRequests(file_name):
    hosts_count = {}
    with open(file_name) as fp:
        for cnt, line in enumerate(fp):
            index = line.index('- -')
            key = line[:index].strip()
            if key not in hosts_count:
                hosts_count[key] = 0
            hosts_count[key] += 1
    with open('records_' + file_name, 'w') as fp:
        for key, value in hosts_count.items():
            fp.write('{0} {1}\n'.format(key, value))


input_file_name = 'supporting_files/host_access_log_00.txt'
totalRequests(input_file_name)
