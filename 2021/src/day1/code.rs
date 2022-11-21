use std::fs;
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
    
        let depths: Vec<u32> = input.trim().split('\n').map(|s| s.parse::<u32>().unwrap()).collect();
    
        let mut increasing_count = 0;
        for (idx, depth) in depths.iter().enumerate() {
            if idx == 0 {
                continue;
            }
            match depths.get(idx - 1) {
                Some(prev_depth) => {
                    if depth > prev_depth {
                        increasing_count += 1;
                    }
                },
                _ => ()
            }
        }
    
        println!("{}", increasing_count)
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
    
        let depths: Vec<u32> = input.trim().split('\n').map(|s| s.parse::<u32>().unwrap()).collect();
    
        let mut increasing_count = 0;
        for (idx, _) in depths.iter().enumerate() {
            let prev_window_sum = if idx >= 2 && idx+1 <= depths.len() {
                Some(depths[idx-2..idx+1].iter().sum::<u32>())
            } else {
                None
            };
            
            let curr_window_sum = if idx >= 1 && idx+2 <= depths.len() {
                Some(depths[idx-1..idx+2].iter().sum::<u32>())
            } else {
                None
            };

            if let (Some(prev_sum), Some(curr_sum)) = (prev_window_sum, curr_window_sum) {
                if curr_sum > prev_sum {
                    increasing_count += 1;
                }
            }
        }
    
        println!("{}", increasing_count)
    }
}

