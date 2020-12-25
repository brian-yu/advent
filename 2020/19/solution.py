import re

file = open('input.txt')

rule_strs, messages = [chunk.split('\n') for chunk in file.read()[:-1].split('\n\n')]

rule_matches = [re.match(r'(\d+): (.+)', s) for s in rule_strs]
rules_dict = {int(match.group(1)): match.group(2) for match in rule_matches}

def get_rule_matches(rules_dict, rule_str):
    matches = set()

    match = re.match(r'^"([a-z])"$', rule_str)
    if match:
        return set([match.group(1)])
    match = re.match(r'^(\d+)$', rule_str)
    if match:
        return get_rule_matches(rules_dict, rules_dict[int(match.group(1))])
    match = re.match(r'^\d+( \d+)+$', rule_str)
    if match:
        rule_ids = [rule_id for rule_id in rule_str.split(' ')]
        left_matches = get_rule_matches(rules_dict, rule_ids[0])
        right_matches = get_rule_matches(rules_dict, " ".join(rule_ids[1:]))
        matches = set()
        for left_match in left_matches:
            for right_match in right_matches:
                matches.add(left_match + right_match)
        return matches
    match = re.match(r'^(.+) \| (.+)$', rule_str)
    if match:
        return get_rule_matches(rules_dict, match.group(1)) | get_rule_matches(rules_dict,match.group(2))
    
    raise Exception(f'invalid rule: {rule_str}')

print(len(set(messages) & get_rule_matches(rules_dict, rules_dict[0])))

MATCHES_42 = get_rule_matches(rules_dict, rules_dict[42])
MATCHES_31 = get_rule_matches(rules_dict, rules_dict[31])

def matches_8(s):
    for match in MATCHES_42:
        if s.startswith(match):
            if s == match or matches_8(s[len(match):]):
                return True
    return False

def matches_11(s):
    for match_42 in MATCHES_42:
        for match_31 in MATCHES_31:
            match = s.startswith(match_42) and s.endswith(match_31)
            if match and len(s) >= len(match_42) + len(match_31):
                inner = s[len(match_42):-len(match_31)]
                if inner == "" or matches_11(inner):
                    return True
    return False

def matches_0(s):
    for split in range(1, len(s)):
        if matches_8(s[:split]) and matches_11(s[split:]):
            return True
    return False

print(sum(matches_0(message) for message in messages))
