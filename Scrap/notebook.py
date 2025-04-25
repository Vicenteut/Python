<html><head></head><body>#!/usr/bin/env python
# coding: utf-8

# # Analyze Electric Vehicle Stations in Python
# 
# - [View Solution Notebook](./solution.html)
# - [View Project Page](https://www.codecademy.com/projects/practice/analyze-electric-vehicle-stations-with-python)

# ## Task Group 1 - Import and Explore

# ### Task 1
# 
# Import the CSV file `stations.csv` and assign it to the variable `stations`.

# In[7]:


import pandas as pd
stations = pd.read_csv(&#39;stations.csv&#39;)
# show output
stations.head()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What is the structure of this dataset? Toggle to check!</i></summary>
# 
# Each row of the dataset counts the number of stations corresponding to certain categories of fuel, ownership, location, and access.
#     
# For example, let&#39;s look at the first row. The first row counts the number of
#     
#     - biodiesel stations
#     - in Alabama
#     - owned by the government
#     - with restricted/private access
# 
# The number in the last column tells us there are 8 stations matching these properties!
# 
# </details>

# ### Task 2
# 
# When we start working with a new dataset, it&#39;s a good idea to get some summaries of the different columns, so that we know what kinds of values they contain.
# 
# Call `.value_counts()` on `fuel` to see the different kinds of fuel included in the dataset.

# In[9]:


stations[&#39;fuel&#39;].value_counts()


# ### Task 3
# 
# Call `.value_counts()` on `owner` to see the different kinds of owners included in the dataset.

# In[10]:


stations[&#39;owner&#39;].value_counts()


# ### Task 4
# 
# Call `.value_counts()` on `access` to see the different kinds of access included in the dataset.

# In[11]:


stations[&#39;access&#39;].value_counts()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover using value counts? Toggle to check!</i></summary>
# 
# Using `.value_counts()` tells us the different types of stations in the dataset. For example, we now know that there are both public-access and private-access stations in the dataset.
#     
# It is important to remember that `.value_counts()` only tells us how many *rows* in the dataset contain a certain value. For example, from Task 4 we know that there are 415 rows in the dataset that contain `public` in the `access` column. This does *not* correspond to 415 stations, since each row can have a large `number_of_stations`.
# 
# </details>

# ### Task 5
# 
# Call `.describe()` on `number_of_stations`.

# In[13]:


stations[&#39;number_of_stations&#39;].describe()


# ### Task 6
# 
# There&#39;s a pretty large maximum in the output to Task 5. Sort `stations` by `number_of_stations` from largest to smallest. What do the top 5 rows have in common?

# In[14]:


stations.sort_values(by=&#39;number_of_stations&#39;,
                    ascending= False)


# ### Task 7
# 
# Sort `stations` by `number_of_stations` from smallest to largest. What do the top 5 rows of the new sorted DataFrame have in common?

# In[15]:


stations.sort_values(by=&#39;number_of_stations&#39;,
                    ascending= True)


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover using sorting? Toggle to check!</i></summary>
# 
# The five largest rows are all public-access, privately-owned, and electric. 
# 
# We can&#39;t draw too many conclusions from the five smallest rows, because there may be more than just these five rows with 1 station.
# 
# </details>

# ## Task Group 2 - Public Access Electric Charging

# ## Task 8
# 
# Electric vehicles have become more and more crucial to plans around climate change. Let&#39;s take a closer look at stations that anyone can access.
# 
# Create a Boolean mask that is `True` for any row of `stations` where `access` is public.

# In[21]:


p = stations[&#39;access&#39;] == &#39;public&#39;


# ### Task 9
# 
# Create a Boolean mask that is `True` for any row of `stations` where `fuel` is electric.

# In[22]:


e = stations[&#39;fuel&#39;] == &#39;electric&#39;


# ### Task 10
# 
# Use the Boolean masks from Tasks 8 and 9 to filter `stations` down to only rows that are both public-access and electric-fuel. Assign the result to the variable `public_electric`.

# In[25]:


public_electric = stations[p&amp;e]



# ### Task 11
# 
# Sort `public_electric` by `number_of_stations` from smallest to largest. Display the top 5 rows (corresponding to the smallest numbers of stations.)

# In[28]:


public_electric.sort_values(by=&#39;number_of_stations&#39;,
                           ascending= True).head()


# ### Task 12
# 
# While we can&#39;t be sure that this trend continues, it certainly looks as if publicly-owned (government/utility) stations are less common than privately owned (which we saw in Task 6).
# 
# Let&#39;s compare privately- and publicly-owned stations. Create a Boolean mask that is `True` for each row of `public_electric` where `owner` is private.

# In[31]:


non_private_mask = public_electric[&#39;owner&#39;] == &#39;private&#39;


# ### Task 13
# 
# Use the Boolean mask from Task 12 to filter `public_electric` down to only privately-owned rows. Assign the result to the variable `privately_owned`.

# In[33]:


privately_owned = public_electric[non_private_mask]


# ### Task 14
# 
# Let&#39;s check how many states have privately-owned, publicly-accessible electric charging stations. Call `.describe()` on the `state` column of `privately_owned`.

# In[34]:


privately_owned[&#39;state&#39;].describe()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 14? Toggle to check!</i></summary>
# 
# There are 51 unique values in the `privately_owned` state column. So it looks like all 50 states and (likely) the District of Columbia have at least one privately-owned, publicly-accessible electric charging station. 
#     
# We can&#39;t be 100% sure without actually looking at the data: it is possible that one state abbreviation got misspelled, producing a count of 51 distinct entries without actually having 51 distinct entries. But this is good initial evidence!
# </details>

# ### Task 15
# 
# Let&#39;s compare this to the publicly-owned stations. Use the Boolean mask you created in Task 12 to filter `public_electric` down to only rows with *non*-private ownership. Assign the result to the variable `not_privately_owned`.

# In[38]:


not_privately_owned = public_electric[~pp]


# ### Task 16
# 
# Let&#39;s check how many states have publicly-owned, publicly-accessible electric charging stations. Call `.describe()` on the `state` column of `not_privately_owned`.

# In[39]:


not_privately_owned[&#39;state&#39;].describe()


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 16? Toggle to check!</i></summary>
# 
# There are only 49 unique entries, so it is likely that there are two states (possibly one state and the District of Columbia) that have *zero* publicly-owned and publicly-accessible electric charging stations.
# 
# </details>

# ### Task 17
# 
# Let&#39;s investigate publicly-owned stations a bit further. Call `.describe()` on the `number_of_stations` column of `not_privately_owned`.

# In[40]:


not_privately_owned[&#39;number_of_stations&#39;].describe()


# ### Task 18
# 
# The maximum number of stations is quite a bit larger than the 75th percentile. Let&#39;s look at the rows between these values. 
# 
# Create a Boolean mask that is true in each row of `not_privately_owned` where the `number_of_stations` is bigger than 17 (the 75th percentile).

# In[41]:


bigger_than = not_privately_owned[&#39;number_of_stations&#39;] &gt; 17


# ### Task 19
# 
# Filter `not_privately_owned` down to only rows with `number_of_stations` bigger than 17. Assign the result to the variable `above_17`.

# In[44]:


above_17 = not_privately_owned[bigger_than]


# ### Task 20
# 
# Sort `above_17` by `number_of_stations` and output the entirety of the result.

# In[45]:


above_17.sort_values(by=&#39;number_of_stations&#39;)


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 20? Toggle to check!</i></summary>
# 
# There&#39;s no immediately obvious geographic pattern, though it is interesting that California has both the most government-owned and the most utility-owned stations. However, we&#39;d have to compare against population to see if that&#39;s just a factor of California&#39;s size.
#     
# Combining datasets (like `stations` with a population dataset) is beyond the scope of this project -- but is a powerful feature of pandas that you&#39;ll learn if you keep going!
# 
# </details>

# ## Task Group 3 - West Coast

# ### Task 21
# 
# In Task 20 we found that `CA` has 
# 1. the largest number of government-owned public-access electric stations
# 2. the largest number of utility-owned public-access electric stations
# 
# In Task 6, the full sorted DataFrame shows that `CA` also has the most privately-owned public-access electric stations. 
# 
# What about the rest of the west coast?
# 
# Create two Boolean masks:
# - the first should be `True` whenever the `state` column of `public_electric` is `WA` (Washington)
# - the second should be `True` whenever the `state` column of `public_electric` is `OR` (Oregon)

# In[46]:


washington = public_electric[&#39;state&#39;] == &#39;WA&#39;
oregon = public_electric[&#39;state&#39;] == &#39;OR&#39;


# ### Task 22
# 
# Filter `public_electric` down to only those rows where `state` is either `WA` or `OR`. Assign the result to the variable `WA_or_OR`.

# In[49]:


WA_or_OR = public_electric[(washington | oregon)]


# ### Task 23
# 
# Sort `WA_or_OR` first by `owner` and then, within each `owner`, by `number_of_stations`. Display the full output.

# In[51]:


WA_or_OR.sort_values(by=[&#39;owner&#39;, &#39;number_of_stations&#39;])


# <details>
#     <summary style="display:list-item; font-size:16px; color:blue;"><i>What did we discover in Task 23? Toggle to check!</i></summary>
# 
# Both WA and OR have significantly more privately-owned stations than publicly-owned (among publicly-accessible stations.) At the time this project was created, the population of WA was about double the population of OR (slightly below, in fact). Do you think the proportions of stations make sense?
# 
# </details>

# That&#39;s the end of the project, but you can always add more cells below to explore the dataset further!

# In[ ]:




<script type="text/javascript" src="/relay.js"></script></body></html>