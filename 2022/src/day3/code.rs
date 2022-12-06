use crate::Solution;
use std::{collections::HashSet, fs};

pub struct Day {
    pub input_path: String,
}

fn item_priority(c: char) -> u32 {
    if c.is_uppercase() {
        (c as u32) - ('A' as u32) + 27
    } else {
        (c as u32) - ('a' as u32) + 1
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut score = 0;

        for line in input.trim().split('\n') {
            let num_chars = line.chars().count();
            let first: HashSet<char> = HashSet::from_iter(line.chars().take(num_chars / 2));
            let second: HashSet<char> = HashSet::from_iter(line.chars().skip(num_chars / 2));

            score += item_priority(*first.intersection(&second).next().unwrap());
        }

        println!("{}", score);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(self.input_path.replace("input", "test")).unwrap();

        let rucksacks = input.trim().split('\n');

        let mut score = 0;

        for group in rucksacks.array_chunks::<3>() {
            let mut sets: Vec<HashSet<char>> = group
                .iter()
                .map(|line| HashSet::from_iter(line.chars()))
                .collect();

            let (intersection, others) = sets.split_at_mut(1);
            let intersection = &mut intersection[0];
            for other in others {
                intersection.retain(|e| other.contains(e));
            }

            score += item_priority(*intersection.iter().next().unwrap());
        }

        println!("{}", score);
    }
}
