#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 13:08:02 2022

@author: MariaLoizou
"""

#Formula 
"""Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
def find_payment(loan, r, m):
    a = (1+r)**m
    b = loan * r * a 
    c = a-1 
    fixedPayment = b/c
    return fixedPayment
   
   
#print(find_payment(300000, 0.05/12, 360))

# abstract class 

"""Abstract class for building different kinds of mortgages
Assumes: loan and ann_rate are floats (rate is ann_rate/12), 
months an int. Creates a new mortgage of size loan, duration months, and
annual rate ann_rate"""
class Mortgage(object):

    def __init__(self, loan, ann_rate, months): 
        self.loan = loan 
        self.monthly_rate = ann_rate/12
        self.months = months 
        self.fixedPayment = find_payment(loan,self.monthly_rate, months)
        self.paid = [0.0]
        self.outstanding = [loan]
        self.legend = None
  
    """Make a payment. The payment is added to the self.paid list and also 
    updates the sel.outstanding list by calculating the loan readunction and 
    subtracting it from the outstanding value""" 
    def make_payment(self): 
        self.paid.append(self.fixedPayment)
        loan_reduction = self.fixedPayment - (self.outstanding[-1]*self.monthly_rate)
        self.outstanding.append(self.outstanding[-1]- loan_reduction)
        
    """Calcluates the total amount paid. Raises exception if the values in the list 
    are not numerical"""
    def get_total_paid(self):
      
        try:
            total_paid = sum(self.paid)
            return total_paid
        except TypeError:
            print('Sequence contains non-numeric value')
    
    """Prints a description of the mortgage type """
    def __str__(self):
        return self.legend
    
"""Class for building a fixed mortgage. Takes as arguments the loan, ann_rate
and months. It is a subclass of Mortgage"""   
class Fixed(Mortgage):
    
    """Constructor to create an object of the class"""
    def __init__(self, loan, ann_rate, months):
        Mortgage.__init__(self, loan, ann_rate, months)
        self.legend = "Fixed, " + str(round((ann_rate * 100),1)) + "%"
 
"""Class for building a fixed mortgage with points. Takes as arguments the loan, ann_rate
and months and points"""  
class Fixed_with_pts(Mortgage):
    def __init__(self, loan, ann_rate, months, pts):
        
        Mortgage.__init__(self, loan, ann_rate, months)
        self.pts = pts
        self.paid = [loan * (pts * 0.01)]
        self.outstanding = [loan - self.paid[0]]
        self.legend = ("Fixed, " + str(round((ann_rate * 100),1)) + "%" + ", " 
                       + str(self.pts)+ " "+ "points")
        
"""Class for building a tworate mortgage. Takes as arguments the loan, 
ann_rate, months, teaser_rate and teaser_months. The make_payment function
changes the rate after the teaser_months have passed"""      
class Two_rate(Mortgage):
    
    def __init__(self, loan, ann_rate, months, teaser_rate, teaser_months):
        Mortgage.__init__(self, loan, ann_rate, months)
        self.monthly_teaser_rate = teaser_rate/12
        self.teaser_months = teaser_months 
        self.next_monthly_rate = self.monthly_rate
        self.monthly_rate = self.monthly_teaser_rate
        self.fixedPayment = find_payment(self.outstanding[-1],self.monthly_rate, self.months)
        self.legend = (str(round((teaser_rate *100),1)) + "%" + " for" + " " 
                       + str(teaser_months) + " months,then" 
                       + " " + str(round((ann_rate *100),1))+ "%")
                         
    def make_payment(self):
        if len(self.paid) == self.teaser_months + 1:
            self.monthly_rate = self.next_monthly_rate
            self.fixedPayment = find_payment(self.outstanding[-1],self.monthly_rate, self.months-self.teaser_months)
       
        self.paid.append(self.fixedPayment)
        loan_reduction = self.fixedPayment - (self.outstanding[-1] * self.monthly_rate)
        self.outstanding.append(self.outstanding[-1]- loan_reduction)
       
        
# Comparison code for three mortgage types
def compare_mortgages(amt, years, fixed_rate, pts, pts_rate,
                     var_rate1, var_rate2, var_months):
    tot_months = years*12
    fixed1 = Fixed(amt, fixed_rate, tot_months)
    fixed2 = Fixed_with_pts(amt, pts_rate, tot_months, pts)
    two_rate = Two_rate(amt, var_rate2, tot_months, var_rate1,
                      var_months)
    morts = [fixed1, fixed2, two_rate]
    for m in range(tot_months):
        for mort in morts:
            mort.make_payment()
    for m in morts:
        print(m)
        print(f' Total payments = ${m.get_total_paid():,.0f}')
    

 # Create sample output for validation
compare_mortgages(amt=200000, years=30, fixed_rate=0.07,
                   pts = 3.25, pts_rate=0.05, var_rate1=0.045,
                   var_rate2=0.095, var_months=48)  # Second edition
       
             

        






        
    







