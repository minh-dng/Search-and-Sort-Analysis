# %% [markdown]
# # Comparing Binary and Linear Search

# %% [markdown]
# ## Configuration

# %% [markdown]
# ### Import

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from IPython.display import clear_output

# %% [markdown]
# ### Ramdom setup

# %%
def int_check(prompt, top = None):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Check input")
            continue
        
        if top is None and value < 0:
            print("Please input a number larger than 0")
            continue

        if top is not None and value < range_low:
            print("Invalid top end")
            continue
        clear_output()
        return value


seed_info = int_check("Choose your seed ( > 0 ): ")

range_low = int_check("Choose the bottom end of your randomness ( > 0 ): ")

range_high = int_check("Choose the top end of your randomness ( > 0 ): ", True)

random_size = int_check("Choose the size of the array ( > 0 ): ")

np.random.seed(seed_info)

arr = np.random.randint(low = range_low, high = range_high, size = random_size)

exec_unsort = input("CONFIRMING LINEAR search on UNSORTED array (yes): ")

exec_sort = input("CONFIRMING LINEAR search on SORTED array (yes): ")

# %% [markdown]
# ### Duplication handling

# %%
unique_arr_unsorted = pd.unique(arr)

unique_arr_sorted = np.sort(unique_arr_unsorted)

print(f"{arr.size - unique_arr_sorted.size} duplicate values removed from array")
print(f"{unique_arr_sorted.size} values remaining")

# %% [markdown]
# ## **_Binary_ Search** ##

# %%
def BinarySearch():

    start = timer() # Performance - Start timer

    min_value = 0
    max_value = unique_arr_sorted.size
    found = False

    while min_value <= max_value:
        mid_value = int(min_value + (max_value - min_value) / 2)
        if unique_arr_sorted[mid_value] == tofind:
            end = timer() # Performance - End timer
            found = True
            return start, end, found
        elif tofind < unique_arr_sorted[mid_value]:
            max_value = mid_value - 1
        else:
            min_value = mid_value + 1

bs_performance = []

for tofind in unique_arr_sorted:
    start, end, found = BinarySearch()
    if found:
        bs_performance.append((end - start)*10**6)

dict_binary = {'Number': unique_arr_sorted, 'Time (microseconds)': bs_performance}

dict_binary_df = pd.DataFrame(dict_binary)

# %% [markdown]
# ## **_Linear_ Search**
# Be aware of the computing power and time this would taken

# %% [markdown]
# ### General Function

# %%
def LinearSearch(arraytosearch):

    start = timer() # Performance - Start timer

    found = False

    for item in arraytosearch:
        if tofind == item:
            end = timer() # Performance - End timer
            found = True
            return start, end, found   

# %% [markdown]
# ### *Unsorted* array

# %%
if exec_unsort.lower() == 'yes':
    ls_unsorted_performance = []

    for tofind in unique_arr_unsorted:
        start, end, found = LinearSearch(unique_arr_unsorted)
        if found:
            ls_unsorted_performance.append((end-start)*10**6)

    dict_linear_unsorted = {'Number': unique_arr_unsorted, 'Time (microseconds)': ls_unsorted_performance}

    dict_linear_unsorted_df = pd.DataFrame(dict_linear_unsorted)

    dict_linear_unsorted_df = dict_linear_unsorted_df.sort_values(by = ['Number'])

# %% [markdown]
# ### *Sorted* array

# %%
if exec_sort.lower() == 'yes':
    ls_sorted_performance = []

    for tofind in unique_arr_sorted:
        start, end, found = LinearSearch(unique_arr_sorted)
        if found:
            ls_sorted_performance.append((end-start)*10**6)

    dict_linear_sorted = {'Number': unique_arr_sorted, 'Time (microseconds)': ls_sorted_performance}

    dict_linear_sorted_df = pd.DataFrame(dict_linear_sorted)

    dict_linear_sorted_df = dict_linear_sorted_df.sort_values(by = ['Number'])

# %% [markdown]
# ## Performance visualisation

# %% [markdown]
# ### Binary Search
# *log(n)* trend line

# %%
plt.figure()
ax1 = dict_binary_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 14, loglog = True)
ax1.set_ylabel('Time (microseconds)',fontdict={'fontsize' : 15})
ax1.set_xlabel('Number',fontdict={'fontsize' : 15})
ax1.set_title('Binary Search Performance', fontdict={'fontsize': 15})

# %% [markdown]
# ### Linear Search

# %% [markdown]
# #### Unsorted Array

# %%
if exec_unsort.lower() == 'yes':
    plt.figure()
    ax2 = dict_linear_unsorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 14, loglog = True)
    ax2.set_ylabel('Time (microseconds)',fontdict={'fontsize' : 15})
    ax2.set_xlabel('Number',fontdict={'fontsize' : 15})
    ax2.set_title('Linear Search - Unsorted - Performance', fontdict={'fontsize': 15})

# %% [markdown]
# #### Sorted Array

# %%
if exec_sort.lower() == 'yes':
    plt.figure()
    ax3 = dict_linear_sorted_df.plot(x = 'Number', y = 'Time (microseconds)', kind = 'scatter', figsize = (30 , 10), fontsize = 14, loglog = True)
    ax3.set_ylabel('Time (microseconds)',fontdict={'fontsize' : 15})
    ax3.set_xlabel('Number',fontdict={'fontsize' : 15})
    ax3.set_title('Linear Search - Sorted - Performance', fontdict={'fontsize': 15})


