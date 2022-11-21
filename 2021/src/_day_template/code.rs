use std::fs;
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

impl Solution for Day {
    fn part_1(&self) -> () {
        // let input = fs::read_to_string(&self.input_path).unwrap();
        let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();
    
        println!("Part 1...");
        println!("{}", input);
    }

    fn part_2(&self) -> () {
        // let input = fs::read_to_string(&self.input_path).unwrap();
        let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();
    
        println!("Part 2...");
        println!("{}", input);
    }
}

