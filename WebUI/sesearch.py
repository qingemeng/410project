# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 14:26:09 2018

@author: acer
"""


        
def se_search(query_string):
    query_string1="start a web server"
    query_string2="read data into dataframe"
    query_string3="plot time series"
    
    query_result1={
            0:{
                    'content':'result for query start a web server',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            1:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            2:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },        
            3:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            4:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            5:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            6:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            7:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            8:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            9:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    }
                                                 
            }
            
    query_result2={
            0:{
                    'content':'result for read data into dataframe',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            1:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            2:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },        
            3:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            4:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            5:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            6:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            7:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            8:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            9:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    }
                                                 
            }
            
    query_result3={
            0:{
                    'content':'result for plot time series',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            1:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            2:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },        
            3:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            4:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            5:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            6:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            7:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            8:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    },
            9:{
                    'content':'another solution is to use a proxy for the d_file .',
                    'score':0.23250860159443879,
                    'url':'https://stackoverflow.com/a/11521614'                
                    }
                                                 
            }
    if query_string==query_string1:
        return query_result1;
    if query_string==query_string2:
        return query_result2;
    if query_string==query_string3:
        return query_string3;
    return {}
        