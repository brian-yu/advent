import re

file = open('input.txt')
contents = file.read()[:-1]  # remove last newline

lines = [line.replace('\n', ' ').split(' ') for line in contents.split("\n\n")]
lines = [[pair.split(':') for pair in line] for line in lines]


passports = [{pair[0]: pair[1] for pair in line} for line in lines]

print(passports)

def validator(passport):
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if key not in passport:
            return False
    
    return True

def validate_passports(passports, validator):
    count = 0

    for passport in passports:
        if validator(passport):
            count += 1
    
    return count

def strict_validator(passport):
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if key not in passport:
            return False
    
    try:
        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
    except:
        return False

    if byr < 1920 or byr > 2002:
        return False
    
    if iyr < 2010 or iyr > 2020:
        return False
    
    if eyr < 2020 or eyr > 2030:
        return False

    hgt_match = re.match(r'(\d+)(cm|in)$', hgt)
    if not hgt_match:
        return False
    
    hgt_val = int(hgt_match.group(1))
    hgt_unit = hgt_match.group(2)

    if hgt_unit == 'cm' and (hgt_val < 150 or hgt_val > 193):
        return False
    
    if hgt_unit == 'in' and (hgt_val < 59 or hgt_val > 76):
        return False
    
    if not re.match(r'#[0-9a-f]{6}$', hcl):
        return False
    
    if ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    
    if not re.match(r'\d{9}$', pid):
        return False
    print(passport)
    return True


print(validate_passports(passports, validator))

print(validate_passports(passports, strict_validator))