
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.2** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-social-network-analysis/resources/yPcBs) course resource._
# 
# ---

# # Assignment 3
# 
# In this assignment you will explore measures of centrality on two networks, a friendship network in Part 1, and a blog network in Part 2.

# ## Part 1
# 
# Answer questions 1-4 using the network `G1`, a network of friendships at a university department. Each node corresponds to a person, and an edge indicates friendship. 
# 
# *The network has been loaded as networkx graph object `G1`.*

# In[2]:

import networkx as nx

G1 = nx.read_gml('friendships.gml')


# ### Question 1
# 
# Find the degree centrality, closeness centrality, and normalized betweeness centrality (excluding endpoints) of node 100.
# 
# *This function should return a tuple of floats `(degree_centrality, closeness_centrality, betweenness_centrality)`.*

# In[3]:

def answer_one():
        
    degree_centrality = nx.degree_centrality(G1)[100]
    closeness_centrality = nx.closeness_centrality(G1)[100]
    betweenness_centrality = nx.betweenness_centrality(G1,endpoints=False, normalized=True)[100]
    
    return (degree_centrality,closeness_centrality,betweenness_centrality)
#print(answer_one)


# <br>
# #### For Questions 2, 3, and 4, assume that you do not know anything about the structure of the network, except for the all the centrality values of the nodes. That is, use one of the covered centrality measures to rank the nodes and find the most appropriate candidate.
# <br>

# ### Question 2
# 
# Suppose you are employed by an online shopping website and are tasked with selecting one user in network G1 to send an online shopping voucher to. We expect that the user who receives the voucher will send it to their friends in the network.  You want the voucher to reach as many nodes as possible. The voucher can be forwarded to multiple users at the same time, but the travel distance of the voucher is limited to one step, which means if the voucher travels more than one step in this network, it is no longer valid. Apply your knowledge in network centrality to select the best candidate for the voucher. 
# 
# *This function should return an integer, the name of the node.*

# In[16]:

def answer_two():
    degree = nx.degree_centrality(G1)
    max_node = None
    max_degree = -1
    for key, value in degree.items():
        if value > max_degree:
            max_degree = value
            max_node = key
    return max_node
#print(answer_two())


# ### Question 3
# 
# Now the limit of the voucher’s travel distance has been removed. Because the network is connected, regardless of who you pick, every node in the network will eventually receive the voucher. However, we now want to ensure that the voucher reaches the nodes in the lowest average number of hops.
# 
# How would you change your selection strategy? Write a function to tell us who is the best candidate in the network under this condition.
# 
# *This function should return an integer, the name of the node.*

# In[17]:

def answer_three():
    degree = nx.closeness_centrality(G1)
    max_node = None
    max_degree = -1
    for key, value in degree.items():
        if value > max_degree:
            max_degree = value
            max_node = key
    return max_node
#print(answer_three())


# ### Question 4
# 
# Assume the restriction on the voucher’s travel distance is still removed, but now a competitor has developed a strategy to remove a person from the network in order to disrupt the distribution of your company’s voucher. Your competitor is specifically targeting people who are often bridges of information flow between other pairs of people. Identify the single riskiest person to be removed under your competitor’s strategy?
# 
# *This function should return an integer, the name of the node.*

# In[20]:

def answer_four():
    degree = nx.betweenness_centrality(G1)
    max_node = None
    max_degree = -1
    for key, value in degree.items():
        if value > max_degree:
            max_degree = value
            max_node = key
    return max_node
#print(answer_four())


# ## Part 2
# 
# `G2` is a directed network of political blogs, where nodes correspond to a blog and edges correspond to links between blogs. Use your knowledge of PageRank and HITS to answer Questions 5-9.

# In[4]:

G2 = nx.read_gml('blogs.gml')


# ### Question 5
# 
# Apply the Scaled Page Rank Algorithm to this network. Find the Page Rank of node 'realclearpolitics.com' with damping value 0.85.
# 
# *This function should return a float.*

# In[23]:

def answer_five():
    pr = nx.pagerank(G2,alpha=0.85)
    return pr['realclearpolitics.com']
#print(answer_five())


# ### Question 6
# 
# Apply the Scaled Page Rank Algorithm to this network with damping value 0.85. Find the 5 nodes with highest Page Rank. 
# 
# *This function should return a list of the top 5 blogs in desending order of Page Rank.*

# In[32]:

def answer_six():
        
    pr = nx.pagerank(G2,alpha=0.85)
    pr_desc = sorted(pr.keys(),key= pr.__getitem__, reverse= True) 
    return pr_desc[:5]
#answer_six()


# ### Question 7
# 
# Apply the HITS Algorithm to the network to find the hub and authority scores of node 'realclearpolitics.com'. 
# 
# *Your result should return a tuple of floats `(hub_score, authority_score)`.*

# In[28]:

def answer_seven():
    hub , authority = nx.hits(G2)
    hub_score = hub['realclearpolitics.com']
    authority_score = authority['realclearpolitics.com']
    return hub_score,authority_score
#answer_seven()


# ### Question 8 
# 
# Apply the HITS Algorithm to this network to find the 5 nodes with highest hub scores.
# 
# *This function should return a list of the top 5 blogs in desending order of hub scores.*

# In[35]:

def answer_eight():
        hub , authority = nx.hits(G2)
        hub_desc = sorted(hub.keys(),key = hub.__getitem__,reverse = True)
        return hub_desc[:5]
#answer_eight()


# ### Question 9 
# 
# Apply the HITS Algorithm to this network to find the 5 nodes with highest authority scores.
# 
# *This function should return a list of the top 5 blogs in desending order of authority scores.*

# In[37]:

def answer_nine():  
    hub , auth = nx.hits(G2)
    auth_desc = sorted(auth.keys(),key = auth.__getitem__,reverse = True)
    return auth_desc[:5]
answer_nine()

