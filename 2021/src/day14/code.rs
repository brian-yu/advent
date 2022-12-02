use crate::Solution;
use std::{
    collections::{HashMap, LinkedList},
    fmt::{self, Display},
    fs,
    hash::Hash,
};

pub struct Day {
    pub input_path: String,
}

struct Polymer {
    chars: Vec<char>,
    insertion_rules: HashMap<String, char>,
}

impl Polymer {
    fn new(template: &str, rules_str: &str) -> Polymer {
        let chars = template.chars().collect::<Vec<char>>();

        let mut insertion_rules = HashMap::new();
        for rule in rules_str.split('\n') {
            let (pair, insert) = rule.split_once(" -> ").unwrap();
            insertion_rules.insert(pair.to_string(), insert.chars().next().unwrap());
        }

        Polymer {
            chars,
            insertion_rules,
        }
    }

    fn run_step(&mut self) {
        let mut insertions = vec![];
        for i in 0..self.chars.len() - 1 {
            let pair = self.chars[i..i + 2].iter().collect::<String>();
            if self.insertion_rules.contains_key(&pair) {
                insertions.push((i + 1, self.insertion_rules.get(&pair).unwrap()))
            }
        }
        for (offset, (i, insert)) in insertions.iter().enumerate() {
            self.chars.insert(i + offset, **insert);
        }
    }

    fn element_frequencies(&self) -> HashMap<char, usize> {
        let mut frequencies = HashMap::new();

        for char in &self.chars {
            frequencies.insert(*char, frequencies.get(char).unwrap_or(&0) + 1);
        }

        frequencies
    }
}

impl Display for Polymer {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.chars.iter().collect::<String>())
    }
}

// struct Node {
//     next:
// }
struct PolymerLL {
    chars: LinkedList<char>,
    insertion_rules: HashMap<String, char>,
}

impl PolymerLL {
    fn new(template: &str, rules_str: &str) -> PolymerLL {
        let chars = template.chars().collect::<LinkedList<char>>();

        let mut insertion_rules = HashMap::new();
        for rule in rules_str.split('\n') {
            let (pair, insert) = rule.split_once(" -> ").unwrap();
            insertion_rules.insert(pair.to_string(), insert.chars().next().unwrap());
        }

        PolymerLL {
            chars,
            insertion_rules,
        }
    }

    fn run_step(&mut self) {
        // let mut insertions = vec![];

        let mut cursor = self.chars.cursor_front_mut();
        let mut maybe_prev: Option<char> = None;
        while let Some(curr) = &cursor.current() {
            if let Some(prev) = maybe_prev {
                let pair = [prev, **curr].iter().collect::<String>();
                if let Some(inserted) = self.insertion_rules.get(&pair) {
                    cursor.insert_before(*inserted);
                    // cursor.move_next();
                }
            }

            maybe_prev = Some(*cursor.current().unwrap());

            cursor.move_next();
        }

        // let mut cursor = self.chars.cursor_front();
        // let mut idx = 0;
        // let mut offset = 0;
        // while let Some(curr) = cursor.current() {
        //     if let Some(prev) = cursor.peek_prev() {
        //         let pair = [*prev, *curr].iter().collect::<String>();
        //         if self.insertion_rules.contains_key(&pair) {
        //             insertions.push((idx, self.insertion_rules.get(&pair).unwrap()))
        //         }
        //     }
        //     idx += 1;

        //     cursor.move_next();
        // }
    }

    fn element_frequencies(&self) -> HashMap<char, usize> {
        let mut frequencies = HashMap::new();

        for char in &self.chars {
            frequencies.insert(*char, frequencies.get(char).unwrap_or(&0) + 1);
        }

        frequencies
    }
}

impl Display for PolymerLL {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.chars.iter().collect::<String>())
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let (template, rules_str) = input.trim().split_once("\n\n").unwrap();

        let mut polymer = Polymer::new(template, rules_str);

        for _ in 0..10 {
            polymer.run_step();
        }

        let freqs = polymer.element_frequencies();

        println!(
            "{}",
            freqs.values().max().unwrap() - freqs.values().min().unwrap()
        )
    }

    fn part_2(&self) {
        // let input = fs::read_to_string(&self.input_path).unwrap();
        let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let (template, rules_str) = input.trim().split_once("\n\n").unwrap();

        let mut polymer = PolymerLL::new(template, rules_str);

        for step in 0..40 {
            polymer.run_step();
            println!("After step {}", step);
            println!("{}", polymer);
        }

        let freqs = polymer.element_frequencies();

        println!(
            "{}",
            freqs.values().max().unwrap() - freqs.values().min().unwrap()
        )
    }
}
