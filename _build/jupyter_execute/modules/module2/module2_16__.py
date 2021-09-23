#!/usr/bin/env python
# coding: utf-8

# # Data Filtering
# 
# :::{admonition} Watch it
# See the accompanied youtube video at <a href="https://www.youtube.com/embed/WCWi1R2CQsY?start=847&end=1221" target="_blank">the link here.</a>
# :::

# In[1]:


import pandas as pd
import numpy as np

pd.set_option('display.width', 350)
np.set_printoptions(linewidth=400)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 20)


# Filtering is probably one of the most frequent data manipulations you
# will do in data analysis.
# 
# Filtering is often used when we are either trying to rid the dataframe
# of unwanted rows or trying to analyze rows with a particular column
# value.
# 
# Let’s try to filter the `cereal.csv` dataset.

# In[2]:


cereal = pd.read_csv('cereal.csv')
cereal.head()


# ## Conditions
# 
# Suppose you are trying to find the information for cereals with a
# protein content greater than 4g per serving.
# 
# Our first instinct would be to write code that looks somewhat like this.

# In[3]:


cereal['protein'] > 4


# This can be translated as
# 
# *“From the `protein` column in the dataframe `cereal`, which have values
# greater than 4?”*
# 
# The output shows all the index labels and a column with `True` or
# `False` values depending on if the row meets the condition. Cereals with
# `True` have a protein content greater than 4 and `False` if they do not.
# 
# But we want a dataframe with all the information that only contains the
# rows with protein above 4.
# 
# How can this be achieved?
# 
# We can do this by indexing into our `cereal` dataframe using this column
# of True/False values. The result is a smaller dataframe that only
# contains the rows corresponding to the `True` values.

# In[4]:


cereal[cereal['protein'] > 4]


# This code can be translated to:
# 
# *Select the rows from the `cereal` dataframe that, according to the
# `cereal` dataframe, have a `protein` values greater than 4.*
# 
# We can see from the output that only the rows meeting the condition are
# displayed.
# 
# By the way, it is a common pattern that we’re using the same dataframe
# twice, namely `cereal`, but it’s not strictly required by pandas.
# 
# We can do this with equalities as well.

# In[5]:


cereal[cereal['protein'] == 4]


# Now we get all the cereals with a protein content of exactly 4g per
# serving.
# 
# The key point to remember here is that we use **two** equal signs.
# 
# In Python, a single `=` is used as an assignment operator. We are
# setting something to equal something else.
# 
# The double equal sign operator is used for comparison. We check if
# certain values are equivalent to one another.
# 
# 
# By the way, these conventions were set a long time ago when people made
# the early programming languages. In hindsight, maybe something like `=?`
# would have been more clear, but the double equal sign for comparison is
# now a standard.
# 
# 
# We can filter categorical columns too. In this example, we only want
# cereals from the manufacturer “Q” (For Quaker):
# 
# Here, we are using the double equal sign operator that we saw in the
# last slide.

# In[6]:


cereal[cereal['mfr'] == 'Q']


# ## Multiple Condition Filtering - “and”
# 
# We now know how to filter on one condition but how do we filter if we
# have many?
# 
# Perhaps we only want cereals with protein content between 4 to 5 grams?
# 
# To find the cereals that meet protein contents greater or equal to 4, we
# use the code shown here.

# In[7]:


cereal[cereal['protein'] >= 4]


# And the cereals that meet the condition of protein content below or
# equal to 5 would be obtained as shown here.

# In[8]:


cereal[cereal['protein'] <= 5]


# We can combine the two conditions using the `&` operator. This allows us
# to obtain cereals that meet **both** conditions.

# In[9]:


cereal[cereal['protein'] >= 4]


# In[10]:


cereal[cereal['protein'] <= 5]


# In[11]:


cereal[(cereal['protein'] >= 4) & (cereal['protein'] <= 5)]


# The `&` indicates “and”. This means that both conditions must hold for a
# row to be included in the new dataframe.
# 
# Each condition is wrapped with parentheses to keep them clearly
# separated.
# 
# Only rows present in **both** dataframes will be selected.
# 
# <img src='../imgs/module2/condition_and.png'  alt="404 image"/> 
# 
# 
# Next, we will look at a case where we filter on two different columns.
# 
# Let’s say we only want cereals from the Quaker manufacturer, with a
# protein content greater than 4.
# 
# The same coding syntax can be applied to two different column
# conditions.

# In[12]:


cereal[(cereal['mfr'] == 'Q') & (cereal['protein'] > 4)]


# ## Multiple Condition Filtering - “or”
# 
# Suppose that we are interested in cereals that either are made from the
# Quaker manufacturer **OR** a protein content above 4.
# 
# For a row to be included in the output, we only require one or the other
# condition to hold.
# 
# Instead of using the `&` symbol, we use `|` which is called the “pipe
# operator”. This means “or” in the Python programming language (and many
# other languages).

# In[13]:


cereal[(cereal['mfr'] == 'Q') | (cereal['protein'] > 4)]


# When we filter using “or” this time, it resulted in 10 cereals that met
# either of the conditions.
# 
# When we filtered using “and”, only 1 cereal met both conditions.
# 
# 
# <img src='../imgs/module2/condition_or.png'  alt="404 image"/> 
# 
# 
# 
# 
# ## Tilde
# 
# We saw that when we filter the conditions are expressed with an
# underlying column with `True` or `False` values indicating if the
# condition has been met in each row of the dataframe.
# 
# But what if I wanted the rows that were the complement (or opposite) of
# this?

# In[14]:


cereal['protein'] > 4


# In[15]:


(cereal['protein'] > 4).head()


# The opposite of `cereal['protein'] > 4` is `cereal['protein'] <= 4`, so
# that one isn’t too tricky. But sometimes taking the opposite is not so
# straightforward. This is where the `~` (“tilde”) operator can be
# helpful.
# 
# 
# Tilde converts all the `True` values to `False` and all the `False`
# values, to `True.`

# In[16]:


(~(cereal['protein'] > 4)).head()


# *Tilde* (`~`) gives us the ability to return the complement of the code
# following it.
# 
# 
# We can obtain the complete dataframe by putting the entire condition
# within our square brackets like we did before.
# 
# What we have here, is taking the rows where the protein content is not
# greater than four.

# In[17]:


cereal[~(cereal['protein'] > 4)]


# This gives us more versatility when filtering, especially when we want
# the inverse of more complicated conditions and verbs (you’ll see this in
# Module 3).
# 
# :::{admonition} Let’s apply what we learned!
# 
# 1\. If the output of     
# 
# ```python 
# df['location'] == 'Canada'
# ```
#  is 
#  
#  ```out
#  [ True, False, False, True]
#  ```
#  
#  What would be the output of 
#  
#  ```python
#   ~(df['location'] == 'Canada')
# ```
#  
# a) `[True, False, False, True]`      
# b) `[False, False, False, False]`       
# c) `[True, True, True, True]`         
# d) `[False, True, True, False]`         
# 
# :::
# 
# 
# ```{admonition} Solutions!
# :class: tip, dropdown
# 
# 1. d) `[False, True, True, False]`    
# 
# ```
