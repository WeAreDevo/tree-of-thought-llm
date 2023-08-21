# 5-shot
standard_prompt = '''Perform the decomposition of a complex policy to answer a question. Here are a few examples of policies and their decompositions with respect to input questions
Policy: “The following benefits can be reduced or stopped if you commit benefit fraud:
* Carer’s Allowance
* Employment and Support Allowance
* Housing Benefit
* Incapacity Benefit”
Input question: Can my benefit be reduced or stopped?
Decomposition: Based on the policy, I first need to answer to the following basic questions:
Q0: Have you committed benefit fraud?
Q1: Is it Carer’s Allowance?
Q2: Is it Employment and Support Allowance?
Q3: Is it Housing Benefit?
Q4: Is it Incapacity Benefit?
The answers to those questions should be logically combined as follows: Q0 AND (Q1 OR Q2 OR Q3 OR Q4)
[STOP]


Policy: "Indiana Head Start
Children in foster care, homeless children, and children from families receiving public assistance (Temporary Assistance for Needy Families or Supplemental Security Income) are also eligible for Head Start and Early Head Start services regardless of income."
Input question: Am I eligible for Head Start and Early Head Start?
Decomposition: Based on the policy, I first need to answer to the following basic questions:
Q0:  Are you a child in foster care?
Q1:  Are you a homeless child?
Q2:  Are you a child from a family receiving public assistance?
Q3:  Are you living in Indiana?
The answers to those questions should be logically combined as follows: Q3 AND (Q0 OR Q1 OR Q2)
[STOP]

Policy:  “General Program Requirements:
In order to qualify for this benefit program, you must be a resident of Indiana, responsible for a child under 18 years of age, a U.S. citizen or qualified alien and have very low income."
Input question:  Do I qualify for this benefit program?
Decomposition: Based on the policy, I first need to answer to the following basic questions: 
Q0: Do you have very low income?
Q1: Are you a resident of Indiana?
Q2: Are you responsible for a child under 18 years of age?
Q3: Are you a U.S. citizen or qualified alien?
The answers to those questions should be logically combined as follows: Q0 AND Q1 AND Q2 AND Q3
[STOP]

Policy: "2. Authorization
You must be authorized to talk to the Tax Credit Office about someone else’s tax credits. If you’re not, every time you call that person must first confirm their identity and say they’re happy for you to act for them."
Input question:  Can I talk to the Tax Credit Office about someone else’s tax credits?
Decomposition: Based on the policy,  I first need to answer to the following basic questions: 
Q0:  Are you authorized?
Q1:  Can that person first confirm their identity and say they’re happy for you to act for them every time you call?
The answers to those questions should be logically combined as follows: Q0 OR Q1
[STOP]

Policy: "Who can get Crisis Payment:
If you get Family Tax Benefit or Child Care Benefit, you must also get another income support payment to be eligible for a crisis payment."
Input question: Can I get Crisis Payment?
Decomposition: Based on the policy,  I first need to answer to the following basic questions: 
Q0: Do you get another income support payment?
Q1: Do you get Family Tax Benefit?
Q2: Do you get Child Care Benefit?
The answers to those questions should be logically combined as follows: (Q1 or Q2) and Q0
[STOP]

Policy: “In order to qualify for this benefit program, homeowners and renters must have sustained physical damage
and be located in a disaster declared county”
Input question: Do I qualify for this benefit program?
Decomposition: Based on the policy,  I first need to answer to the following basic questions: 
Q0: Are you located in a disaster declared county?
Q1: Do you have sustained physical damage?
Q2: Are you a homeowner?
Q3: Are you a renter?
The answers to those questions should be logically combined as follows: Q0 AND Q1 AND (Q2 OR Q3)
[STOP]

Policy: "To be covered by NY PFL, employees must meet the following criteria:
* Have a NY tax jurisdiction code (work in New York)
* Be a regular or supplemental employee
* Take leave that qualifies for NY PFL (i.e., care of a seriously ill, covered family member, bonding with a new child, or military exigency -- as described below)
* Employees with a regular schedule of 20 or more hours per week are eligible after 26 weeks of employment
* Employees with a regular schedule of less than 20 hours per week are eligible after 175 days worked"
Input question: Do I qualify for this benefit program?
Decomposition: Based on the policy, I first need to answer the following basic questions:
Q0: Do you have a NY tax jurisdiction code (work in New York)?
Q1: Are you a regular or supplemental employee?
Q2: Are you taking leave that qualifies for NY PFL (i.e., care of a seriously ill, covered family member, bonding with a new child, or military exigency)?
Q3: Do you have a regular schedule of 20 or more hours per week?
Q4: Do you have a regular schedule of less than 20 hours per week?
Q5: Have vou been employed for 26 weeks?
Q6: Have you worked for 175 days?
The answers to those questions should be logically combined as follows: (QO AND Q1 AND Q2 AND Q3 AND Q5) OR (Q0 AND Q1 AND Q2 AND Q4 AND Q6)
[STOP]

{input}
'''

