class Statistics:
    def __init__(self,data = []):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def appearance(self):
        count = {}
        for number in self.data:
            count[number] = count.get(number,0)+1
        return count
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum()/self.count()
    
    def median(self):
        sorted_data = sorted(self.data)
        count = self.count()
        return sorted_data[count//2] if count%2 == 1 else (sorted_data[count//2]+sorted_data[1+(count//2)])/2

    def mode(self):
        count = self.appearance()
        res = (max(count.items(),key = lambda x: x[1]))
        output = {'mode':res[0], 'count': res[1]}
        return output
    
    def var(self):
        mean = self.mean()
        size = self.count()
        numerator = 0
        for number in self.data:
            numerator += pow(number - mean,2)
        return numerator/size
    
    def std(self):
        return pow(self.var(),1/2)
    
    def freq_dist(self):
        appearance = self.appearance().items()
        total = self.count()
        return sorted([((number[1]*100/total),number[0]) for number in appearance],key = lambda x: x[1])
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

class PersonAccount:
    def __init__(self,fname,lname,income,expense):
        self.firstname = fname
        self.lastname = lname
        self.incomes = income
        self.expenses = expense
    
    def total_income(self):
        return sum(self.incomes.values())
    
    def total_expense(self):
        return sum(self.expenses.values())
    
    def account_info(self):
        return f"This account belongs to {self.firstname} {self.lastname}. It has a total income of {self.total_income()} and a total expense of {self.total_expense()}"
    
    def add_income(self,money):
        for k,v in money.items():
            self.incomes[k] = v
        print(self.incomes)

    def add_expense(self,money):
        for k,v in money.items():
            self.expenses[k] = v
        print(self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expense()


        