use std::fs;
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

enum Direction {
    Up,
    Down,
    Forward,
}

impl Direction {
    fn parse(s: &str) -> Direction {
        match s {
            "forward" => Direction::Forward,
            "up" => Direction::Up,
            "down" => Direction::Down,
            s => panic!("Invalid direction: {}", s)
        }
    }
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
    
        let directions: Vec<&str> = input.trim().split('\n').collect();

        let mut horizontal_pos = 0;
        let mut depth = 0;

        for direction in directions {
            let mut iter = direction.split(" ");
            let direction = Direction::parse(iter.next().unwrap());
            let magnitude = iter.next().unwrap().parse::<u32>().unwrap();

            match direction {
                Direction::Forward => horizontal_pos += magnitude,
                Direction::Up => depth -= magnitude,
                Direction::Down => depth += magnitude
            }
        }
    
        println!("{:?} {:?} {:?}", horizontal_pos, depth, horizontal_pos * depth);
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
    
        let directions: Vec<&str> = input.trim().split('\n').collect();

        let mut aim = 0;
        let mut horizontal_pos = 0;
        let mut depth = 0;

        for direction in directions {
            let mut iter = direction.split(" ");
            let direction = Direction::parse(iter.next().unwrap());
            let magnitude = iter.next().unwrap().parse::<u32>().unwrap();

            match direction {
                Direction::Forward => {
                    horizontal_pos += magnitude;
                    depth += aim * magnitude;
                },
                Direction::Up => aim -= magnitude,
                Direction::Down => aim += magnitude
            }
        }
    
        println!("{:?} {:?} {:?}", horizontal_pos, depth, horizontal_pos * depth);
    }
}

