
############### USE LAMBDA ###########
import os
import sys


def sorting(property, dict_all, nrows, status_key):

    unique_key = list(set(dict_all[property]))

    unique_key = sorted(unique_key, key=str.lower)
    counter = [0] * len(unique_key)
    for j in range(len(unique_key)):
        for i in range(nrows):
            if unique_key[j] == dict_all[property][i] and dict_all[status_key][i] == 'CERTIFIED':
                counter[j] = counter[j] + 1
    c1 = [(x, y) for x, y in zip(unique_key, counter)]
    c2 = sorted(c1, key=lambda x: x[1], reverse=True)
    unique_key, counter = zip(*c2)
    return unique_key, counter


if __name__ == '__main__':

    DIR = os.getcwd()
    if len(sys.argv)>=2:
    
    	print ("input file is", sys.argv[1])
	
    elif len (sys.argv)>=3:

    	print ("SOC (occupation) keyword", sys.argv[2])
    elif len(sys.argv) >=4:
    	print ("WORK_SITE_STATE (work site state) keyword", sys.argv[3])
    elif len(sys.argv)>=5:
    	print ("CERTIFIED certified status ", sys.argv[4])
    else:
    	print (' We are using default key words, ')

    if len(sys.argv) <5:

    	output_stat = dict({'in_key': ['SOC_NAME', 'WORKSITE_STATE'],
                        'out_key': ['TOP_OCCUPATIONS', 'TOP_STATES'],
                        'out_text': ['occupations', 'states']})
    	status_key = 'CASE_STATUS'


    else:
    	#### for year 2014 keys are defined by -----
    	#output_stat['in_key'] = ['LCA_CASE_SOC_NAME', 'LCA_CASE_WORKLOC1_STATE']
    	#status_key = 'STATUS'
    	output_stat = dict({'in_key': [sys.argv[2], sys.argv[3]],\
	'out_key': ['TOP_OCCUPATIONS', 'TOP_STATES'],'out_text': ['occupations', 'states']})
        status_key = sys.argv[4]

    out_keys = ['NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
							     
   
        with open(DIR + '/input/%s' % (sys.argv[1])) as fp:
            for ii, line in enumerate(iter(fp.readline, '')):
                if ii == 0:
                    keys = line.split(';')
                    dict_all = dict.fromkeys(keys)
                    for key in keys:
                        dict_all[key] = []
                else:
                    [dict_all[keys[j]].append(line.split(';')[j].replace('"', '')) for j in range(len(keys))]
        
        
        nrows = len(dict_all[''])
        print ('number of rows', nrows)
        for j in range(2):
            unique_key, counter = sorting(output_stat['in_key'][j], dict_all, nrows, status_key)
            keys_extend = out_keys + [output_stat['out_key'][j]]
            dict_out = dict.fromkeys(keys_extend)
            dict_out[output_stat['out_key'][j]] = unique_key
            dict_out[out_keys[0]] = counter
            sum_all = 0 

	    for x in counter:
	    	sum_all = sum_all+x
	
	    dict_out[out_keys[1]] = [format((counter[x] * 100 / sum_all), '.1f') for x in range(len(unique_key))]

            with open(DIR + '/output/top_10_%s.txt' % (output_stat['out_text'][j]), 'w') as f:
                f.write('%s;%s;%s\n' % (keys_extend[0], keys_extend[1], keys_extend[2]))
                for i in range(10):
                    f.write('%s;%s;%s%%\n' % (dict_out[output_stat['out_key'][j]][i],
                                              dict_out[out_keys[0]][i], dict_out[out_keys[1]][i]))
       
