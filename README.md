# adhoc_slcsp
## Ad Hoc's Slcsp Homework Problem

Found here: https://homework.adhoc.team/slcsp/

Prompt also in 'problem_statment.md'

'silver_plans_sorted.csv' allows for easy spot-checking of results.

### Step 1: organize plans.csv into 'rates' dict
- iterate over file, only storing rows with 'Silver' plans
    - create new key that is "<state> <rate_area>" Ex. "GA 7"
    - value is a list of rates

### Step 2: load zips.csv into 'zips_areas' dict
- iterate over file, add or augment dict entries
    - key is 'zip', value is a new or augmented list of 'rate_area'

### Step 3: find SLCSP for each zipcode in slcsp.csv
- find all instances of 'target' zipcode in zips.csv
    - if all rate_area values are the same for the zipcode
        - use tuple of state and rate area to lookup costs in 'rates' dict
        - if not present in 'rates' dict return ''
        - elif only one cost from lookup return ''
        - else return second lowest cost