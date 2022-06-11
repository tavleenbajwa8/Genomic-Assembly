#!/usr/bin/env python
# coding: utf-8

# Create a small synthetic genome (10,000 bases) using a random number generator (for ATGC)
# Use a second random number generator and break down the genome into 5,000 overlapping
# fragments of 100 bases and save each 'read' as a fasta file
# break-down the genome into 5,000 overlapping fragments with a randomly generated fragment size.
# Use these to calculate the N50 value

# In[2]:


# Part-1 Forging a genome of 10,000 bp using random function

import random
import numpy as np
def create_genome(n=10000):
    return ''.join(np.random.choice(list('ACTG'), n))
x = create_genome()
print(x)


# In[3]:


# Part-2 Function which use a second random number generator and break down the genome into 5,000 overlapping fragments of 100 bases and save each 'read' as a fasta file

def get_random_str(main_str, substr_len):
    idx = random.randrange(0, len(main_str) - substr_len + 1)    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
    return (main_str[idx : (idx+substr_len)])

get_random_str(x,100)
overlaps = []
n = 5000
for i in range(n):
    func = get_random_str(x,100)
    overlaps.append(func)
    
print(overlaps)


# In[4]:


# Part-3 Fragments of 100 bases and save each 'read' as a fasta file

all_fragments = overlaps
frag_file = open(r'Fragmented_DNA_100bp.fasta', 'w+')
data = '\n'.join(['>Fragment' + str(i+1) + "\n" + j for i,j in enumerate(all_fragments)])
frag_file.write(data)
frag_file.close()


# In[17]:


# Part-4 Function to break-down the genome into 5,000 overlapping fragments with a randomly generated fragment size.
l1 = []
def random_frag_size(n, genome):
    
    for i in range(n):
        N = random.randrange(1,100)
        res = ''.join(random.choices(genome, k = N))
        l1.append(res)
    print(l1)
    
n = 5000
genome = x
random_frag_size(n, genome)
l1


# l1 = []
# n = 5000
# for i in range(n):
#     N = random.randrange(1,100)
#     res = ''.join(random.choices(x, k = N))
#     l1.append(res)
    


# In[18]:


l1


# In[23]:


# Part - 4 Calculating n50 value
"""This function calculates the N50, N90 values for an assembly. 
The N50 value is calculated by first ordering every contig/scaffold by length from longest to shortest. 
Next, starting from the longest contig/scaffold, the lengths of each contig are summed,
until this running sum equals one-half of the total length of all contigs/scaffolds in the assembly. 
Then the length of shortest contig/scaffold in this list is the N50 value"""

seq_len1 = []
sorted_list = sorted(l1, key=len, reverse = True)   #Sorting the random fragments in descending order based on length
for i in sorted_list:
    seq_len1.append(len(i))                    #Appending each fragment in a list named seq_len1
#print(seq_len1)
vo = []
count = 0
for i,event in enumerate(range(len(seq_len1))):              
    if count < 5000:
        count = i + (i+1)                           #Summing the two indexes at once until it reaches
        vo.append(event)                                              #5000 (half of total no of base pairs in a genome)
                
    else:
        break
        
        
print(count)                                       #Sum that exceepts 5000
print(len(vo))                                     
index = len(vo)                                    #Calculating the index of events

print("The n50 value is :", seq_len1[index])         #Finding the value corresponding to the last index = n50 value


# In[24]:


#Not complete 

import numpy
seq_len = []
sorted_list = sorted(l1, key=len)     #Sorting the sequencing in ascending order based on length and keeping it in a list 
                                                        #list name is seq_len
for i in sorted_list:
    seq_len.append(len(i))
#print(seq_len)

unique = []
for j in seq_len:
    if not j in unique:
        unique.append(j)             #Out of whole seq_len appnding only the unique elements into new list 
                                            #List name "unique"
#print(unique)


n50 = []

for j in unique:
    
    multiplier = seq_len.count(j)*j
    #print(multiplier)
    #print(seq_len.count(j))
    for k in range(multiplier):
        n50.append(j)
print(n50)

index = len(n50)//2
print(index)
avg = []

if index % 2 == 0:
    first = n50[index - 1]
    second = n50[index]
    avg.append(first)
    avg.append(second)
#print(avg)
    n50 = numpy.mean(avg)
    print("n50 is ", n50)
else:
     print("n50 is ", n50[index-1])


# In[ ]:




