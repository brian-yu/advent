use std::fs;
use crate::Solution;

pub struct Day {
    pub input_path: String,
}

#[derive(Debug)]
struct Fish {
    timer: i32,
}

impl Solution for Day {
    fn part_1(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
        // let input = fs::read_to_string(&self.input_path.replace("input", "test")).unwrap();

        let mut fishes: Vec<Fish> = input.trim().split(",").map(
            |item| Fish {timer: item.parse::<i32>().unwrap()}
        ).collect();

        for _day in 0..80 {
            let mut new_fish: Vec<Fish> = Vec::new();
            for mut fish in &mut fishes { 
                match fish.timer {
                    0 => {
                        fish.timer = 6;
                        new_fish.push(Fish { timer: 8 })
                    },
                    _ => {
                        fish.timer -= 1;
                    }
                }
            }

            for fish in new_fish {
                fishes.push(fish);
            }
        }

        println!("{:?}", fishes.len())
    }

    fn part_2(&self) -> () {
        let input = fs::read_to_string(&self.input_path).unwrap();
    
        let mut timers = [0; 9];

        for fish in input.trim().split(",") {
            let timer: usize = fish.parse().unwrap();
            timers[timer] += 1;
        }

        for _day in 0..256 {
            let mut new_timers = [0; 9];
            for i in 1..9 {
                new_timers[i-1] = timers[i];
            }
            new_timers[8] = timers[0];
            new_timers[6] += timers[0];
            timers = new_timers
        }

        println!("{:?}", timers.iter().sum::<usize>());
    }
}

