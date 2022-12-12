use crate::Solution;
use std::fs;

pub struct Day {
    pub input_path: String,
}

fn solve(input: &str) -> (i32, [char; 240]) {
    let mut cycle: i32 = 0;
    let mut x: i32 = 1;
    let mut sum = 0;
    let mut display = [' '; 240];
    for instruction in input.trim().split('\n') {
        let tokens: Vec<&str> = instruction.split_whitespace().collect();

        let (cycles_to_advance, to_add) = match tokens[0] {
            "noop" => (1, 0),
            "addx" => (2, tokens[1].parse::<i32>().unwrap()),
            _ => panic!("Invalid instruction: {}", instruction),
        };

        for _ in 0..cycles_to_advance {
            cycle += 1;

            if (cycle - 20) % 40 == 0 {
                sum += cycle * x;
            }

            for offset in -1..=1 {
                if ((cycle - 1) % 40) == ((x + offset) % 40) {
                    display[((cycle - 1) % 240) as usize] = '█';
                }
            }
        }

        x += to_add;
    }
    (sum, display)
}

impl Solution for Day {
    fn part_1(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let (sum, _) = solve(&input);

        println!("{}", sum);
    }

    fn part_2(&self) {
        let input = fs::read_to_string(&self.input_path).unwrap();

        let (_, display) = solve(&input);

        for row in display.array_chunks::<40>() {
            println!("{}", row.iter().collect::<String>());
        }
    }
}