# 5-shot
cot_prompt = '''Perform the decomposition of a complex policy to answer a question. Here are a few examples of policies and their decompositions with respect to input questions
Input: 4 4 6 8
Steps:
4 + 8 = 12 (left: 4 6 12)
6 - 4 = 2 (left: 2 12)
2 * 12 = 24 (left: 24)
Answer: (6 - 4) * (4 + 8) = 24
Input: 2 9 10 12
Steps:
12 * 2 = 24 (left: 9 10 24)
10 - 9 = 1 (left: 1 24)
24 * 1 = 24 (left: 24)
Answer: (12 * 2) * (10 - 9) = 24
Input: 4 9 10 13
Steps:
13 - 10 = 3 (left: 3 4 9)
9 - 3 = 6 (left: 4 6)
4 * 6 = 24 (left: 24)
Answer: 4 * (9 - (13 - 10)) = 24
Input: 1 4 8 8
Steps:
8 / 4 = 2 (left: 1 2 8)
1 + 2 = 3 (left: 3 8)
3 * 8 = 24 (left: 24)
Answer: (1 + 8 / 4) * 8 = 24
Input: 5 5 5 9
Steps:
5 + 5 = 10 (left: 5 9 10)
10 + 5 = 15 (left: 9 15)
15 + 9 = 24 (left: 24)
Answer: ((5 + 5) + 5) + 9 = 24
Input: {input}
'''

# 1-shot
propose_prompt = '''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {input}
Possible next steps:
'''

value_prompt = '''Evaluate if given numbers can reach 24 (sure/likely/impossible)
10 14
10 + 14 = 24
sure
11 12
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
11 / 12 = 0.91
impossible
4 4 10
4 + 4 + 10 = 8 + 10 = 18
4 * 10 - 4 = 40 - 4 = 36
(10 - 4) * 4 = 6 * 4 = 24
sure
4 9 11
9 + 11 + 4 = 20 + 4 = 24
sure
5 7 8
5 + 7 + 8 = 12 + 8 = 20
(8 - 5) * 7 = 3 * 7 = 21
I cannot obtain 24 now, but numbers are within a reasonable range
likely
5 6 6
5 + 6 + 6 = 17
(6 - 5) * 6 = 1 * 6 = 6
I cannot obtain 24 now, but numbers are within a reasonable range
likely
10 10 11
10 + 10 + 11 = 31
(11 - 10) * 10 = 10
10 10 10 are all too big
impossible
1 3 3
1 * 3 * 3 = 9
(1 + 3) * 3 = 12
1 3 3 are all too small
impossible
{input}
'''

value_last_step_prompt = '''Use numbers and basic arithmetic operations (+ - * /) to obtain 24. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 24.
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) = 24
Judge: 
sure
Input: 2 9 10 12
Answer: 2 * 12 * (10 - 9) = 24
Judge: 
sure
Input: 4 9 10 13
Answer: (13 - 9) * (10 - 4) = 24
Judge: 
sure
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25
Judge: 
impossible
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24
Judge: 
impossible
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24
Judge: 
impossible
Input: {input}
Answer: {answer}
Judge:'''