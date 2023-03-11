# creating forest using dictionary

Families={
           'charley':
                    {'sam':{'boxy','rosy'},
                     'nila':{'pepsi'}},
           'devi':
                   {'tommy':{'tony'},
                    'timmy':{'hamster'},
                    'tammy':{'lobster'}},
           'carlos':
                   {'deigo':'cat','ferret':'fox'}
           }
for parent,children in Families.items():
    print(f"{parent} has {len(children)} kids :")
    print(f"{','.join([str(child) for child in [*children]])}")
        
