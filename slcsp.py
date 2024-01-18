from collections import defaultdict
import csv
import sys

# organize plans.csv by state and rate area with corresponding plan costs
# rates['<state> <rate area>'] = [<cost1>, <cost2>, ...]
# rates['MD 1'] = [195.54, 245.42, ...]
rates = defaultdict(list)

with open('plans.csv') as csvfile:
    planreader = csv.reader(csvfile)
    for row in planreader:
        if row[2] == 'Silver':  # only keep Silver plans
            key = f'{row[1]} {row[4]}'
            value = float(row[3])
            rates[key].append(value)

# organize zips.csv by the states and rate areas each zipcode contains
# zips_areas['<zipcode>'] = ['<state> <rate area1>', '<state> <rate area2>', ...]
# zips_areas['64148'] = ['MO 3', 'MO 3', ...]
zips_areas = defaultdict(list)

with open('zips.csv') as csvfile:
    zipreader = csv.reader(csvfile)
    for row in zipreader:
        zips_areas[row[0]].append(f'{row[1]} {row[4]}')

# iterate list of target zipcodes, adding slcsp values where found
results = []
with open('slcsp.csv') as csvfile:
    slcspreader = csv.reader(csvfile)
    header_row = next(slcspreader)
    results.append([header_row[0],header_row[1]])

    for row in slcspreader:
        zipcode = row[0]
        slcsp_result = ''
        target_state_area = zips_areas[zipcode]
        # check that the zipcode only contains ONE rate area
        if len(set(target_state_area)) == 1:
            target_in_rates = target_state_area[0]
            # use set() to deduplicate in case 2 plans have the same cost
            plan_costs = sorted(list(set(rates[target_in_rates])))
            # check that there are at least 2 remaining plan costs
            if len(plan_costs) > 1:
                slcsp_result = format(plan_costs[1], '.2f')
        results.append([zipcode, slcsp_result])

# write results to stdout in csv format matching input 'slcsp.csv'
slcspwriter = csv.writer(sys.stdout)
slcspwriter.writerows(results)
