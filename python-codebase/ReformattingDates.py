def reformatDate(dates):
    dict_months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                   'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    res = []
    for date in dates:
        parts = date.split()
        if len(parts[0]) == 3:
            parts[0] = parts[0][:1]
        else:
            parts[0] = parts[0][:2]
        new_date = '{0:04d}-{1:02d}-{2:02d}'.format(int(parts[2]), int(dict_months[parts[1]]), int(parts[0]))
        print new_date


dates_list = ['20th Oct 2052', '6th Jun 1933', '26th May 1960', '20th Sep 1958', '16th Mar 2068',
              '25th May 1912', '16th Dec 2018', '26th Dec 2061', '4th Nov 2030', '28th Jul 1963']
reformatDate(dates_list)
