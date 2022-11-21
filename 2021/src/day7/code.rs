use std::{fs, collections::HashMap};
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

struct Space {
    min: u32,
    max: u32,
    cache: HashMap<u32, u32>,
}

impl Space {
    fn new(min: u32, max: u32) -> Space {
        Space { cache: HashMap::new(), min, max }
    }

    fn distance(&mut self, a: u32, b: u32) -> u32 {
        let absolute_diff = a.abs_diff(b);

        if let Some(scaled_diff) = self.cache.get(&absolute_diff) {
            return scaled_diff.clone();
        }

        let mut scaled_diff = 0;

        for diff in (1..=absolute_diff).rev() {
            if self.cache.contains_key(&diff) {
                let d = scaled_diff + self.cache.get(&diff).unwrap();
                self.cache.insert(absolute_diff, d);
                return d;
            }
            scaled_diff += diff;
        }

        self.cache.insert(absolute_diff, scaled_diff);
        scaled_diff
    }

    fn validate(&mut self, positions: &Vec<u32>, pos: u32) -> () {
        println!("========== Validating move to {}", pos);
        let mut cost = 0;
        for ship_pos in positions {
            let dist = self.distance(pos, *ship_pos);
            cost += dist;
            println!("Move from {} to {}: {} fuel", ship_pos, pos, dist);
        }

        println!("Total cost to move to {}: {}", pos, cost);
    }
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();

        let mut positions: Vec<i32> = input.trim().split(",").map(|i| i.parse().unwrap()).collect();

        positions.sort();

        let middle = (positions.len() - 1) / 2;
        let median = match positions.len() % 2 {
            0 => (positions[middle] + positions[middle + 1]) / 2,
            1 => positions[middle],
            _ => panic!("Bleh"),
        };

        let mut cost = 0;
        for position in positions {
            cost += median.abs_diff(position);

        }

        println!("{}", cost);
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();

        let positions: Vec<u32> = input.trim().split(",").map(|i| i.parse().unwrap()).collect();

        let min_pos = positions.iter().min().unwrap().clone();
        let max_pos = positions.iter().max().unwrap().clone();

        let mut space = Space::new(min_pos, max_pos);

        let mut best_cost = u32::MAX;

        for pos in space.min..=space.max {
            let mut cost = 0;
            for ship_pos in &positions {
                cost += space.distance(*ship_pos, pos);
            }
            best_cost = best_cost.min(cost);
        }
    
        println!("{}", best_cost);
    }
}

