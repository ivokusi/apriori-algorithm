from itertools import combinations

def parse_table(filename):

    file = open(filename, "r")
    lines = file.readlines()

    transactions = []
    items = str()

    for line in lines:

        transaction = line.replace("\n", "")
        transactions.append(transaction)
        items += transaction

    items = sorted(list(set(items)))

    return transactions, items

def support(transactions, pattern):

    sup = 0

    for transaction in transactions:

        flag = 0

        for item in pattern:

            if item not in transaction:

                flag = 1
                break

        if not flag:

            sup += 1

    return sup

def first_iteration(transactions, items, minsup, apriori_result):

    apriori_result[1] = {
        "c": {

        }, "f": {

        }
    }

    for item in items:

        sup = support(transactions, item)

        apriori_result[1]["c"][item] = sup

        if minsup <= sup:

            apriori_result[1]["f"][item] = sup

def subset_generation(c, k):

    for comb in combinations(c, k):
        yield "".join(comb)

def has_infrequent_subset(c, k, frequent_prev):

    for s in subset_generation(c, k):

        if s not in frequent_prev:
            return True

    return False

def prefix(pattern):
    return pattern[:-1]

def last(pattern):
    return pattern[-1]

def apriori_generation(apriori_result, k):

    candidates = list()

    frequent_prev = list(apriori_result[k - 1]["f"].keys())

    for i, p in enumerate(frequent_prev):

        for q in frequent_prev[i + 1:]:

            if prefix(p) == prefix(q) and last(p) < last(q):

                c = p + last(q)

                if has_infrequent_subset(c, k - 1, frequent_prev):
                    continue

                candidates.append(c)

    return candidates

def apriori(filename, minsup): 

    apriori_result = dict()

    transactions, items = parse_table(filename)

    first_iteration(transactions, items, minsup, apriori_result)

    k = 2
    while True:

        candidates = apriori_generation(apriori_result, k)

        if not candidates:
            break
        
        apriori_result[k] = {
            "c": {

            }, "f": {

            }
        }

        for c in candidates:

            count = support(transactions, c)
            apriori_result[k]["c"][c] = count

            if minsup <= count:
    
                apriori_result[k]["f"][c] = count

        k += 1

    return apriori_result

