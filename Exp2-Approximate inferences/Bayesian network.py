from pgmpy.models import BayesianNetwork 

from pgmpy.factors.discrete import TabularCPD 

from pgmpy.inference import VariableElimination 

import networkx as nx 

import matplotlib.pyplot as plt 

model = BayesianNetwork([('Guest', 'Host'), ('Price', 'Host')]) 

cpd_guest = TabularCPD('Guest', 3, [[0.33], [0.33], [0.33]]) 

cpd_price = TabularCPD('Price', 3, [[0.33], [0.33], [0.33]]) 

cpd_host = TabularCPD('Host', 3, [[0, 0, 0, 0, 0.5, 1, 0, 1, 0.5], 
                                    [0.5, 0, 1, 0, 0, 0, 1, 0, 0.5], 
                                    [0.5, 1, 0, 1, 0.5, 0, 0, 0, 0]], 
evidence=['Guest', 'Price'], evidence_card=[3, 3]) 

model.add_cpds(cpd_guest, cpd_price, cpd_host) 

model.check_model() 

infer = VariableElimination(model) 

posterior_p = infer.query(['Host'], evidence={'Guest': 2, 'Price': 2}) 

print(posterior_p) 

plt.rcParams["patch.force_edgecolor"] = True 

nx.draw_networkx(model, with_labels=True) 

plt.savefig('model.png') 

plt.close() 