import csv

def write_to_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Email'])
        writer.writerows(data)

def read_from_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader]
        return header, data

sample_data = [
    ['Alice', '25', 'alice@example.com'],
    ['Bob', '30', 'bob@example.com'],
    ['Charlie', '28', 'charlie@example.com']
]

write_to_csv('data.csv', sample_data)
header, data = read_from_csv('data.csv')

print("Header:", header)
print("Data:")
for row in data:
    print(row)
