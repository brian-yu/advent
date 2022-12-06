use crate::Solution;
use std::{
    collections::{HashSet, VecDeque},
    fs,
};

pub struct Day {
    pub input_path: String,
}

fn unique(deque: &VecDeque<&char>) -> bool {
    let set: HashSet<&&char> = HashSet::from_iter(deque);
    set.len() == deque.len()
}

fn unique_substring_end(s: &str, n: usize) -> usize {
    let chars: Vec<char> = s.chars().collect();

    let mut deque = VecDeque::from_iter(chars.iter().take(n));
    let mut idx = n;
    for char in chars.iter().skip(n) {
        if unique(&deque) {
            break;
        }

        deque.pop_front();
        deque.push_back(char);

        idx += 1;
    }

    idx
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        println!("{}", unique_substring_end(input.trim(), 4));
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        println!("{}", unique_substring_end(input.trim(), 14));
    }
}
