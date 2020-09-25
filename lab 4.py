#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Calculating Inital and final momentums of slowest

vi_1=0.23 #initial velocity for slowest
vi_1_uncertainty=0.01 #uncertainty of the initial velocity for slowest

vf_1=-0.16 #final velocity for slowest
vf_1_uncertainty=0.03 #uncertainty of the final velocity for slowest

m_cart=0.4966 #mass of the cart
m_cart_uncertainty=0.0001 #uncertainty of the mass of the cart

Pi=vi_1*m_cart #calculating the initial momentum for the slowest trail
Pi_uncertainty= Pi*((vi_1_uncertainty/vi_1)+(m_cart_uncertainty/m_cart)) #calculating the uncertainty of initial momentum for the slowest trial

Pf=vf_1*m_cart #calculating the final momentum for the slowest trail
Pf_uncertainty= Pf*((vf_1_uncertainty/vf_1)+(m_cart_uncertainty/m_cart)) #calculating the uncertainty of final momentum for the slowest trial

print("Results of Slowest Trial") #Differentiate the 3 trials

#Make sure the initial momentum and its error show up in the outputs with the proper units
print ("Pi = ", Pi, "(kg*m)/s")
print ("Pi Uncertainty = ", Pi_uncertainty, "(kg*m)/s")

#Make sure the final momentum and its error show up in the outputs with the proper units
print ("Pf = ", Pf, "(kg*m)/s")
print ("Pf Uncertainty = ", Pf_uncertainty, "(kg*m)/s")


# In[ ]: