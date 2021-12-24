from gurobipy import *
import math
'''
for case in range(10):
    print('case '+str(case))
    m = read('AES_Model3_Simplified_5r_collide3_case{}.lp'.format(case))
    m.setParam( 'OutputFlag', 1 )
    #m.Params.timeLimit = 1800.0
    #m.Params.BestObjStop = 12.5
    m.optimize()
    
    #m.write("AES_Model3_simplified\AES_Model3_Simplified_3r_collide3_case4.sol")


'''


for case in range(0,10):
    print('case '+str(case))
    m=read('3r\lp\AES_3r_collide3_case{}.lp'.format(case))
    m.setParam( 'OutputFlag', 0 )
    m.setParam( 'PoolSearchMode',  2 )
    m.setParam( 'PoolSolutions', 700)


    m.optimize()

    counter = m.getAttr( 'SolCount' ) 
    print( "{} solutions...".format( counter ) )

    obj_list=[]
    gv=m.getVars()
    names=m.getAttr('VarName',gv)
    for i in range(counter):
        m.setParam('SolutionNumber',i)
        obj_list.append(round(m.PoolObjVal))
        '''
        xn=m.getAttr('Xn',gv)
        lines=["{} {}".format(v1,round(v2)) for v1,v2 in zip(names,xn)]
        with open('3r\sol\AES_3r_collide3_case{}_{}.sol'.format(case,i), 'w') as f:
            f.write('# objective value = {}\n'.format(m.PoolObjVal))
            f.write("\n".join(lines))
        '''   

    obj_set=set(obj_list)
    obj_sorted_list=list(obj_set)
    obj_sorted_list.sort()
    if len(obj_sorted_list)==0:
        continue
    res=[]
    for i in range(len(obj_sorted_list)):
            print(str(obj_sorted_list[i])+"  "+ str(obj_list.count(obj_sorted_list[i])))
            res.append([obj_sorted_list[i],obj_list.count(obj_sorted_list[i])])

    prob=0
    
    prob=prob + 2**((-8)*res[0][0]) * res[0][1]

    print('Prob =  2 ^ '+ str(math.log(prob,2)))



