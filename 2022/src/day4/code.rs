use crate::Solution;
use std::fs;

pub struct Day {
    pub input_path: String,
}

struct Interval {
    start: u32,
    end: u32,
}

impl Interval {
    fn from_str(s: &str) -> Interval {
        let mut nums = s.split('-').map(|item| item.parse::<u32>().unwrap());

        Interval {
            start: nums.next().unwrap(),
            end: nums.next().unwrap(),
        }
    }

    fn contains(&self, other: &Interval) -> bool {
        self.start <= other.start && self.end >= other.end
    }

    fn overlaps(&self, other: &Interval) -> bool {
        self.start >= other.start && self.start <= other.end
            || self.end >= other.start && self.end <= other.end
            || other.start >= self.start && other.start <= self.end
    }
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut sum = 0;

        for line in input.trim().split('\n') {
            let (first_str, second_str) = line.split_once(',').unwrap();
            let first = Interval::from_str(first_str);
            let second = Interval::from_str(second_str);

            if first.contains(&second) || second.contains(&first) {
                sum += 1;
            }
        }

        println!("{}", sum);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let mut sum = 0;

        for line in input.trim().split('\n') {
            let (first_str, second_str) = line.split_once(',').unwrap();
            let first = Interval::from_str(first_str);
            let second = Interval::from_str(second_str);

            if first.overlaps(&second) {
                sum += 1;
            }
        }

        println!("{}", sum);
    }
}
