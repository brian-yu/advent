#![feature(linked_list_cursors)]
#![feature(binary_heap_into_iter_sorted)]
use std::env;

mod day1;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;
mod day9;

pub trait Solution {
    fn part_1(&self) {}
    fn part_2(&self) {}
    fn run(&self) {
        println!("Running Part 1:");
        self.part_1();
        println!("Running Part 2:");
        self.part_2();
    }
}

pub fn run() {
    let args: Vec<String> = env::args().collect();

    let day = args
        .get(1)
        .expect("Please specify a day to run.")
        .parse::<u8>()
        .expect("Specified day must be parseable to an int");

    match day {
        1 => day1::code::Day {
            input_path: "src/day1/input.txt".to_string(),
        }
        .run(),
        2 => day2::code::Day {
            input_path: "src/day2/input.txt".to_string(),
        }
        .run(),
        3 => day3::code::Day {
            input_path: "src/day3/input.txt".to_string(),
        }
        .run(),
        4 => day4::code::Day {
            input_path: "src/day4/input.txt".to_string(),
        }
        .run(),
        5 => day5::code::Day {
            input_path: "src/day5/input.txt".to_string(),
        }
        .run(),
        6 => day6::code::Day {
            input_path: "src/day6/input.txt".to_string(),
        }
        .run(),
        7 => day7::code::Day {
            input_path: "src/day7/input.txt".to_string(),
        }
        .run(),
        8 => day8::code::Day {
            input_path: "src/day8/input.txt".to_string(),
        }
        .run(),
        9 => day9::code::Day {
            input_path: "src/day9/input.txt".to_string(),
        }
        .run(),
        10 => day10::code::Day {
            input_path: "src/day10/input.txt".to_string(),
        }
        .run(),
        11 => day11::code::Day {
            input_path: "src/day11/input.txt".to_string(),
        }
        .run(),
        12 => day12::code::Day {
            input_path: "src/day12/input.txt".to_string(),
        }
        .run(),
        13 => day13::code::Day {
            input_path: "src/day13/input.txt".to_string(),
        }
        .run(),
        14 => day14::code::Day {
            input_path: "src/day14/input.txt".to_string(),
        }
        .run(),
        _ => panic!("No solution exists for specified day."),
    }
}
