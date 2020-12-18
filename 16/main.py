my_ticket = [179,101,223,107,127,211,191,61,199,193,181,131,89,109,197,59,227,53,103,97]

def validateValue(value, rules):
  values = []
  for key in rules.keys():
    if not (
      (value >= rules[key][0] and value <= rules[key][1]) or 
      (value >= rules[key][2] and value <= rules[key][3])
    ): values.append(False)
    else: values.append(True)

  return True in values

def validateValueWithKey(value, rules, key):
  return ((value >= rules[key][0] and value <= rules[key][1]) or (value >= rules[key][2] and value <= rules[key][3]))
  
  

def classifyField(index, tickets, rules, validated_keys):
  for key in rules.keys():
    if key in validated_keys: continue
    validation_table = []
    for ticket in tickets:
      validation_table.append(validateValueWithKey(ticket[index], rules, key))
    if not False in validation_table: return key
  return 'invalid field'

def partII(tickets, rules):
  valid_tickets = []
  for ticket in tickets:
    validation_table = []
    for value in ticket:
      validation_table.append(validateValue(value, rules))
    if not False in validation_table: valid_tickets.append(ticket)

  values_map = {}
  for i in range(len(valid_tickets[0])):
    values_map[i + 1] = classifyField(i, valid_tickets, rules, values_map.values())
  
  return values_map



def partI(tickets, rules):
  invalid_values = []

  for ticket in tickets:
    for value in ticket:
      if not validateValue(value, rules): invalid_values.append(value)

  return sum(invalid_values)

def main():
  rule_lines = open('rules.txt').readlines()
  ticket_lines = open('tickets.txt').readlines()
  ruleset = {}
  tickets = []
  for rule in rule_lines:
    key_values = rule.split(':')
    key = key_values[0].replace(' ', '_')
    values = key_values[1].replace('\n', '').strip()
    ruleset[key] = [
      int(values.split('or')[0].strip().split('-')[0]),
      int(values.split('or')[0].strip().split('-')[1]),
      int(values.split('or')[1].strip().split('-')[0]),
      int(values.split('or')[1].strip().split('-')[1])
    ]
  
  for ticket in ticket_lines:
    formated = ticket.replace('\n', '')
    ticket_values = [int(value) for value in formated.split(',')]
    tickets.append(ticket_values)

  print(partI(tickets, ruleset))  
  print(partII(tickets, ruleset))

if __name__ == "__main__":
  main()