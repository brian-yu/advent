use crate::Solution;
use std::collections::{HashMap, HashSet};
use std::fs;

pub struct Day {
    pub input_path: String,
}

const CHARS: [char; 7] = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];

fn permutations(mut chars: HashSet<char>, len: u8) -> Vec<String> {
    if len == 0 {
        return vec!["".to_string()];
    }

    let mut sub_perms = Vec::new();

    for char in chars.clone() {
        chars.remove(&char);
        sub_perms.extend(
            permutations(chars.clone(), len - 1)
                .iter()
                .map(|sub_perm| format!("{}{}", char, sub_perm)),
        );
        chars.insert(char);
    }

    sub_perms
}

fn decode(s: &str) -> Option<u8> {
    match s {
        "abcefg" => Some(0),
        "cf" => Some(1),
        "acdeg" => Some(2),
        "acdfg" => Some(3),
        "bcdf" => Some(4),
        "abdfg" => Some(5),
        "abdefg" => Some(6),
        "acf" => Some(7),
        "abcdefg" => Some(8),
        "abcdfg" => Some(9),
        _ => None,
    }
}

fn translate(signal: &str, mapping: &HashMap<char, char>) -> Option<u8> {
    let mut char_arr = signal
        .chars()
        .map(|char| *mapping.get(&char).unwrap())
        .collect::<Vec<char>>();
    char_arr.sort();

    let translated_signal = char_arr.iter().collect::<String>();

    decode(&translated_signal)
}

fn validate_mapping(signals: &[&str], mapping: &HashMap<char, char>) -> bool {
    let mut results = HashSet::new();
    for signal in signals {
        if let Some(translation) = translate(signal, mapping) {
            results.insert(translation);
        } else {
            return false;
        }
    }

    results.len() == 10
}

fn find_mapping(
    signals: &[&str],
    outputs: &[&str],
    permutations: &Vec<HashMap<char, char>>,
) -> Option<u32> {
    for mapping in permutations {
        if validate_mapping(signals, mapping) {
            let d: Vec<u8> = outputs
                .iter()
                .map(|output| translate(output, mapping).unwrap())
                .collect();

            let res: u32 = d.iter().fold(0, |acc, item| acc * 10 + *item as u32);
            return Some(res);
        }
    }

    None
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut count = 0;

        for line in input.trim().split('\n') {
            let (_, output) = line.split_once(" | ").unwrap();

            for value in output.split(' ') {
                match value.len() {
                    2 | 3 | 4 | 7 => count += 1,
                    _ => (),
                }
            }
        }

        println!("{}", count);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let permutations = permutations(CHARS.into_iter().collect(), 7);
        let mut potential_mappings: Vec<HashMap<char, char>> = Vec::new();

        for perm in permutations {
            let mut map = HashMap::new();
            for (idx, char) in perm.chars().enumerate() {
                map.insert(CHARS[idx], char);
            }
            potential_mappings.push(map);
        }

        let mut result = 0;

        for line in input.trim().split('\n') {
            let mut inputs = line
                .split(" | ")
                .map(|s| s.split(' ').collect::<Vec<&str>>());
            let signals = inputs.next().unwrap();
            let outputs = inputs.next().unwrap();

            result += find_mapping(&signals, &outputs, &potential_mappings).unwrap();
        }

        println!("{}", result);
    }
}
