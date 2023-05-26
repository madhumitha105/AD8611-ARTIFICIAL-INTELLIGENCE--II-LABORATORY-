from pgmpy.models import BayesianNetwork 

from pgmpy.inference import VariableElimination 

from pgmpy.factors.discrete import TabularCPD 

alarm_model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'),('Alarm', 'JohnCalls'),('Alarm', 'MaryCalls')]) 

cpd_burglary = TabularCPD(variable='Burglary', variable_card=2,values=[[.999], [0.001]]) 

cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2,values=[[0.998], [0.002]]) 

cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,values=[[0.999, 0.71, 0.06, 0.05],[0.001, 0.29, 0.94, 0.95]],evidence=['Burglary', 'Earthquake'],evidence_card=[2, 2]) 

cpd_johncalls = TabularCPD(variable='JohnCalls', variable_card=2,values=[[0.95, 0.1], [0.05, 0.9]],evidence=['Alarm'], evidence_card=[2]) 

cpd_marycalls = TabularCPD(variable='MaryCalls', variable_card=2,values=[[0.1, 0.7], [0.9, 0.3]],evidence=['Alarm'], evidence_card=[2]) 

alarm_model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls) 

print(alarm_model.check_model()) 

print(alarm_model.nodes()) 

print(alarm_model.edges()) 

print(alarm_model.local_independencies('Burglary'))