from itertools import combinations

class Apriori:

    def __init__(self):
        
        pass

    def apriori(self, filename, minsup): 
    
        apriori_result = dict()

        transactions, items = self._parse_table(filename)

        self._first_iteration(transactions, items, minsup, apriori_result)

        k = 2
        while True:

            candidates = self._apriori_generation(apriori_result, k)

            if not candidates:
                break
        
            apriori_result[str(k)] = {
                "c": {

                }, "f": {

                }
            }

            for c in candidates:

                count = self._support(transactions, c)
                apriori_result[str(k)]["c"][c] = count

                if minsup <= count:
    
                    apriori_result[str(k)]["f"][c] = count

            k += 1

        return apriori_result

    def _parse_table(self, filename):

        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        transactions = []
        items = str()

        for line in lines:

            transaction = line.replace("\n", "")
            transactions.append(transaction)
            items += transaction

        items = sorted(list(set(items)))

        return transactions, items

    def _support(self, transactions, pattern):

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

    def _first_iteration(self, transactions, items, minsup, apriori_result):

        apriori_result["1"] = {
            "c": {

            }, "f": {

            }
        }

        for item in items:

            sup = self._support(transactions, item)

            apriori_result["1"]["c"][item] = sup

            if minsup <= sup:

                apriori_result["1"]["f"][item] = sup

    def _subset_generation(self, c, k):

        for comb in combinations(c, k):
            yield "".join(comb)

    def _has_infrequent_subset(self, c, k, frequent_prev):

        for s in self._subset_generation(c, k):

            if s not in frequent_prev:
                return True

        return False

    def _prefix(self, pattern):
        return pattern[:-1]

    def _last(self, pattern):
        return pattern[-1]

    def _apriori_generation(self, apriori_result, k):

        candidates = list()

        frequent_prev = list(apriori_result[str(k - 1)]["f"].keys())

        for i, p in enumerate(frequent_prev):

            for q in frequent_prev[i + 1:]:

                if self._prefix(p) == self._prefix(q) and self._last(p) < self._last(q):

                    c = p + self._last(q)

                    if self._has_infrequent_subset(c, k - 1, frequent_prev):
                        continue

                    candidates.append(c)

        return candidates

