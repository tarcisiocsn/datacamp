# Notes python codes

#### Data manipulation with pandas
```python
df.describe()
df.shape()
```
Sorting and subsetting rows
```python
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals", ascending=True)

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending=False)

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"], ascending = [True, False])

# now subsetting rows
# Select the state and family_members columns
state_fam = homelessness[["state","family_members"]]
```

more of subsetting rows (filtering)

```python
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"]>10000]

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"]=="Mountain"]
```


