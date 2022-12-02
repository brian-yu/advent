use crate::Solution;
use std::{collections::BinaryHeap, fs};

pub struct Day {
    pub input_path: String,
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let max = input
            .trim()
            .split("\n\n")
            .map(|lines| {
                lines
                    .split('\n')
                    .map(|line| line.parse::<u32>().unwrap())
                    .sum::<u32>()
            })
            .max()
            .unwrap();

        println!("{}", max);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let heap = BinaryHeap::from(
            input
                .trim()
                .split("\n\n")
                .map(|lines| {
                    lines
                        .split('\n')
                        .map(|line| line.parse::<u32>().unwrap())
                        .sum::<u32>()
                })
                .collect::<Vec<u32>>(),
        );

        let top_3_sum: u32 = heap.into_iter_sorted().take(3).sum();

        println!("{}", top_3_sum);
    }
}
